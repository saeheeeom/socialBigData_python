import requests

headerData = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

def getTitleClien(wantpage):
    titleList = []
    for pageNum in range(wantpage):
        pageNum = str(pageNum)
        urlStr = 'https://www.clien.net/service/board/sold?&od=T31&category=0&po='+pageNum

        resp = requests.get(urlStr, headers = headerData)
        htmlText = resp.text

        titleFirst = 'data-role="list-title-text" title="'
        titleLast = '">'
        titleLastIndex = 0

        while True:
            try:
                titleFirstIndex = htmlText.index(titleFirst, titleLastIndex) + len(titleFirst)
            except ValueError:
                break
            titleLastIndex = htmlText.index(titleLast, titleFirstIndex)
            titleStr = htmlText[titleFirstIndex:titleLastIndex]
            titleList.append(titleStr)
    return titleList

print(getTitleClien(1))
