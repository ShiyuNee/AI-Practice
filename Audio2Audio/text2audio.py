import base64
import json
import wave
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tts.v20190823 import tts_client, models


def getAudio(text):
    try:
        # 上传的时候记得把关键信息去掉
        cred = credential.Credential("AKIDvc3E8l7D3cuve6HDsHPHtEI5cttc4GBp", "OWNwDEyRdYCZfU3LQEm33mFRM0SeZDZf")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tts.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tts_client.TtsClient(cred, "ap-beijing", clientProfile)

        req = models.TextToVoiceRequest()
        params = {
            "Text": text,
            "SessionId": "302000009733",
            "ModelType": -1,
            "VoiceType": 101001
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextToVoice(req)
        wav_string = eval(resp.to_json_string())['Audio']

        wav_file = open(r"D:\AI\process\temp.wav", "wb")
        decode_string = base64.b64decode(wav_string)
        wav_file.write(decode_string)
        wav_file.close()


    except TencentCloudSDKException as err:
        print(err)