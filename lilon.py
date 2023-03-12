from __future__ import unicode_literals 
#파이썬 3에서 쓰던 문법을 파이썬2에서 쓸수있게 해줌
#from 모듈 import 이름 (from 파일명(라이브러리) import 함수이름)

from selenium import webdriver  #selenuim패키지에서 webdriver
#유튜브는 동적페이지 라서 사용자의 행동에 따라 서버에서 정보가 바뀜
#따라서 selenium 을 사용해야함
from selenium.webdriver.common.keys import Keys
import time



from bs4 import BeautifulSoup
#bs4 라이브러리에서 Beautifulsoup 사용 선언
import lxml
import requests 

import youtube_dl

import os
import eyed3

import get_info
import Download



#headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

print("Insert the keyword")


keyword=input("")

url=f'https://www.youtube.com/results?search_query={keyword}'


sth = get_info.getVideo() #get_info.py의 getVideo클래스
sth.getURL(url)  #입력받은 키워드가 들어간 url을 getURL함수에 넘김
names, urls = sth.getINFO() #names리스트랑 url리스트 반환


print(names[0])
print(names[1])
print(names[2])

link = sth.selection(urls)


sth2 = Download.download_mp3() #Download.py의 do~mp3클래스
A = sth2.extractInfo(link) #extractInfo에 링크 넣으면 title(제목)이 반환 A=제목
sth2.setOpition(A)  #다운받을때 파일이름이 제목으로 설정되게끔 옵션설정
audio = sth2.download(A,link) #다운로드 하고 eyeD3 load해서 반환
sth2.tags(audio)  #load한 ID3 정보들을 수정

