import requests,datetime,json
dt=datetime.datetime.now()
enddate=int(dt.timestamp())
dt=enddate-4*24*60*60
days=5
datajson=[]
sun_sec=[]
sub_temp=[]
param={
    'lat':'55.75',
    'lon':'37.61',
    'dt':str(dt),
    'appid':'976c371210bde351b4db2275aa98352e',
    'units':'metric',
    'lang':'ru'
}
for i in range(days):
    res=requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine',params=param)
    datajson.append(json.loads(res.text))
    sun_sec.append((datajson[i]["current"]["sunset"]-datajson[i]["current"]["sunrise"],int(param['dt'])))
    print(datetime.datetime.utcfromtimestamp(int(param['dt'])).strftime('%Y-%m-%d ')+res.url)
    param['dt']=str(dt+(i+1)*24*60*60)    
max_sun=max(sun_sec,key=lambda item:item[0])
print()
print('Максимальная продолжительность светового дня '+str(datetime.timedelta(seconds=max_sun[0]))+' наблюдалась '+ datetime.datetime.utcfromtimestamp(max_sun[1]).strftime('%Y-%m-%d'))
#в качестве ночи возьму астрономическую ночь - с заката до восхода солнца
for i in range(days):
    for dj in datajson[i]["hourly"]:
        if dj["dt"]<=datajson[i]["current"]["sunrise"] or dj["dt"]>=datajson[i]["current"]["sunset"]:
            sub_temp.append((abs(dj["temp"]-dj["feels_like"]),i,dj["dt"]))  
min_sub=min(sub_temp,key=lambda item:item[0])
print('Минимальная разница ощущаемой и фактической температуры ночью составила '+str(round(min_sub[0],2))+' градусов и достигнута в '+str(min_sub[1]+1)+'-й день - '+datetime.datetime.utcfromtimestamp(min_sub[2]).strftime('%Y-%m-%d'))