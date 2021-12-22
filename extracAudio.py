from moviepy.editor import AudioFileClip
my_audio_clip = AudioFileClip(r"D:\AI\wav2lip\results\阅读男生.mp4")
my_audio_clip.write_audiofile(r"D:\AI\阅读男声.wav")
