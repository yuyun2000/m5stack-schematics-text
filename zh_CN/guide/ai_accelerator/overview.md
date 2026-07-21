# LLM-8850 Card 使用指南

## 简介

**M5Stack LLM‑8850 Card** 是一款面向边缘设备的 **M.2 M‑Key 2242** AI 加速卡。AXERA 官方开源[SDK](https://huggingface.co/M5Stack/AX650_SDK_V3.6.2_for_Developer)地址。

## 快速上手

<div class="directory-links-container">

<div class="directory-links-item">
    <div class="directory-links-body">
        <ul>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_hardware_install">LLM-8850 Card 硬件安装 </a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_software_install">LLM-8850 Card 环境配置 </a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_quick_start">LLM-8850 Card 快速体验 </a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_windows_install">LLM-8850 Card Windows 环境配置 </a></li>        
        </ul>
    </div>
</div>

</div>

## 模型列表

<div class="card-container">

  <div class="card-item">
    <div class="card-cover linear-blue">视觉模型</div>
    <div class="card-desc">
      <ul>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_yolo11">YOLO11</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_yolo_world_v2">Yolo-World-V2</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_yolov7_face">Yolov7-face</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_depth_anything_v2">Depth-Anything-V2</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_mixformer_v2">MixFormer-V2</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_real_esrgan">Real-ESRGAN</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_superresolution">SuperResolution</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_rife">RIFE</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_ppocr_v5">PP-OCRv5</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_deimv2">DEIMv2</a></li>
      </ul>
    </div>
  </div>

  <div class="card-item">
    <div class="card-cover linear-gray">大语言模型</div>
    <div class="card-desc">
      <ul>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen3_0.6b">Qwen3-0.6B</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen3_1.7b">Qwen3-1.7B</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen3_4b">Qwen3-4B</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen2.5_0.5b">Qwen2.5-0.5B-Instruct</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen2.5_1.5b">Qwen2.5-1.5B-Instruct</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_deepseek">DeepSeek-R1-Distill-Qwen-1.5B</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_minicpm4">MiniCPM4-0.5B</a></li>
      </ul>
    </div>
  </div>

  <div class="card-item">
    <div class="card-cover linear-orange">多模态模型</div>
    <div class="card-desc">
      <ul>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen3.5_0.8b.">Qwen3.5-0.8B</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen3.5_2b">Qwen3.5-2B</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen3.5_4b">Qwen3.5-4B</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_internvl3">InternVL3-1B</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen2.5_vl">Qwen2.5-VL-3B-Instruct</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen3_vl_2b">Qwen3-VL-2B-Instruct</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_qwen3_vl_4b">Qwen3-VL-4B-Instruct-GPTQ-Int4</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_smolvlm2">SmolVLM2-500M-Video-Instruct</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_clip">LibCLIP</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_jina_clip_v2">Jina CLIP v2</a></li>
      </ul>
    </div>
  </div>
</div>

<div class="card-container">

  <div class="card-item">
    <div class="card-cover linear-orange">音频模型</div>
    <div class="card-desc">
      <ul>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_whisper">Whisper</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_melotts">MeloTTS</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_sensevoice">SenseVoice</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_cosy_voice2">CosyVoice2</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_3d_speaker_mt">3D-Speaker-MT</a></li>
      </ul>
    </div>
  </div>

  <div class="card-item">
    <div class="card-cover linear-orange">生成模型</div>
    <div class="card-desc">
      <ul>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_lcm_lora_sd">lcm-lora-sdv1-5</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_sd_demo">SD1.5-LLM8850</a></li>
        <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_liveportrait">LivePortrait</a></li>
      </ul>
    </div>
  </div>
</div>

- [查看更多模型](https://huggingface.co/AXERA-TECH)

## 应用列表

<div class="directory-links-item">
    <div class="directory-links-body">
        <ul>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_frigate">Frigate NVR</a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_immich">Immich</a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_openai">OpenAI API</a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_cosy_voice2_api">CosyVoice2 API</a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_sherpa-onnx">sherpa-onnx</a></li>
        </ul>
    </div>
</div>

## 进阶使用

<div class="directory-links-container">

<div class="directory-links-item">
    <div class="directory-links-body">
        <ul>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_axcl_smi">LLM-8850  Card AXCL-SMI </a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_npu_samples">LLM-8850  Card NPU 使用示例</a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_npu_benchmark">LLM-8850  Card NPU 基准</a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_samples">LLM-8850  Card AXCL-Sample 使用说明</a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_ffmpeg">LLM-8850  Card AXCL ffmpeg 使用示例</a></li>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_axcl_api">LLM-8850  Card AXCL SDK API</a></li>
        </ul>
    </div>
</div>

</div>

## 常见问题

<div class="directory-links-container">

<div class="directory-links-item">
    <div class="directory-links-body">
        <ul>
            <li><a href="/zh_CN/guide/ai_accelerator/llm-8850/m5_llm_8850_faq">LLM-8850 Card AXCL FAQ</a></li>
        </ul>
    </div>
</div>

</div>
