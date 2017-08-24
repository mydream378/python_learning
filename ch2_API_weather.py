import requests
# def weather_search():

# {  心知API 原始文档
#   "results": [{
#   "location": {
#       "id": "C23NB62W20TF",
#       "name": "西雅图",
#       "country": "US",
#       "timezone": "America/Los_Angeles",
#       "timezone_offset": "-07:00"
#   },
#   "now": {
#       "text": "多云", //天气现象文字
#       "code": "4", //天气现象代码
#       "temperature": "14", //温度，单位为c摄氏度或f华氏度
#       "feels_like": "14", //体感温度，单位为c摄氏度或f华氏度
#       "pressure": "1018", //气压，单位为mb百帕或in英寸
#       "humidity": "76", //相对湿度，0~100，单位为百分比
#       "visibility": "16.09", //能见度，单位为km公里或mi英里
#       "wind_direction": "西北", //风向文字
#       "wind_direction_degree": "340", //风向角度，范围0~360，0为正北，90为正东，180为正南，270为正西
#       "wind_speed": "8.05", //风速，单位为km/h公里每小时或mph英里每小时
#       "wind_scale": "2", //风力等级，请参考：http://baike.baidu.com/view/465076.htm
#       "clouds": "90", //云量，范围0~100，天空被云覆盖的百分比 #目前不支持中国城市#
#       "dew_point": "-12" //露点温度，请参考：http://baike.baidu.com/view/118348.htm #目前不支持中国城市#
#   },
#   "last_update": "2015-09-25T22:45:00-07:00" //数据更新时间（该城市的本地时间）
#   }]
# }



history_list =  []
while True:
    city_name = input(">")
    try:
        url = 'https://api.seniverse.com/v3/weather/now.json?key=tyx1q4fjgqjmlu42'

        locality= "&location=" + city_name
        final_url=url+locality+"&language=zh-Hans&unit=c"

        r = requests.get(final_url)
        # print("Status code:", r.status_code)
        return_dict = r.json()


        result_dict_list = return_dict['results']  # 将results对应的key,转为字典列表
        # print("all information:", result_dict_list)
        weather_dict = result_dict_list[0]  #将字典列表,转为字典
        current_dict = weather_dict['now']  # 实时天气的具体情况,转为最新的列表

        # print(current_dict)
        print("%s的天气:%s;温度:%s度,湿度:%s,风向:%s" %(city_name,current_dict['text'],current_dict['temperature'],current_dict['humidity'],current_dict['wind_direction']))
        print("更新时间:", weather_dict['last_update'])
        print("\n")

        weather_report = city_name+'的天气:'+ current_dict['text']+ ";" +'温度:'+current_dict['temperature'] +";"+'湿度:'+current_dict['humidity']+";"+'风向:'+current_dict['wind_direction']

        history_list.append(weather_report)
        # print(history_list)


        # for i in history_list:
        #     print (i)
        # history_info = {
        # "天气:":current_dict['text'],
        # "温度:":current_dict['temperature'],
        # "湿度:":current_dict['humidity'],
        # "风向:":current_dict['wind_direction']
        # }
        # history_dict[city_name]=history_info
        # print(history_dict)
    except KeyError:

        if city_name == 'history':
            for item in history_list:
                print(item)
            # print(history_list)

        elif city_name in ['help','h']:  #city_name in ['h','help']
            print ("""
    输入城市名，返回该城市的天气数据；
    输入h或help，打印帮助文档；
    输入history，打印查询历史；
    输入exit，退出程序。
                   """
            )

        elif city_name == 'exit':
            print('你已退出查询程序。')
            break
        else :
            print('对不起，你输入的城市不存在，请检查后重新输入。')
