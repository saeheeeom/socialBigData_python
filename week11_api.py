# week11
# what is an API? 데이터를 일일이 크롤링하는 대신, 조금 더 편하게 데이터를
# 정돈된 형태로 받을 수 있게 해주는 서비스.

# 이러한 API로 받는 데이터는 XML 또는 JSON의 형식을 따를 수 있음.
# JSON의 경우 파이썬의 리스트와 딕셔너리를 합쳐놓은 형태
# XML의 경우 html과 비슷한 형태로 자료가 이루어짐
# XML은 파이썬에서 기본적으로 parser를 제공함


import requests
import json # python standard library

jsonTestURL = 'https://jsonplaceholder.typicode.com/users'

resp = requests.get(jsonTestURL)
jsonStr = resp.text

x = json.loads(jsonStr)

print(x)


# 1단계: 트위터가 제공하는 API
# 2단계: Tweepy가 제공하는 API

# 데이터를 끌어오는 과정에서 인증 등을 대신 해주는 api가 있음
# 트위터의 경우 Tweepy가 이에 해당됨.
# def getData(): 한 뒤, X = Twitter로 데이터 요청, 받아온 X를 딕셔너리 또는
# 리스트 구조로 정리, return X -> 이 과정을 Tweepy가 해줌.
# 우리는 그냥 import한 뒤 getData()만 사용하면 됨.

import tweepy
# 1단계 tweeter 계정 만들고, app만들기 (앱 개발자 권한으로 키, 시크릿을 얻을 수 있는것임)
# 그리고 다른 사람에게 인증을 위한 url을 줄 수 있는 권한을 얻음
# 그래서 tweepy을 통해서 그 url을 계속 얻을 수 있는 것임
# 3단계 Oauth 인증을 통해 Access Token 얻기
# 4단계 API 사용해서 데이터 얻기
# tweeTest.py에서 계속


