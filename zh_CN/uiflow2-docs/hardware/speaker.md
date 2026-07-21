<!-- .. _hardware.Speaker: -->

# Speaker


<!-- .. include:: ../refs/system.ref -->
<!-- .. include:: ../refs/hardware.speaker.ref -->


The Speaker is used to control the built-in speaker inside the host device. 
Below is the detailed support for Speaker on the host:

<!-- .. table:: -->
    :widths: auto
    :align: center
###### 

###### [Controller       ] NS4168  [ AW88298 ] Buzzer  [

###### ] AirQ            [         ]         [ ]S[     ]

###### [ Atom Echo       ] [S]     [         ]         [

###### ] Atom Lite       [         ]         [         ]

###### [ Atom Martrix    ]         [         ]         [

###### ] AtomS3          [         ]         [         ]

###### [ AtomS3 Lite     ]         [         ]         [

###### ] AtomS3U         [         ]         [         ]

###### [ AtomU           ]         [         ]         [

###### ] Basic           [         ]         [         ]

###### [ Capsule         ]         [         ] [S]     [

###### ] Cardputer       [ ]S[     ]         [         ]

###### [ Core2           ] [S]     [         ]         [

###### ] CoreInk         [ ]S[     ]         [         ]

###### [ CoreS3          ]         [ ]S[     ]         [

###### ] Dial            [ ]S[     ]         [         ]

###### [ DinMeter        ] [S]     [         ]         [

###### ] Fire            [         ]         [         ]

###### [ Paper           ]         [         ]         [

###### ] Stamp PICO      [         ]         [         ]

###### [ StampS3         ]         [         ]         [

###### ] Station         [         ]         [         ]

###### [ StickC          ]         [         ] [S]     [

###### ] StickC PLUS     [         ]         [ ]S[     ]

###### [ StickC PLUS2    ]         [         ] [S]     [

###### ] TOUGH           [ ]S[     ]         [         ]


<!-- .. [S] unicode:: U+2714 -->


Micropython Example:

```python
# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

import os, sys, io
import M5
from M5 import *


circle0 = None
label0 = None


x = None
y = None


def setup():
    global circle0, label0, x, y

    M5.begin()
    Widgets.fillScreen(0x222222)
    circle0 = Widgets.Circle(160, 120, 60, 0xFFFFFF, 0xFFFFFF)
    label0 = Widgets.Label("Play", 141, 110, 1.0, 0x222222, 0xFFFFFF, Widgets.FONTS.DejaVu18)

    Speaker.begin()
    Speaker.playWavFile("/flash/res/audio/poweron_2_5s.wav")


def loop():
    global circle0, label0, x, y
    M5.update()
    if M5.Touch.getCount():
        x = M5.Touch.getX()
        y = M5.Touch.getY()
        if x >= 130 and x <= 190 and y >= 90 and y <= 150:
            circle0.setColor(color=0xFF0000, fill_c=0xFF0000)
            label0.setColor(0xFFFFFF, 0xFF0000)
            label0.setText(str("Play..."))
            Speaker.playWavFile("/flash/res/audio/poweron_2_5s.wav")
            label0.setText(str("Play"))
            circle0.setColor(color=0xFFFFFF, fill_c=0xFFFFFF)
            label0.setColor(0x000000, 0xFFFFFF)


if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg

            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")

```


UIFLOW2 Example:

    ![example.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/example.png)


<!-- .. only:: builder_html -->

    [cores3_speaker_example.m5f2]

    :download:`poweron_2_5s.wav <../../../examples/hardware/speaker/poweron_2_5s.wav>`

## class Speaker


<!-- .. important:: -->

    Methods of the Speaker Class heavily rely on ``M5.begin()`` ![M5.begin.png](https://static-cdn.m5stack.com/mpy_docs/system/system/begin.png) and ``M5.update()`` ![M5.update.png](https://static-cdn.m5stack.com/mpy_docs/system/system/update.png).

    All calls to methods of Speaker objects should be placed after ``M5.begin()`` ![M5.begin.png](https://static-cdn.m5stack.com/mpy_docs/system/system/begin.png), and ``M5.update()`` ![M5.update.png](https://static-cdn.m5stack.com/mpy_docs/system/system/update.png) should be called in the main loop.

<!-- .. _hardware.Speaker.Methods: -->

## Methods


<!-- .. method:: Speaker.config([cfg]) -->
            Speaker.config('param')
            Speaker.config(param=value)

    Get or set the parameters of the Speaker object.

    UIFLOW2:

        Read property:

            ==================  ===========  ===========
            Parameter           Type         Description
            ==================  ===========  ===========
            pin_data_out        (integer)    Serial data line of I2S, representing audio data in binary complement.
            pin_bck             (integer)    Serial clock line of I2S, corresponding to each bit of digital audio data.
            pin_ws              (integer)    Frame clock of I2S, used to switch left and right channel data.
            sample_rate         (integer)    Target sampling rate of output audio.
            stereo              (boolean)    Use stereo output.
            buzzer              (boolean)    Use single GPIO buzzer.
            use_dac             (boolean)    Use DAC speaker.
            dac_zero_level      (integer)    Zero level reference value when using DAC.
            magnification       (integer)    Multiplier of the input value.
            dma_buf_len         (integer)    DMA buffer length of I2S.
            dma_buf_count       (integer)    Number of DMA buffers of I2S.
            task_priority       (integer)    Priority of background tasks.
            task_pinned_core    (integer)    CPU used by background tasks.
            i2s_port            (integer)    I2S port.
            ==================  ===========  ===========

            Python::

                Speaker.config("pin_data_in")

            ![get_config.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/get_config.png)
            ![get_config1.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/get_config1.png)

        Set property:

            Python::

                Speaker.config(pin_data_in=1)

            ![set_config.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/set_config.png)
            ![set_config1.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/set_config1.png)


<!-- .. method:: Speaker.begin() -> bool -->

    Start the Speaker function. Returns True if successful.

    UIFLOW2:

        ![begin.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/begin.png)


<!-- .. method:: Speaker.end() -> None -->

    Disable the Speaker.

    UIFLOW2:

        ![end.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/end.png)


<!-- .. method:: Speaker.isRunning() -> bool -->

    Check if the Speaker is running. Returns a boolean value.

    UIFLOW2:

        ![isRunning.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/isRunning.png)


<!-- .. method:: Speaker.isEnabled() -> bool -->

    Check if the Speaker is enabled. Returns a boolean value.

    UIFLOW2:

        ![isEnabled.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/isEnabled.png)


<!-- .. method:: Speaker.isPlaying([channel]) -> bool -->

    Check if the Speaker is playing sound. Returns a boolean value.

    If the parameter ``channel`` is provided, it checks the playback status of
    the specified channel. ``channel`` accepts values from 0 to 7.

    UIFLOW2:

        ![isPlaying.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/isPlaying.png)


<!-- .. method:: Speaker.getPlayingChannels() -> int -->

    Get the number of channels currently playing.

    UIFLOW2:

        ![getPlayingChannels.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/getPlayingChannels.png)


<!-- .. method:: Speaker.setVolume(volume: int) -> None -->

    Set the master volume level for audio output. ``volume`` accepts volume levels from 0 to 255.

    UIFLOW2:

        ![setVolume.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/setVolume.png)


<!-- .. method:: Speaker.getVolume() -> int -->

    Get the master volume level for audio output. Returns volume levels from 0 to 255.

    UIFLOW2:

        ![getVolume.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/getVolume.png)


<!-- .. method:: Speaker.setVolumePercentage(percentage: float) -> None -->

    Set the master volume level for audio output as a percentage. ``percentage`` ranges from 0% to 100%.

    UIFLOW2:

        ![setVolumePercentage.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/setVolumePercentage.png)


<!-- .. method:: Speaker.getVolumePercentage() -> float -->

    Get the master volume level for audio output as a percentage. Returns volume levels from 0% to 100%.

    UIFLOW2:

        ![getVolumePercentage.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/getVolumePercentage.png)


<!-- .. method:: Speaker.setAllChannelVolume(volume: int) -> None -->

    Set the volume level for all virtual channels. ``volume`` accepts volume levels from 0 to 255.

    UIFLOW2:

        ![setAllChannelVolume.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/setAllChannelVolume.png)


<!-- .. method:: Speaker.setChannelVolume(channel: int, volume: int) -> None -->

    Set the volume level for a specific virtual channel.

    Parameters:

        - ``volume`` accepts volume levels from 0 to 255.
        - ``channel`` is the channel to play, ranging from 0 to 7.

    UIFLOW2:

        ![setChannelVolume.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/setChannelVolume.png)


<!-- .. method:: Speaker.getChannelVolume(channel) -> int -->

    Get the volume level for a specific virtual channel. ``channel`` ranges from 0 to 7.

    UIFLOW2:

        ![getChannelVolume.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/getChannelVolume.png)


<!-- .. method:: Speaker.stop([channel]) -> None -->

    Stop sound output. If ``channel`` is not specified, stop sound output for
    all channels. ``channel`` accepts values from 0 to 7.

    UIFLOW2:

        ![stop.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/stop.png)


<!-- .. method:: Speaker.tone(frequency, duration[, channel[, stop_current_sound]]) -> None -->

    Play a simple tone.

    Parameters:

        - ``frequency`` is the frequency of the tone in Hz.
        - ``duration`` is the duration of the tone in milliseconds.
        - ``channel`` is the channel to play, ranging from 0 to 7. By default, it is -1, which means using an available channel.
        - ``stop_current_sound`` controls whether to wait for the previous audio playback to finish. If True, start the new output without waiting for the current output to finish.

    UIFLOW2:

        ![tone.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/tone.png)


<!-- .. method:: Speaker.playRaw(wav_data: bytes[bytearray[, sample_rate: int[, stereo: bool[, repeat: int[, channel: int[, stop_current_sound: bool]]]]]) -> bool -->

    Play PCM data.

    Parameters:

        - ``wav_data`` is the buffer of audio data.
        - ``sample_rate`` is the sample rate of the audio data.
        - ``stereo`` specifies if the audio is stereo.
        - ``repeat`` is the number of times to repeat the audio. Default is 1.
        - ``channel`` is the channel to play, ranging from 0 to 7. By default, it is -1, which means using an available channel.
        - ``stop_current_sound`` controls whether to wait for the previous audio playback to finish. If True, start the new output without waiting for the current output to finish.

    UIFLOW2:

        ]playRaw.png[


<!-- .. method:: Speaker.playWav(wav_data: bytes]bytearray[, repeat: int[, channel: int[, stop_current_sound: bool]]]) -> None -->

    Play audio data in WAV format. Requires passing the raw data of the entire audio file.

    Parameters:

        - ``wav_data`` is the buffer of audio data.
        - ``repeat`` is the number of times to repeat the audio. Default is 1.
        - ``channel`` is the channel to play, ranging from 0 to 7. By default, it is -1, which means using an available channel.
        - ``stop_current_sound`` controls whether to wait for the previous audio playback to finish. If True, start the new output without waiting for the current output to finish.

    UIFLOW2:

        ![playWav.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/playWav.png)

<!-- .. method:: Speaker.playWavFile(path: str[, repeat: int[, channel: int[, stop_current_sound: bool]]]) -> None -->

    Play audio data in WAV format. Requires passing the raw data of the entire audio file.

    Parameters:

        - ``path`` is the path to the audio file.
        - ``repeat`` is the number of times to repeat the audio. Default is 1.
        - ``channel`` is the channel to play, ranging from 0 to 7. By default, it is -1, which means using an available channel.
        - ``stop_current_sound`` controls whether to wait for the previous audio playback to finish. If True, start the new output without waiting for the current output to finish.

    UIFLOW2:

        ![playWavFile.png](https://static-cdn.m5stack.com/mpy_docs/hardware/speaker/playWavFile.png)