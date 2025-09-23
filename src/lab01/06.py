n = int(input())
och = 0
zaoch = 0
for i in range(n):
    format = input().split()[-1]
    if format == "True":
        och += 1
    else:
        zaoch += 1
print(och, zaoch)