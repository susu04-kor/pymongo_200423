import requests
import re

url = "https://comic.naver.com/webtoon/weekday.nhn"
def getData():
    text = requests.get(url).text
    list = re.findall('<div class="col_inner">(.+?)</ul>', text, re.DOTALL)
    for line in list:
        li = re.findall("<li>(.+?)</li>", line, re.DOTALL)
        for data in li:
            a = re.findall('src="(.+?)".+? title="(.+?)"', data, re.DOTALL)
            img_url, title = a[0]
            content = requests.get(img_url).content
            f = open('img/'+title+".jpg", "wb")
            f.write(content)
            f.close()
            print(title + "저장됨")
            # print(img_url, title)
    print("모두 저장하였습니다.")
# print(len(list))
# print(text)