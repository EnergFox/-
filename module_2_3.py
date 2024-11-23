my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
while len(my_list) > num:
    if my_list[num] == 0: # или же поменять == на <=
        num += 1
        continue
    elif my_list[num] < 0:
        break
    print(my_list[num])
    num += 1
print(end='\n')

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
for num1 in my_list:
    if num1 > 0:
        print(num1, end='\n')