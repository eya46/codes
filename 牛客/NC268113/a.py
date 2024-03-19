# https://ac.nowcoder.com/acm/problem/268113

L, N = map(int, input().split())

SL, SR = input().strip().split("I")

for i in range(N):
    if input().strip() == "delete":
        SR = SR[1:]
    else:
        if SL and SR and SL[-1] == "(" and SR[0] == ")":
            SL = SL[:-1]
            SR = SR[1:]
        else:
            SL = SL[:-1]

print(f"{SL}I{SR}")
