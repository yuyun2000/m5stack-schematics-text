from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Any

try:
    from .pipeline_common import PROJECT_ROOT, load_json
    from .validate_description import validate_files
except ImportError:
    from pipeline_common import PROJECT_ROOT, load_json  # type: ignore
    from validate_description import validate_files  # type: ignore


CATEGORY_TITLES = {
    "system": "系统结构",
    "component": "核心器件",
    "power": "电源",
    "interface": "接口",
    "bus": "总线",
    "address": "总线地址",
    "gpio": "GPIO 与控制信号",
    "clock": "时钟",
    "reset": "复位",
    "protection": "保护电路",
    "key_net": "关键网络",
    "storage": "存储",
    "memory": "内存与 Flash",
    "audio": "音频",
    "sensor": "传感器",
    "rf": "射频",
    "debug": "调试与烧录",
    "analog": "模拟电路",
    "other": "其他事实",
}


def evidence_text(evidence: list[dict[str, Any]]) -> str:
    return "; ".join(
        f"图 {item['asset_sha256'][:12]} / 第 {item['page']} 页 / {item['locator']}"
        for item in evidence
    )


def attributes_text(attributes: dict[str, Any]) -> str:
    if not attributes:
        return ""
    def display_value(value: Any) -> str:
        if value is None:
            return "null"
        if isinstance(value, bool):
            return str(value).lower()
        return str(value)

    return "；".join(f"`{key}={display_value(value)}`" for key, value in attributes.items())


def render_markdown(data: dict[str, Any]) -> str:
    product = data["product"]
    lines = [
        f"# {product['product_name']} 原理图描述",
        "",
        "## 快速信息",
        "",
        "| 项目 | 内容 |",
        "| --- | --- |",
        f"| 产品 | {product['product_name']} |",
        f"| SKU | {product['sku'] or '源文档未标注'} |",
        f"| 产品 ID | `{product['product_id']}` |",
        f"| 源文档 | `zh_CN/{product['source_path']}` |",
        "",
        "## 概述",
        "",
        data["summary"].strip(),
        "",
        "## 检索关键词",
        "",
        "、".join(f"`{keyword}`" for keyword in data["keywords"]),
        "",
    ]

    if data["components"]:
        lines.extend(["## 主要器件", "", "| 位号 | 型号 | 作用 | 证据 |", "| --- | --- | --- | --- |"])
        for item in data["components"]:
            part_number = item["part_number"] or "未标注"
            lines.append(
                f"| {item['reference']} | {part_number} | {item['role']} | {evidence_text(item['evidence'])} |"
            )
        lines.append("")

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    uncertain: list[dict[str, Any]] = []
    for fact in data["facts"]:
        if fact["confidence"] == "confirmed":
            grouped[fact["category"]].append(fact)
        else:
            uncertain.append(fact)
    for category in CATEGORY_TITLES:
        facts = grouped.get(category, [])
        if not facts:
            continue
        lines.extend([f"## {CATEGORY_TITLES[category]}", ""])
        for fact in facts:
            lines.append(f"### {fact['subject']}")
            lines.append("")
            lines.append(fact["statement"])
            if fact["attributes"]:
                lines.extend(["", f"- 参数与网络：{attributes_text(fact['attributes'])}"])
            lines.append(f"- 证据：{evidence_text(fact['evidence'])}")
            lines.append("")

    indexed_facts = [fact for fact in data["facts"] if fact["attributes"]]
    if indexed_facts:
        lines.extend(["## 参数与信号索引", "", "| 分类 | 对象 | 参数 |", "| --- | --- | --- |"])
        for fact in indexed_facts:
            lines.append(
                f"| {CATEGORY_TITLES[fact['category']]} | {fact['subject']} | {attributes_text(fact['attributes'])} |"
            )
        lines.append("")

    lines.extend(["## 待确认事项", ""])
    if uncertain or data["needs_review"]:
        for fact in uncertain:
            lines.append(f"- `{fact['id']}`：{fact['statement']}（证据：{evidence_text(fact['evidence'])}）")
        for item in data["needs_review"]:
            lines.append(f"- `{item['id']}`：{item['question']}；原因：{item['reason']}")
    else:
        lines.append("- 无：当前结构化事实中没有标记为 `uncertain` 的内容。")
    lines.append("")

    lines.extend(["## 原理图来源", "", "| 资源 | 页码 | SHA-256 | 原始地址 |", "| --- | --- | --- | --- |"])
    for index, asset in enumerate(data["schematic_assets"], start=1):
        pages = ", ".join(str(page) for page in asset["pages"])
        lines.append(
            f"| {index} | {pages} | `{asset['sha256']}` | `{asset['source_url']}` |"
        )
    lines.append("")

    lines.extend(
        [
            "---",
            "",
            f"源文档：`zh_CN/{product['source_path']}`",
            "",
            f"源文档 SHA-256：`{product['source_sha256']}`",
            "",
            "*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render validated schematic facts as Markdown")
    parser.add_argument("facts", type=Path)
    parser.add_argument("--manifest", type=Path, default=PROJECT_ROOT / "state" / "product_manifest.json")
    parser.add_argument("--assets-root", type=Path, default=PROJECT_ROOT / "artifacts" / "schematics")
    parser.add_argument("--schema", type=Path, default=PROJECT_ROOT / "schemas" / "schematic-description.schema.json")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    raw = load_json(args.facts)
    product_id = raw.get("product", {}).get("product_id")
    asset_manifest_path = args.assets_root / product_id / "asset_manifest.json"
    data, product, errors = validate_files(
        args.facts,
        manifest_path=args.manifest,
        asset_manifest_path=asset_manifest_path,
        schema_path=args.schema,
    )
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    output = args.output or (PROJECT_ROOT / "generated_docs" / product["output_filename"])
    encoded = render_markdown(data).encode("utf-8")
    changed = not output.exists() or output.read_bytes() != encoded
    if changed:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(encoded)
    print(f"[{'UPDATED' if changed else 'UNCHANGED'}] {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
