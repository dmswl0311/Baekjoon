import sys

str = sys.stdin.readline()
print(str)
cnt = 0
cnt2 = 0
list = ["c=", "c-", "dz=", "d", "lj", "nj", "s=", "z="]
# s1 = str.replace("c=", "č").replace(
#     "c-", "ć").replace("dz=", "dž").replace("d", "đ").replace("lj", "lj").replace("nj", "nj").replace("s=", "š").replace("z=", "ž")

for i in list:
    if i in str:
        cnt = cnt+1

print(cnt)
