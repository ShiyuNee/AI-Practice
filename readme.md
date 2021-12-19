:robot:本仓库致力于实现一款能用于对话的智能机器人

# :timer_clock:2021.11.all

:rocket:借助讯飞开放平台音频识别，文字翻译技术

:bridge_at_night:借助腾讯云音频合成与聊天机器人

:dart:Audio2Audio文件夹中包含语音相关的所有功能

​	:microphone:录音功能getAudio.py

​	:bread:语音转文字main.py（融合了其他功能作为主函数）

​	:smile_cat:中文转英文CHN2Eng.py

​	:smiling_imp:文字聊天机器人text2text.py

​	:cat2:通过文字合成音频text2Audio.py

合成结果为Audio2Audio/temp.wav

# :timer_clock:2021.12.14

:hand:增加了wav2lip模型[Rudrabha/Wav2Lip: This repository contains the codes of "A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild", published at ACM Multimedia 2020. (github.com)](https://github.com/Rudrabha/Wav2Lip)

:icecream:wav2lip模型能够将一段视频和一段音频进行匹配，从而使图片中的人物达到张嘴的效果。

​	:a:wav2lip/​tests文件夹中存储用于合成的音频和视频

​	:b:wav2lip/results中存储合成结果

:chicken:log中为运行记录

# :timer_clock: 2021.12.19

:open_hands:舍弃了腾讯云音频合成技术

:hand:增加了 Real-Time-Voice-Cloning-master模型[CorentinJ/Real-Time-Voice-Cloning: Clone a voice in 5 seconds to generate arbitrary speech in real-time (github.com)](https://github.com/CorentinJ/Real-Time-Voice-Cloning)

:rabbit:原因：实践过程中发现，wav2lip模型在音频为人声时匹配效果较好，使用腾讯云TTS技术生成的语音时，嘴唇匹配效果欠佳。考虑腾讯云合成语音与人声有一定差距

:tiger:改进：Real-Time-Voice-Cloning-master模型的输入为一个几秒钟的音频文件和一段文字，输出为利用该人声说出该段文字的语音

:running:过程中遇到的问题：

- repo中提供的预训练模型网址https://github.com/blue-fish/Real-Time-Voice-Cloning/releases/download/v1.0/pretrained.zip 已失效
- 最终在其他朋友提出的问题中找到答案[No such file or directory: 'synthesizer\\saved_models\\pretrained\\pretrained.pt' · Issue #524 · CorentinJ/Real-Time-Voice-Cloning (github.com)](https://github.com/CorentinJ/Real-Time-Voice-Cloning/issues/524)
- 通过谷歌网盘下载预训练模型 https://drive.google.com/drive/folders/1lb-LlS8Sx9RqcGzuV6GxvKHk-PC9TqQx?usp=sharing

:smile:结果：使用该模型合成的语音作为wav2lip的音频输入效果较好，同直接利用人声输入差别不大

