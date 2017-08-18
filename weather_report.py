#import sys
#import os

weather_dict={}

with open('weather_info.txt') as f:
    data = f.readlines()
                             #调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容
                            #并按行返回**list**。因此，要根据需要决定怎么调用。
                            #如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
    #print (data)                   #如果是配置文件，调用readlines()最方便：
for line in data:

    city = line.split(',')[0]
    #print (city)

    weather_info=line.split(',')[1].rstrip()
    # print(weather_info)
    weather_dict[city]=weather_info
    #print(weather_dict)
    history= {}
while True:


    user_input = input("请输入某个城市名称：")
    if user_input in weather_dict.keys():    #注意这里是if 不是for
        weather_report = weather_dict[user_input]
        #print (weather_report)
        print ("%s天气: %s" %(user_input, weather_report))
        history[user_input] = weather_report # 回头用list -city --对应到dict


    elif user_input == "history":
        for key,value in history.items():
                 print ("历史查询记录:%s" % key,value)


    elif user_input == "exit":
        for key,value in history.items():
                 print ("历史查询记录:%s" % key,value)
        exit(0)
    elif user_input == "help":
        print ("""
输入城市名，返回该城市的天气数据；
        输入h或help，打印帮助文档；
        输入history，打印查询历史；
        输入quit，退出程序。
               """
        )
    else:
        continue
