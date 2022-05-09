from __future__ import unicode_literals

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time



from bs4 import BeautifulSoup
import lxml
import requests 

import youtube_dl

import os
import eyed3

#headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

print("Insert the keyword")

keyword=input("")
url='https://www.youtube.com/results?search_query={}'.format(keyword)
driver = webdriver.Chrome(executable_path='C:\Python27\chromedriver.exe')

# chromedriver를 본인의 크롬 버전에 맞춰 설치하고 설치한 경로를 path에 써주세요
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.close()

name = soup.select('a#video-title')
video_url = soup.select('a#video-title')
view = soup.select('a#video-title')

name_list = []
url_list = []
view_list = []

for i in range(len(name)):
    name_list.append(name[i].text.strip())
    view_list.append(view[i].get('aria-label').split()[-1])
for i in video_url:
    url_list.append('{}{}'.format('https://www.youtube.com',i.get('href')))
    
youtubeDic = {
    '제목': name_list,
    '주소': url_list,
    '조회수': view_list
}

youtubeDf = pd.DataFrame(youtubeDic)

print(name_list[0])
print(name_list[1])
print(name_list[2])
print('옵션 1,2,3 을 선택하세요')
o=input()
if(o=='1'):
    link=url_list[0]
elif(o=='2'):
    link=url_list[1]
elif(o=='3'):
    link=url_list[2] 
else:      #외에 것을 입력하면 최상단의 영상 다운
    link=url_list[0]
    
#link = input ("") # 또는 아래와 같이 직접 유튜브 동영상 주소를 파이썬 스크립트 파일에 복사


ydl=youtube_dl.YoutubeDL({})
with ydl:
    video=ydl.extract_info(link,download=False)
print('{}--{}--{}'.format(video['artist'],video['track'],video['album']))

a=video['track']



ydl_opts = {

    'format': 'bestaudio/best',

    'postprocessors': [{

        'key': 'FFmpegExtractAudio',

        'preferredcodec': 'mp3',

        'preferredquality': '320',

    }],
    'outtmpl':f"{os.getcwd()}/{a}.m4a" 
    #파이썬 문자열안에 변수를 대치시키는 방법 f 와 {} 이용
}




with youtube_dl.YoutubeDL(ydl_opts) as ydl:
   
    ydl.download([link])



audiofile = eyed3.load(f"{a}.mp3")
audiofile.initTag(version=(2,3,0))
audiofile.tag.artist = video['artist']
audiofile.tag.album = video['album']
audiofile.tag.title = video['track']
audiofile.tag.save()






"""
def get_song_info(link):
    response=requests.get(link)
    soup=BeautifulSoup(response.text,'lxml') #html 데이터 가져오기
    
    song_info['title']=soup.find('div',id='content')
    result=soup.find('div',id='content')
    print(result)
    
   # lis=soup.find_all("ytd-metadata-row-container-renderer","sticky.style-scope.ytd-video-secondary-info-renderer")

 for i in lis:
        global song_info
        song_info["title"]=i.find("div",id="content")
        print(i.find("div",id="content"))
"""
"""
ydl=youtube_dl.YoutubeDL({})
with ydl:
    video=ydl.extract_info(link,download=False)
print('{}--{}--{}'.format(video['artist'],video['track'],video['album']))
print(video['artist'])
print(video['track'])
print(video['album'])


"""