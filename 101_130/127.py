user=input("주민등록번호: ")
user=user.split("-")[1]
if(user[0]=='1' or user[0]=='3'):
    sex='남자'
else:
    sex='여자'
print(f"{sex}")