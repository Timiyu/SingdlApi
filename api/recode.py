# -*- coding:utf-8 -*-

from datetime import date, datetime
import json


# 自定义时间处理类
class dataEncoder(json.JSONEncoder):

    def default(self, obj):

        # if isinstance(obj, datetime.datetime):
        #     return int(mktime(obj.timetuple()))

        if isinstance(obj, datetime):

            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, date):

            return obj.strftime('%Y-%m-%d')

        else:

            return json.JSONEncoder.default(self, obj)


# 对django.models对象进行处理返回json字符串的方法
def recode(data, isAscii=True):

    if isAscii == True:

        data = json.dumps(list(data), cls=dataEncoder, ensure_ascii=True)

    elif isAscii == False:

        data = json.dumps(list(data), cls=dataEncoder, ensure_ascii=False)

    return data


if __name__ == "__main__":

    data = {'phone': '15986751551'}

    recode(data)
