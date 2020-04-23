# a = [10, 20, 30]
# b = ['사과', '포도', '딸기']
#
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# print(type(a[0]))
# print(type(b[0]))

list = [10, 20, 30, "사과"]
print(list)
# print(type(list))
# for data in list:
#     print(data)
#     print(type(data))

# for n in list:
#     try:
#         print(n+2)
#     except TypeError:
#         print("숫자가 아닙니다.")

for n in list:
    if str(type(n)) == "<class 'int'>":
        print(n+2)