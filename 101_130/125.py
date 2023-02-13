user=input("휴대전화 번호 입력: ")
first=user.split('-')[0]
if first=="011":
    com="SKT"
elif first=="016":
    com="KT"
elif first=="019":
    com="LGU"
else:
    com="알수없음"
print(f"당신은 {com} 사용자 입니다.")
    