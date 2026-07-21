# Module GPS v2.0 拨码开关说明文档

## 1. 简介

### 1.1 概述

为避免 Module GPS v2.0 与主机堆叠时因引脚冲突产生问题，模块采用拨码开关灵活切换关键引脚的连接方式。用户可根据所使用的主机（如 Core/Basics、Core2 或 CoreS3）调整对应的引脚配置，从而确保系统稳定运行。

### 1.2 位置说明

拨码开关位于模块指定位置，用于控制三个功能引脚：TXD、RXD 和 PPS。

<img alt="模块外观" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/950/M003_V2_dip_switch_01.png" width="30%" />

模块上的`OFF`表示关闭该引脚，`ON`表示打开该引脚。**TXD、RXD、PPS** 均可通过拨码开关选择具体连接的引脚。每个功能只能同时打开一个引脚。

<img alt="拨码开关局部" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/950/M003_V2_dip_switch_02.png" width="30%" />

>

根据不同主机，关键引脚的可选映射如下表所示（与模块上的数字自上而下一一对应）。

<table>
  <tr>
    <th></th>
    <th>CORE</th>
    <th>CORE2</th>
    <th>CORS3</th>
  </tr>
  <tr>
    <th rowspan="4">TXD</th>
    <td>G17</td>
    <td>G14</td>
    <td>G17</td>
  </tr>
  <tr>
    <td>G15</td>
    <td>G2</td>
    <td>G13</td>
  </tr>
  <tr>
    <td>G12</td>
    <td>G27</td>
    <td>G6</td>
  </tr>
  <tr>
    <td>G0</td>
    <td>G0</td>
    <td>G0</td>
  </tr>
  <tr>
    <th rowspan="4">RXD</th>
    <td>G16</td>
    <td>G13</td>
    <td>G18</td>
  </tr>
  <tr>
    <td>G13</td>
    <td>G19</td>
    <td>G7</td>
  </tr>
  <tr>
    <td>G34</td>
    <td>G34</td>
    <td>G14</td>
  </tr>
  <tr>
    <td>G35</td>
    <td>G35</td>
    <td>G10</td>
  </tr>
  <tr>
    <th rowspan="3">PPS</th>
    <td>G25</td>
    <td>G25</td>
    <td>G5</td>
  </tr>
  <tr>
    <td>G35</td>
    <td>G35</td>
    <td>G10</td>
  </tr>
  <tr>
    <td>G36</td>
    <td>G36</td>
    <td>G8</td>
  </tr>
</table>

例如，**在 Core (Basic) 主机上**：

- **TXD**：可选 G17、G15、G12 或 G0（四选一）
- **RXD**：可选 G16、G13、G34 或 G35（四选一）
- **PPS**：可选 G25、G35 或 G36（三选一）

## 使用指导

下面介绍调整拨码开关配置的步骤。

1. **模块断电**。在调整拨码开关前，请确保模块完全断电，避免损坏硬件。

2. **设置拨码开关**。根据所使用的主机选择相应的引脚映射。

 <img alt="拨码开关设置示意图1" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/950/M003_V2_dip_switch_03.png" width="30%" />

> <br/>如上图，拨码开关的位置被选择为： <br/>TXD → G12 <br/>RXD → G34 <br/>PPS → G25

3. **重新接线并上电**。完成拨码开关设置后，重新连接模块，并接通电源进行后续使用。
