# -*- coding: utf-8 -*-
import requests
import json

MSGURL = "https://sms-api.luosimao.com/v1/send.json"

MSGAPIKEY = "key-e25c554d3dd58ffa207bbe1c950e5b7a"

MSGUSERNAME = "api"

requests.packages.urllib3.disable_warnings()

def send_message(phone, code):

    resp = requests.post(MSGURL, auth=(MSGUSERNAME, MSGAPIKEY), data={"mobile": phone, "message": "您的身份验证码是"+code+"，请您尽快完成验证！请不要将验证码泄露给他人，如非本人操作，请忽略！【新蝶在线】"}, timeout=3, verify=False)

    result = json.loads(resp.content)

    print(result)

    if result['error'] == 0:

        return {'error': 0}         # 发送成功

    else:
        return {'error': 1}         # 发送失败

if __name__ == "__main__":

    phone = '15986751551'

    code = '123456'

    send_message(phone, code)
