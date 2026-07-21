# UiFlow2 添加自定义字体指南

> UiFlow2 UI Editor 支持引用外部字体功能，助力用户实现更丰富的设计表现力。

## 1. 准备工作

在使用自定义字体前，请确保：

- 已获取合法的字体文件（.ttf 格式）

- 了解字体文件的授权许可范围

- 测试字体用例：[阿里巴巴普惠体](https://www.alibabafonts.com/#/font)

> 注意：请遵守字体版权相关规定，确保商业使用合法性

## 2.添加字体步骤

- 1.访问 [UiFlow2 Web IDE](https://uiflow2.m5stack.com/)

- 2.打开 UI 模拟器，进入设计界面

- 3.拖拽任意`Title`或`Label`组件至画布

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/font/font_01.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/font/font_02.png" width="70%">

- 4.在属性面板的字体配置区域，点击`Create Font`按钮，把下载好的字体 ttf 文件上传

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/font/font_03.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/font/font_06.png" width="70%">

## 3.字体优化设置（必选）

提供两种字体加载方式：符号加载和范围加载。两种方式可组合使用，建议根据实际需求选择。由于设备存储限制，必须选择至少一种加载方式。

### 范围加载（Range）

通过 Unicode 编码范围导入特定字符集。示例：ASCII 字符(0x20-0x7F)、中文常用字(0x4E00-0x9FA5)

> 优点：适合连续编码的字符集。注意：请提前查阅字体编码表，范围不宜过大

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/font/font_05.png" width="70%">

### 符号加载（Symbols）

直接输入需要使用的具体字符。示例：输入"Hello M5Stack"，则仅这些字符可用

> 优点：精准控制，节省空间。注意：需包含所有可能需要使用的字符

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/font/font_07.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/font/font_08.png" width="70%">

## 4.最佳实践建议

- 字体精简：优先使用 Symbols 方式，仅添加必要字符

- 多语言支持：如需显示多种语言，请确保包含相应字符集

- 性能优化：单个项目建议使用不超过 3 种自定义字体

- 测试验证：添加字体后请实际运行测试显示效果
