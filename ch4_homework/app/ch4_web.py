import sqlite3
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city_name):
    url = 'https://api.seniverse.com/v3/weather/now.json?key=tyx1q4fjgqjmlu42'
    locality= "&location=" + city_name
    final_url=url+locality+"&language=zh-Hans&unit=c"

    r = requests.get(final_url)
    print("status code", r.status_code)
    return_dict = r.json()
    result_dict_list = return_dict['results']  # 将results对应的key,转为字典列表
    # print("all information:", result_dict_list)
    weather_dict = result_dict_list[0]  #将字典列表,转为字典
    current_dict = weather_dict['now']  # 实时天气的具体情况,转为最新的列表

    _weather = current_dict['text']
    _temperature = current_dict['temperature']
    weather_report = city_name+' : '+ current_dict['text']+ " ; " +'温度 : '+current_dict['temperature']
    _info = [weather_report,city_name, _weather, _temperature]  #['北京 : 多云 ; 温度 : 25', '多云', '25']
    # print(_info)
    return _info

def create_db():
    conn = sqlite3.connect('ch4.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS stocks (city TEXT , weather TEXT, temperature TEXT)')
    conn.commit()  ## 必须commit
    conn.close()

def store_db(city,main_info,temp):
    conn = sqlite3.connect('ch4.db')
    c = conn.cursor()
    c.execute("INSERT INTO stocks VALUES (?,?,?)", (city, main_info, temp))

    conn.commit()  ## 必须commit
    conn.close()

def retrieve_db(location):
    conn = sqlite3.connect('ch4.db')
    with conn:
        c = conn.cursor()
        c.execute('SELECT * FROM stocks WHERE city = :city' , {'city': location} )
        row = c.fetchone()
        # print(f'{location} 天气:{row[1]} ; 温度:{row[2]}' )
        weather_report = f'{row[0]} 天气:{row[1]} ; 温度:{row[2]}'
        return weather_report

def update_db(location, newinfo):
    conn = sqlite3.connect('ch4.db')
    with conn:
        c = conn.cursor()

        c.execute("UPDATE stocks SET weather = ? WHERE city=?", (newinfo, location))
        # cur.execute("UPDATE stocks SET temperature = ? WHERE city=?", (newtemp, location))

def get_history( ):
    conn = sqlite3.connect('ch4.db')
    with conn:
        c = conn.cursor()
        c.execute('SELECT * FROM stocks')
        rows = c.fetchall()
        return rows

create_db()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user_inquiry')

def _processing():
    city_name = request.args.get('city')
    try:
        if request.args.get('query') == '查询':
            # city_name = request.args.get('city')

            try:
                weather_report = retrieve_db(city_name)
                return render_template("query.html", weather_report = weather_report)

            except TypeError:
                weather_report = get_weather(city_name)[0]
                # history_list.append(weather_report)
                store_db(get_weather(city_name)[1],get_weather(city_name)[2],get_weather(city_name)[3])
                return render_template("query.html", weather_report = weather_report)

        elif request.args.get('history') == '历史':
            history = get_history()
            return render_template("history.html", history = history)
        elif request.args.get('help') == '帮助':
            return render_template("help.html")

        elif request.args.get('update') == '更新':
            # city_name = request.args.get('city')

            # update_info = city_name.split(" ")
            # update_db(update_info[0], update_info[1])
            add_city,add_info = city_name.split(" ")
            update_db(add_city,add_info)
            # # update_message = "天气信息,已经更新"
            return render_template("update.html")




    except ValueError:
            return render_template("404.html")

if __name__ == '__main__':
    app.run(debug = True)
