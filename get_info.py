from __future__ import unicode_literals
from typing import Type
from unicodedata import name 
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

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(r"C:\Users\study\Documents\secondGrade\codeLION\youtube_api\be-hackathon-Lilion\chromedriver.exe")



class getVideo():

    global name, video_url, length

    def getURL(self,urls):
        driver.get(urls)
        global soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.close()
        

    def getINFO(self):
        name_list = []
        url_list = []

        name = soup.select('a#video-title')
        video_url = soup.select('a#video-title')

        length = len(name)
        
        for i in range(length):
            name_list.append(name[i].text.strip())
        for i in video_url:
            url_list.append('{}{}'.format('https://www.youtube.com',i.get('href')))
            
        youtubeDic = {
            '제목': name_list,
            '주소': url_list,
        }

        return name_list, url_list

    def selection(self, urls):           
        print('옵션 1,2,3 을 선택하세요')
        o=input()
        if(o=='1'):
            link=urls[0]
        elif(o=='2'):
            link=urls[1]
        elif(o=='3'):
            link=urls[2] 
        else:      #외에 것을 입력하면 최상단의 영상 다운
            link=urls[0]
        return link


