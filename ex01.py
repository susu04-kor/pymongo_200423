a=[10, 20, 30]
try:
    print(a[0])
    print(a[5])
except IndexError:
    print("인덱스 범위를 넘었어요")
except:
    print("예외발생")
finally:
    print("반드시 만나는 문장입니다.")