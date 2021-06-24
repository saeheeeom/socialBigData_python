import tweepy
from netminerClientPy import _NM

app_api_key = "57D1EUdoiDrTKo5nNLRYQ"
app_api_secret = "cpJzglxNHkbFX6gRKCBFVV8iey6gKzbUdqjE9xo"

auth = tweepy.OAuthHandler(app_api_key, app_api_secret)

user_key = "1392218463192580096-6reBERIJGIYuBKWvPpQ2IiuxWExStn"
user_secret = "PSGOpvetF7nyT4l63OrspgdY3Reil5NygaLsGIG3BnZpf"

auth.set_access_token(user_key, user_secret)

api = tweepy.API(auth)

def getData(searchStr, num):
    mainNodeList = []
    rtLinkList = []
    mainNodeSet = set([])
    tweetNum = 0
    countDict = {} # 네트워크 나타낼 딕셔너리. 하나의 RT관계(key)가 몇 번 이루어졌는지(value) 센다.
    for tweetObj in tweepy.Cursor(api.search, q=searchStr, count=100).items():
        try:
            seedTweetObj = tweetObj.retweeted_status # 현재 글이 rt여야만 함
        except:
            continue

        tweetNum += 1
        if tweetNum >= num: # 수집하려는 개수 제한
            break
        rtAuthor = tweetObj.author.screen_name
        seedAuthor = seedTweetObj.author.screen_name
        link = (rtAuthor, seedAuthor)
        if link in countDict:
            countDict[link] += 1
        else:
            countDict[link] = 1
        # 이렇게 만든 딕셔너리 형태의 정보를, netMiner에서 받을 수 있도록 형태 변화시켜야 함
    for link in countDict:
        weight = countDict[link]
        src = link[0]
        tgt = link[1]
        mainNodeSet.add(src)
        mainNodeSet.add(tgt)
        rtLinkList.append([src, tgt, weight])
    mainNodeList = list(mainNodeSet)
    return mainNodeList, rtLinkList

topicList = ["주식","AI", "코로나", "영화", "범죄", "축구", "육아", "건강", "종교"]

list1 = ["주식", "전환사채", "밈주식", "투자", "밈투자", "주식 거래", "개미", "산업은행", "산은", "투자 규모"] #300번
list2 = ["인공지능", "AI 콜센터", "유플러스 AI", "AI 솔루션", "AI금융", "AI교육"] # AI->인공지능으로 수정, 500번
list3 = ["코로나", "백신", "접종", "확진"] # 700번
list4 = ["영화", "마블", "개봉", "영화 방송", "극장", "유료방송", "영화업계"] # 500번
list5 = ["범죄", "범죄예방", "여성 범죄", "성범죄", "디지털성범죄", "피해자", "경찰서"] # 500번
list6 = ["축구", "에릭센", "권창훈", "축구산업", "수원삼성", "최종예선", "이동준", "김학범", "이강인", "축구감독", "정우영", "가나축구", "한국축구"] # 300번
list7 = ["육아", "육아지원", "공동육아", "육아 아빠", "육아 부모", "육아 정읍시", "육아 나눔터", "육아고민"] # 500번
list8 = ["건강식품", "건강기능", "대웅제약", "제약", "건강 생활", "정신건강", "건강관리", "검진", "보험"] # 건강 제외, 500번
list9 = ["종교 자유", "종교시설", "종교 침해", "채플", "인권위", "종교 강요", "종교 방역"] # 종교 제외, 500번
listofList = [list1, list2, list3, list4, list5, list6, list7, list8, list9]

def makeRtNetwork(searchStr, num):
    mainNodeList , linkList = getData(searchStr, num)
    _NM.Dataset.addMainNodeList(mainNodeList)
    _NM.Dataset.create1modeNetwork('rtNetwork', False, False)
    _NM.Dataset.add1modeLinkList('rtNetwork', linkList)

# workfile tree는 토픽별로, 세는 것 하나의 워크파일 안에서 수행
# 반복문으로 작성한 것을 tweepy의 개수제한으로 일일이 수행
for i in len(topicList):
    _NM.Workfile.createNewWorkfile(topicList[i]+"rtData", 'User', False)
    for word in listofList[i]:
        makeRtNetwork(word, 500)
