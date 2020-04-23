import requests
import re

#한빛도서의 새로운 책 이미지를 모두 저장해 봅니다
#이미지 이름을 도서명으로 저장해 봅니다
url="https://www.hanbit.co.kr/store/books/new_book_list.html"
text= requests.get(url).text
# print(text)

# img = re.findall('<img src="/images/common/(.+?)" alt="상세보기" />',text)[0]
#
# f=open("books.jpg", "wb")
# f.write(img)
# f.close()
# print("이미지를 모두 다운받았습니다.")


list = re.findall('<li class="sub_book_list">(.+?)</li>', text, re.DOTALL)
n=1
for book in list:
    img_url = re.findall('<img src="(.+?)" alt="" class="thumb" />', book)
    data = requests.get("https://www.hanbit.co.kr/"+img_url[0]).content
    fname = "book" +str(n)+ ".jpg"
    f=open("bookImg/"+fname, "wb")
    f.write(data)
    f.close()
    n=n+1
    print(n,"번째 그림을 다운 받았습니다.")