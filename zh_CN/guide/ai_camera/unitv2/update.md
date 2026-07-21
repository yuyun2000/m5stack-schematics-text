# UnitV2固件更新教程

## 固件下载

点击下方链接下载UnitV2固件压缩包,并将其解压至TF卡根目录放置。(`请直接放固件文件至TF卡根目录,请勿更改文件名称`)。

| 固件版本                               | 下载链接                                                                                                                          |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| M5UnitV2RootfsRecoveryPackage-09072021 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/firmware/UnitV2/M5UnitV2RootfsRecoveryPackage-09072021.zip) |


## 开始更新

?>注意:| UnitV2上的所有用户文件将会被`清空`。<br/> 电源必须足5v,第一次上电烧录中途不能断电。<br/> 等待的4分钟中LED灯会出现短暂的白灯微微亮之后白灯红灯同时亮的情况，因此看见白灯微微亮的情况需要等待10s左右，若红灯不亮则烧录完成。<br/> 烧录完后运行10S以上再断电。

#>烧录步骤:| 1. 解压成`M5UnitV2UpdPackage.img`, `请勿修改文件名`<br/>2. SD卡格式化成`FAT32`，把文件放到SD卡`根目录`。<br/>3. 断电关机的时候插入SD卡，按住主机顶部的按键不放，USB接口插上5V电源，红灯闪的时候松开。<br/>4. 上电1-2s后，红灯开始闪烁，闪烁2s后红灯常亮，此时松开顶部按键。<br/>5. 固件开始烧录，等待4分钟左右，最后红灯灭，白灯微微亮即可。

## 更新完成

更新完成后,设备指示灯将熄灭,此时将保持设备连接,通过浏览器访问域名`unitv2.py`或`IP:10.254.239.1`,若能成功访问在线识别功能页面(如下图所示)则表示更新完成。注意: 使用前请安装SR9900驱动,详情安装步骤可参考,前面章节[Jupyter notebook](/zh_CN/guide/ai_camera/unitv2/jupyter_notebook)


## 操作视频

<video width="600" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UNITV2_FW_UPDATE.mp4" type="video/mp4">
</video>

