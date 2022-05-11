from asyncio.windows_events import NULL
from pandas import notnull
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

class download_mp3():

    def extractInfo(self,lin):
        ydl=youtube_dl.YoutubeDL({}) # 주어진옵션에 따라 파일 다운로더 객체 생성 (YoutubeDL 객체 생성)


        with ydl:
            global video
            video=ydl.extract_info(lin,download=False)  # 해당 링크에서 정보를 추출하여 video에 저장 (download=False로 다시 음원이 다운되는 것을 방지함)

        # if(video['track'] == NULL):
        #     print('{}'.format(video['artist'])) # video 객체에 저장된 노래의 정보 중, 가수, 제목, 앨범명을 순서대로 출력
        
        if 'track' in video :
            a = video['track'] 
        else:
            a = input("youtube에서 해당 노래에 저장된 track 정보가 없습니다. 노래의 이름을 직접 입력해주세요!   ")


        
        return a

            



# 옵션 지정
    def setOpition(self,a):
        global ydl_opts
        ydl_opts = {

            'format': 'bestaudio/best',   # 최고음질 오디오

            'postprocessors': [{       # 후처리 프로세서 : 후처리적인 계산이나 편집, 교환을 행함

                'key': 'FFmpegExtractAudio',   # 키 : FFmpeg를 사용

                'preferredcodec': 'mp3',      # .mp3 형태로 변환
                

                'preferredquality': '320',   # 품질 : 320k

            }],
            
            'outtmpl':f"{os.getcwd()}/{a}.m4a"   #파이썬 문자열안에 변수를 대치시키는 방법 f 와 {} 이용

        # YOUTUBE에서 검색한 영상을 .m4a(영상) 파일을 다운로드 하고 .mp3(오디오) 파일로 변환
        }

    def download(self,a,lin):

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        
            ydl.download([lin])    # YOUTUBE에서 검색한 결과의 주소를 통해 youtube-dl을 이용하여 다운로드

        audiofile = eyed3.load(f"{a}.mp3")      # 다운로드 완료한 .mp3 파일을 불러옴
        audiofile.initTag(version=(2,3,0))      # eyed3의 버전

        return audiofile
        

    
    def tags(self, audiofile):
        if 'artist' in video :
            audiofile.tag.artist = video['artist']  # eyed3를 사용하여 .mp3 파일의 artist 속성 추가 
        else:
            Artist = input("등록된 가수 정보가 없습니다. artist 직접 입력: ")
            audiofile.tag.artist = Artist


        if 'album' in video :
            audiofile.tag.album = video['album']    # eyed3를 사용하여 .mp3 파일의 album 속성 추가 

        else:
            Album = input("등록된 앨범 정보가 없습니다. album 직접 입력: ")
            audiofile.tag.album = Album

        if 'title' in video :
            audiofile.tag.title = video['title']    # eyed3를 사용하여 .mp3 파일의 track 속성 추가 
        else:
            Title = input("등록된 제목 정보가 없습니다. title 직접 입력: ")
            audiofile.tag.title = Title
            
        audiofile.tag.save()                    # 추가된 속성 tag 저장

