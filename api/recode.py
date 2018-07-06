# -*- coding:utf-8 -*-

from datetime import date, datetime
import json

class MyEncoder(json.JSONEncoder):

    def default(self, obj):

        # if isinstance(obj, datetime.datetime):
        #     return int(mktime(obj.timetuple()))

        if isinstance(obj, datetime):

            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, date):

            return obj.strftime('%Y-%m-%d')

        else:

            return json.JSONEncoder.default(self, obj)

def recode(data):

    data = json.dumps(list(data), cls=MyEncoder, ensure_ascii=False)

    return data