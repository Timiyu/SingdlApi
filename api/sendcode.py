# -*- coding: utf-8 -*-
import requests
import json

MSGURL = "https://sms-api.luosimao.com/v1/send.json"

MSGAPIKEY = "key-e25c554d3dd58ffa207bbe1c950e5b7a"

MSGUSERNAME = "api"

requests.packages.urllib3.disable_warnings()

def send_message(phone, code):

    returnmsg = {}

    resp = requests.post(MSGURL, auth=(MSGUSERNAME, MSGAPIKEY), data={"mobile": phone, "message": "您的身份验证码是"+code+"，请您尽快完成验证！请不要将验证码泄露给他人，如非本人操作，请忽略！【新蝶在线】"}, timeout=3, verify=False)

    result = json.loads(resp.content)

    print(result)

    if result['error'] == 0 and result['msg'] == 'ok':

        returnmsg['error'] = 0

        return returnmsg         # 发送成功

    else:

        returnmsg['error'] = 1

        return returnmsg         # 发送失败

if __name__ == "__main__":

    phone = '13534187661'

    code = '123456'

    send_message(phone, code)
