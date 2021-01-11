num_list = list(map(int, input().split()))
ori_list = [1, 2, 3, 4, 5, 6, 7, 8]

if num_list == ori_list:
    print("ascending")
elif num_list == sorted(ori_list, reverse=True):
    print("descending")
else:
    print("mixed")
