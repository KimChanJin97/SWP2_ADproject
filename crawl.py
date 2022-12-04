import os
import sys
import urllib.request
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Crawl:
    
    
    def __init__(self, word, maxImageNum=30):
        self.word = word
        self.maxImageNum = maxImageNum # 한 페이지에 출력되는 이미지수는 96개
        # print(type(self.word))
        # print(type(self.maxImageNum))


    def crawl_image(self, path):
        # 프로젝트에 미리 생성해놓은 crawled_img폴더 안에 하위 폴더 생성
        # 폴더명에는 입력한 키워드, 이미지 수 정보를 표시함

        # path = 'crawled_img/' + self.word + '_' + self.maxImageNum

        # try:
        #     # 중복되는 폴더 명이 없다면 생성
        #     if not os.path.exists(path):
        #         os.makedirs(path)
        #     # 중복된다면 문구 출력 후 프로그램 종료
        #     else:
        #         print('이전에 같은 [검색어, 이미지 수]로 다운로드한 폴더가 존재합니다.')
        #         sys.exit(0)
        # except OSError:
        #     print('os error')
        #     sys.exit(0)

        # flaticon 검색 후 1페이지 당 96개의 이미지 나옴

        # 만약 크롤링하고 싶은 이미지가 50개라면? 50 / 96 = 0
        # 49 / 96 + 1 = 0 + 1 = 1
        # 만약 크롤링하고 싶은 이미지가 96개라면? 96 / 96 = 1 (96개일 때 조심!)
        # 95 / 96 + 1 = 0 + 1 = 1
        # 만약 크롤링하고 싶은 이미지가 100개라면? 100 / 96 = 1
        # 99 / 96 + 1 = 1 + 1 = 2
        pages = ((int(self.maxImageNum) - 1) / 96) + 1  # 한 페이지당 표시되는 이미지 수(96)을 참고하여 확인할 페이지 수 계산
        imgCount = 0  # 추출 시도 이미지 수
        success = 0  # 추출 성공 이미지 수
        finish = False  # 이미지에 모두 접근했는지 여부

        # 크롬 드라이버 설정
        # ChromeDriverManager로 import한 ChromeDriverManager 객체 생성해서 webDriver.Chrome 매개변수로 런타임에 다운로드 받아서 사용
        options = webdriver.ChromeOptions()
        options.add_argument('headless') # 크롤링할 때 웹페이지 띄우지 않음
        options.add_argument('--disable-gpu') # gpu 사용하지 않음
        options.add_argument('lang=ko_KR') # 한글 지원
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36") # user-agent 헤더 추가


        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)

        for i in range(1, 2): # 원래 2 대신 int(pages) + 1
            # 첫 페이지의 경우 url이 조금 다름
            if i == 1:
                driver.get('https://www.flaticon.com/search?word=' + self.word + "&color=color")
                sleep(1) # 웹 페이지 접근 후 1초동안 로드를 기다림
            # 첫 페이지 이후의 경우 url은 다음과 같음
            else:
                driver.get('https://www.flaticon.com/search/' + str(i) + '?word=' + self.word + "&color=color")
                
            # 크롤링이 가능하도록 html코드 가공
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            imgs = soup.select('div.icon--holder img')  # 요소 선택
            
            # 마지막 페이지 여부 결정
            lastPage = False
            if len(imgs) != 96: # 한 페이지에 나타낼 수 있는 최대 이미지(96개)를 보여주고 있지 않다면
                lastPage = True # 이는 마지막 페이지임을 알 수 있다

            for img in imgs:
                srcset = ""
                if img.get('data-src') == None:
                    srcset = img.get('srcset') # lazy
                else:
                    srcset = img.get('data-src') # 기본
                
                src = ""
                if len(srcset): # lazy
                    src = str(srcset).split()[0]  # 이미지 경로 추출
                    print(src)
                    filename = src.split('/')[-1]  # 이미지 경로에서 맨 뒤 파일명만 추출
                    print(filename)
                    saveUrl = path + '\\' + filename  # 저장 경로 결정
                    print(saveUrl)

                    # 파일 저장
                    # user-agent 헤더를 가지고 있어야 접근 허용하는 사이트도 있을 수 있음
                    req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})
                    try:
                        imgUrl = urllib.request.urlopen(req).read()  # 웹 페이지 상의 이미지를 불러옴
                        with open(saveUrl, "wb") as f:  # 디렉토리 오픈
                            f.write(imgUrl)  # 파일 저장
                        success += 1
                    except urllib.error.HTTPError:
                        print('에러')
                        sys.exit(0)

                imgCount += 1

                if imgCount == int(self.maxImageNum):
                    finish = True  # 입력한 이미지 수 만큼 모두 접근했음을 알림
                    break

            # finish가 참이거나 더 이상 접근할 이미지가 없을 경우 크롤링 종료
            if finish or lastPage:
                break

        print('성공 : ' + str(success) + ', 실패 : ' + str(int(self.maxImageNum) - success))
        
        file_list = os.listdir(path) # 파일들을 리스트로
        path_file_list = []
        
        for i in file_list:
            path_file_list.append(path + "\\" + i)
        
        return path_file_list