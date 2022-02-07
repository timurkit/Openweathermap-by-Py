Программу, которая на основании данных сервиса https://openweathermap.org/ будет выводить следующие данные для Вашего города: 

1. День, с минимальной разницей "ощущаемой" и фактической температуры ночью (с указанием разницы в градусах Цельсия) 

2. Максимальную продолжительностью светового дня (считать, как разницу между временем заката и рассвета) за ближайшие 5 дней (включая текущий), с указанием даты.

Посчитал нужным иметь возможность проверять данные, так что добавил ссылки по дням.

Output:

2022-01-27 https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=55.75&lon=37.61&dt=1643303655&appid=976c371210bde351b4db2275aa98352e&units=metric&lang=ru

2022-01-28 https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=55.75&lon=37.61&dt=1643390055&appid=976c371210bde351b4db2275aa98352e&units=metric&lang=ru

2022-01-29 https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=55.75&lon=37.61&dt=1643476455&appid=976c371210bde351b4db2275aa98352e&units=metric&lang=ru

2022-01-30 https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=55.75&lon=37.61&dt=1643562855&appid=976c371210bde351b4db2275aa98352e&units=metric&lang=ru

2022-01-31 https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=55.75&lon=37.61&dt=1643649255&appid=976c371210bde351b4db2275aa98352e&units=metric&lang=ru

Максимальная продолжительность светового дня 8:34:16 наблюдалась 2022-01-31
Минимальная разница ощущаемой и фактической температуры ночью составила 0.0 градусов и достигнута в 3-й день - 2022-01-29



