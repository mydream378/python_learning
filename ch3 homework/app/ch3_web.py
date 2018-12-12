from flask import Flask, render_template, request
import requests
app = Flask(__name__)

def get_weather(city_name):
    url = 'https://api.seniverse.com/v3/weather/now.json?key=tyx1q4fjgqjmlu42'
    locality= "&location=" + city_name
    final_url=url+locality+"&language=zh-Hans&unit=c"

    r = requests.get(final_url)
    return_dict = r.json()
    result_dict_list = return_dict['results']  # 将results对应的key,转为字典列表
    # print("all information:", result_dict_list)
    weather_dict = result_dict_list[0]  #将字典列表,转为字典
    current_dict = weather_dict['now']  # 实时天气的具体情况,转为最新的列表

    # print(current_dict)
    # print("%s天气: %s; " " + 温度:%s度; 湿度: %s; 风向: %s" %(city_name,current_dict['text'],current_dict['temperature'],current_dict['humidity'],current_dict['wind_direction']))
    # print("更新时间:", weather_dict['last_update'])
    # print("%s天气: %s; "
    #       " + 温度:%s度; 湿度: %s; 风向: %s" %
    #       (city_name, current_dict['text'], current_dict['temperature'],
    #       current_dict['humidity'], current_dict['wind_direction']))
    # print("\n")
    weather_report = city_name+' : '+ current_dict['text']+ " ; " +'温度 : '+current_dict['temperature']+‘度’

    return weather_report


history_list = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user_inquiry')
def _processing():
    try:
        if request.args.get('help') == '帮助':
            return render_template("help.html")
        elif request.args.get('query') == '查询':
            city_name = request.args.get('city')

            weather_report = get_weather(city_name)

            history_list.append(weather_report)

            return render_template("query.html", weather_report = weather_report)

        elif request.args.get('history') == '历史':

            return render_template("history.html",history_list = history_list)
    except:
            return render_template("404.html")

if __name__ == '__main__':
    app.run(debug = True)
