# -*- coding:utf8 -*-

import re


def phonecheck(data):

    #正则表达式pattern

    pattern = r"^1[3-9]\d{9}$"

    result = re.findall(pattern, data)

    if result:

        return True

    else:

        return False
