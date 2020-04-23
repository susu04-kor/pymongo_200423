import requests
import re

#이미지 링크
url="https://www.hanbit.co.kr/data/books/B8977162495_l.jpg"

#이미지 저장하기
data = requests.get(url).content
f = open("book.jpg", "wb")
f.write(data)
f.close()
print("이미지를 다운받았습니다.")