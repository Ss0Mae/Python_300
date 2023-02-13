user=input("우편번호: ")
reg=user[:3]
if reg in["010","011","012"]:
    print("강북구")
elif reg in["014","015","016"]:
    print("도봉구")
else:
    print("노원구")