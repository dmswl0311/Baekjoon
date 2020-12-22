import sys

str = sys.stdin.readline()

s1 = str.replace("c=", "č").replace(
    "c-", "ć").replace("dz=", "dž").replace("d", "đ").replace("lj", "lj").replace("nj", "nj").replace("s=", "š").replace("z=", "ž")

for i in len(str):
    if str.find("c=") != =-1:
        cnt += 1
