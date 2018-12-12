# -*- coding: utf-8 -*-

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_weather(city_name):
    url = 'https://api.seniverse.com/v3/weather/now.json?key=tyx1q4fjgqjmlu42'
    locality= "&location=" + city_name
    final_url=url+locality+"&language=zh-Hans&unit=c"

    r = requests.get(final_url)
    return_dict = r.json()
    result_dict_list = return_dict['results']  # 将results对应的key,转为字典列表
    weather_dict = result_dict_list[0]  #将字典列表,转为字典
    current_dict = weather_dict['now']  # 实时天气的具体情况,转为最新的列表

    # # weather_report = f‘city_name+' : '+ current_dict['text']+ " ; " +'温度 : '+current_dict['temperature']+'度'
    a = current_dict['text']
    b = current_dict['temperature']
    weather_report = "%s: %s 温度：%s℃" %(city_name,a,b)

    return weather_report
