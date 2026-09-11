# Incremental Schematic Refresh Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Refresh newly added and schematic-changed M5Stack products from the current Nuxt documentation, publish their schematic descriptions, synchronize them back to Nuxt, refresh both knowledge bases without remote deletion, and push both repositories.

**Architecture:** Treat `nuxt-m5-docs/static/zh_CN` as the current product-document source and `m5stack-schematics-text` as the deterministic schematic-processing repository. Synchronize only source documents whose product identity or `## 原理图` resources changed, retain recoverable history for renamed paths, process affected products through manifest, asset, facts, validation, and publication stages, then use additive/overwrite-only knowledge synchronization.

**Tech Stack:** PowerShell 5.1, Python 3, Git, JSON Schema, local schematic pipeline, Volcengine knowledge-base API, S3-compatible ESP document storage.

---

### Task 1: Establish clean repository baselines

**Files:**
- Inspect: `D:/git/m5stack-schematics-text/AGENTS.md`
- Inspect: `C:/Users/15515/Documents/RecoveredProjects/nuxt-m5-docs/tools/knowledge/AGENTS.md`

1. Fetch both remotes and record branch divergence.
2. Preserve pre-existing Nuxt changes and ignored recovery evidence.
3. Confirm the current local and remote heads before editing.

### Task 2: Synchronize schematic discovery inputs

**Files:**
- Modify/Create: affected `zh_CN/**/*.md` product source documents
- Modify: `state/product_manifest.json`
- Modify: `schematic_products.xlsx`

1. Compare the current Nuxt source manifest with the repository manifest by product ID and schematic URL.
2. Copy only new, renamed, or schematic-URL-changed product source documents using byte-preserving file APIs.
3. Preserve renamed source history and do not delete unrelated source files.
4. Rebuild the product manifest twice; require the second JSON run to report `UNCHANGED`.

### Task 3: Fetch and publish affected schematics

**Files:**
- Local only: `artifacts/schematics/<product_id>/`
- Create/Modify: `artifacts/facts/<product_id>.json`
- Create/Modify: `generated_docs/*.md`
- Create/Modify: `zh_CN/schematic/*.md`
- Create/Modify: `reports/*-publish.json`

1. Create a dated fixed batch for genuinely new products.
2. Fetch every new or changed schematic and verify resource hashes and rendered pages.
3. Build or revise one product facts file at a time from the actual pages.
4. Run targeted validation before publishing each product.
5. Publish each product twice and require the second run to be unchanged.
6. Run batch verification, full publish dry-run, unit tests, encoding checks, and mirror hash checks.

### Task 4: Synchronize published descriptions to Nuxt

**Files:**
- Add/Overwrite only: `C:/Users/15515/Documents/RecoveredProjects/nuxt-m5-docs/static/zh_CN/schematic/*.md`

1. Pull Nuxt with `--ff-only` after verifying no conflict with existing local changes.
2. Copy all published schematic Markdown additively without deleting destination-only files.
3. Compare source and destination hashes for every copied document.

### Task 5: Refresh knowledge bases without deletion

**Files:**
- Generated/ignored: `tools/knowledge/output_csv/`
- Modify: `tools/knowledge/document_registry.json`
- Modify: `tools/knowledge/.file_hash_cache.json`
- Generated/ignored: `tools/knowledge/index.json`

1. Extract Markdown to structured CSV and audit expected additions/updates.
2. Upload structured documents by stable ID without calling missing-document cleanup or delete-before-replace paths.
3. Run ESP additive/overwrite-only upload and preserve remote orphan objects.
4. Re-run both paths to convergence; require zero pending structured changes and zero ESP uploads/deletions.
5. Verify the local and remote ESP index hashes match.

### Task 6: Commit, push, and verify remote parity

**Files:**
- Commit only task-related tracked files in each repository.

1. Review `git diff --check`, staged paths, file sizes, and secret exposure.
2. Commit and push `m5stack-schematics-text/main` without force.
3. Commit and push `nuxt-m5-docs/master` without including pre-existing deletion or recovery files.
4. Fetch both remotes and require `HEAD...origin/<branch>` to report `0 0`.
