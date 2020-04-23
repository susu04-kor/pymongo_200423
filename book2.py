import requests
import re


url = 'https://www.hanbit.co.kr/store/books/new_book_list.html'

#이미지이름을 도서명으로 저장해 봅니다.
text = requests.get(url).text
list = re.findall('<li class="sub_book_list">(.+?)</li>', text, re.DOTALL)

for book in list:
    img_url = re.findall('<img src="(.+?)" alt="" class="thumb" />', book)
    data = requests.get("https://www.hanbit.co.kr/"+img_url[0]).content
    bookname = re.findall('<p class="book_tit"><a href=".+?">(.+?)</a>', book)
    fname = bookname[0]+".jpg"
    f = open("bookImg/"+fname, "wb")
    f.write(data)
    f.close()
    print(bookname[0],"번째 그림을 다운 받았습니다.")
    
    # 한빛 출판사의 새로 나온 도서의
    # 도서명, 가격, 이미지를 수집하여
    # 웹서비스를 구현해 봅니다

