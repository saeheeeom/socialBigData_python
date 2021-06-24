from typing import List
import requests
from selenium.webdriver.remote.webelement import WebElement
from netminerClientPy import _NLP
from netminerClientPy import _NM
import tweepy


headerData = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
from selenium import webdriver # 셀레니움은 웹브라우저 기반 데이터 수집
from selenium.webdriver import ActionChains

c_driver = webdriver.Chrome() # 웹 브라우저 객체. 하나의 웹브라우저가 열림
c_driver.implicitly_wait(5)
topicList = ["주식","AI", "코로나", "영화", "범죄", "축구", "육아", "건강", "종교"]
for topic in topicList:
    searchUrl = "https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q="+topic+"&p="
    titList = []
    for i in range(20):
        c_driver.get(searchUrl + str(i + 1))
        titElementList = c_driver.find_elements_by_class_name("f_link_b")
        for j in range(10):
            titList.append(titElementList[j].text)
    _NM.Workfile.createNewWorkfile(topic,'MainNodeSet', False)

    textProc = _NLP.MorphKR.textProcessor(titList) # Document의 list를 인자로 받음
    result = textProc.run()
    wordResult = result.getWordResult()
    wordList = []
    for wordObj in wordResult:
        word = wordObj.getWord()
        freq = wordObj.getFrequency()
        tag = wordObj.getPOSTag()
        if freq >= 15 :
            wordList.append([word, freq, tag])
    def returnFreq(list):
        return list[1]
    wordList.sort(key=returnFreq, reverse=True)
    print(wordList)
    wordfreqFile=open("wordfreqlist.txt",'a')
    wordfreqFile.write(str(wordList)+",")
    wordfreqFile.close()
