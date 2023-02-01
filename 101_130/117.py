fruit = ["사과", "포도", "홍시"]
str=input()
if(str==fruit[0] or str==fruit[1] or str==fruit[2]):
    print("정답입니다")

if str in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")