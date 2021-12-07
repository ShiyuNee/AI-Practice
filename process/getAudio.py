import pyaudio
import wave
import os
import subprocess
import time


def process_video(filename):
    name = filename.split("\\")[-1]
    os.chdir("D:\\AI\\audio")
    retval = os.getcwd()
    print(retval)
    a = os.system("ffmpeg -y -i " + name + ".mp3 -acodec pcm_s16le -f s16le -ac 1 -ar 16000 " + name + ".pcm")
    print(a)

    # cmd = "D:\\AI\\audio"
    # os.chdir(cmd)
    # cmd = "ffmpeg -y -i test.mp3 -acodec pcm_s16le -f s16le -ac 1 -ar 16000 test.pcm"
    # res = os.system(cmd)
    # print(res)


def start_audio(time, filename):
    save_file = filename + '.mp3'
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = time  # 需要录制的时间
    WAVE_OUTPUT_FILENAME = save_file  # 保存的文件名

    p = pyaudio.PyAudio()  # 初始化
    print("ON")

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)  # 创建录音文件
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)  # 开始录音

    print("OFF")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')  # 保存
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    process_video(filename)



