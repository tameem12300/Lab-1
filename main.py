#comment
#hello

BLACK = '\u001b[30m'
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range(5):
    if i % 2 == 0:
        print(f'{WHITE}{"  " * (12)}{END}')
    elif i == 1:
        print(f'{BLACK}{" " * (11)}{WHITE}{"  " * (1)}{RED}{"  " * (0)}{END}')
    elif i != 1:
        print(
            f'{BLACK}{"  " * (2)}{END}'
            f'{WHITE}{"  " * (1)}{END}'
            f'{BLACK}{"  " * (6)}{END}'
            f'{WHITE}{"  " * (1)}{END}'
            f'{BLACK}{"  " * (2)}{END}'
        )
    


# for i in range(6):
#     if i < 3:
#         print(f'{WHITE}{"  " * (14)}{END}')
#     else:
#         print(f'{RED}{"  " * (14)}{END}')


# plot_list = [[0 for i in range(10)] for i in range(10)]
# result = [0 for i in range(10)]

# for i in range(10):
#     result[i] = i**0.5

# step = round(abs(result[0] - result[9]) / 9, 2)
# print(step)

# for i in range(10):
#     for j in range(10):
#         if j == 0:
#             plot_list[i][j] = round(step * (8-i) + step ,2)

# for i in range(9):
#     for j in range(10):
#         if abs(plot_list[i][0] - result[9 - j]) < step:
#             for k in range(9):
#                 if 8 - k == j:
#                     plot_list[i][k+1] = 1

# for i in range(10):
#     print(plot_list[i])
    

# file = open('sequence.txt', 'r')
# list = []
# for number in file:
#     list.append(float(number))
# file.close()
# first1 = []
# second2 = []
# for number in list:
#     if len(first1) < 125:
#         first1.append(float(number))
#     else:
#         second2.append(float(number))
# result1,result2 = sum(first1)/125,sum(second2)/125
# print(result1,result2)

