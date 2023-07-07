import random

print("안녕 넌 나와 가위바위보를 하게 될거야.")
userPick = int(input("안 내면 진다 가위 바위 보!! : "))

pickList = ( "가위", "바위", "보" )

if userPick < 0 or userPick > 2:
    print("가위또는 바위또는 보 중에서 입력해주세요.")

computerPick = random.randint(0, 2)

print(computerPick)

print(f"컴퓨터가 낸 것은 {pickList[computerPick]}입니다.")

if (userPick + 1) % 3 <= computerPick:
    print("너가 졌다.")
elif userPick == computerPick:
    print("비겼다.")
else:
    print("너가 이겼다.")