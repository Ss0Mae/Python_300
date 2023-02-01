fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season=input()
if season in fruit.keys():
    print("Correct")
else:
    print("Wrong")