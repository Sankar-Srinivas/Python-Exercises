x=input('enter no of rows')
y=input('enter no of columns')

# n=User.split(",")
row_num=int(x)
col_num=int(y)
matrix=[[0 for j in range(col_num)] for i in range(row_num)]
for i in range(row_num):
    for j in range (col_num):
        matrix[i][j]=i*j

print(matrix)

# input_str = input('enter')
# dimensions = [int(x) for x in input_str.split(',')]
# row_num = dimensions[0]
# col_num = dimensions[1]
# multilist = [[0 for col in range(col_num)] for row in range(row_num)]
#
# for row in range(row_num):
#     for col in range(col_num):
#         multilist[row][col] = row * col
#
# print (multilist)