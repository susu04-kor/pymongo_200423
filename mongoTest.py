from pymongo import MongoClient
#pymongo로부터 몽고클라이언트를 import해줘

#몽고클라이언트에 access하는 방법
client = MongoClient("localhost", 27017)
db = client['bit']
#컬렉션 설정하기 (goods = 컬렉션 이름)
goods = db['goods']

#insert하기
#먼저 다큐먼트 만들기(딕셔너리 형태로)
# g = {"no":1, "item":"나이키공", "qty":10, "price":25000, "fname":"ball1.jpg", "detail":"좋은 공입니다."}
#
# list = [
#     {"no":2, "item":"나이키 유니폼", "qty":10, "price":65000, "fname":"cloth1.jpg", "detail":"좋은 유니폼입니다."},
#     {"no":3, "item":"나이키 축구화", "qty":10, "price":85000, "fname":"shoe1.jpg", "detail":"좋은 축구화입니다."},
#     {"no":4, "item":"나이키 타이즈", "qty":10, "price":80000, "fname":"stock1.jpg", "detail":"좋은 타이즈입니다."}
# ]
# #insert한 id를 넘겨줌 - 실행하면 mongodb에 데이터가 들어감
# # _id = goods.insert_one(g).inserted_id
#
# _ids = goods.insert_many(list).inserted_ids
# print(_ids)

#모든 상품 목록을 출력해 봅니다

list = goods.find()
print(type(list))
arr = []
for g in list:
    arr.append(g)
    # print(g)
    # print(type(g))
print(arr)




