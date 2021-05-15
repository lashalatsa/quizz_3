# # # გამოვიყენე breaking bad API და შემდეგი url-ები
##  "characters": "https://breakingbadapi.com/api/characters",
##  "episodes": "https://breakingbadapi.com/api/episodes",
##  "quotes": "https://breakingbadapi.com/api/quotes",
##  "deaths": "https://breakingbadapi.com/api/deaths"



# # 1 საკითხი
# import requests
# url = 'https://breakingbadapi.com/api/characters'
# resp = requests.get(url)
# print(resp)
# print(resp.status_code)
# print(resp.headers)
# print(resp.text)



# # 2 საკითხი
# import requests
# import json
# url = "https://breakingbadapi.com/api/quotes"
# url_2 = "https://breakingbadapi.com/api/episodes"
# r = requests.get(url)
# r_2 = requests.get(url_2)
# res = r.json()
# res_2 = r_2.json()
#
# file = open('quotes_data.json','w')
# json.dump(res,file, indent=4)
#
# file = open('episodes_data.json','w')
# json.dump(res_2,file, indent=4)
# file.close()



# # 3 საკითხი
# import requests
# name = input('enter the name of the actor:')
# url = f'https://breakingbadapi.com/api/characters?name={name}'           ##მაგალითად :  walter,  jesse,  skyler
# r = requests.get(url)
# res = r.json()
# print('მსახიობის ნამდვილი სახელია:', res[0]['portrayed'])
# print('ფილმში მისი მეტსახელია:', res[0]['nickname'])
# print('დაბადების თარიღია:', res[0]['birthday'])
# print('მისი პროფესიაა:', res[0]['occupation'][0])




# # 4 საკითხი
# import sqlite3
# conn = sqlite3.connect('film_db.sqlite')
# c = conn.cursor()
#
# import requests
# url = 'https://breakingbadapi.com/api/characters'
# r = requests.get(url)
# res = r.json()
# full_info=[]
# for each in res:
#     birthday = each['birthday']
#     name = each['name']
#     nickname = each[ 'nickname']
#     portrayed = each['portrayed']
#     status  = each['status']
#     info = (birthday, name, nickname, portrayed, status)
#     full_info.append(info)
#
# c.execute('''CREATE TABLE if not exists film(
#            id integer primary key autoincrement,
#            birthday varchar(15),
#            name varchar(25),
#            nickname varchar(25),
#            portrayed varchar (25),
#            status varchar(25)
#            )''')
#
#
# c.executemany('INSERT INTO film(birthday, name, nickname, portrayed, status) VALUES(?,?,?,?,?)', full_info)
# conn.commit()
# ## ცხრილში film ინახება მსახიობების სახელები, მეტსახელები, ნამდვილი სახელები და სტატუსი სიცოცხლის შესახებ
