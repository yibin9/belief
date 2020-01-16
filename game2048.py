"""
    游戏2048核心算法
"""
list_merge = [2, 0, 0, 2]
map = [[2, 2, 8, 2],
       [4, 4, 0, 2],
       [4, 0, 8, 2],
       [0, 4, 2, 0],
       ]


# list_merge = [4, 4, 4, 4]


# 1. 定义函数，将零元素移动到末尾
# [2,0,0,2] --> [2,2,0,0]
# [0,2,0,2] --> [2,2,0,0]
# [0,0,0,2] --> [2,0,0,0]
def zero_to_end():
    # 思路：从后往前判断,如果是零元素则删除,再追加零元素.
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 测试：
# zero_to_end()
# print(list_merge)

# 2. 定义函数，将相同元素合并
# [4,4,2,2] --> [8,4,0,0]
# [2,0,0,2] --> [2,2,0,0] -->  [4,0,0,0]
# [2,2,2,2] --> [4,4,0,0]
# [0,0,0,2] --> [2,0,0,0]
def merge():
    # 思想：将相邻且相同元素进行合并
    zero_to_end()  # [2,0,0,2] --> [2,2,0,0]
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# merge()
# print(list_merge)
# 定义函数,将二维列表所有元素向左移动
# 思想：获取每行,赋值给list_merge,通过merge函数进行合并.
def move_left():
    global list_merge
    for item in map:
        list_merge = item
        merge()


# move_left()
# print(map)

# 定义函数,将二维列表所有元素向右移动
# 思想：获取每行反转后，赋值给list_merge,
#      通过merge函数进行合并.
#      list_merge还给map
def move_right():
    global list_merge
    for item in map:
        list_merge = item[::-1]
        merge()
        item[::-1] = list_merge


# move_left()
# print(map)
# 思想： 矩阵转置
def matrix_arrange():
    for c in range(1, len(map)):
        for r in range(c, len(map)):
            map[r][c - 1], map[c - 1][r] = map[c - 1][r], map[r][c - 1]


matrix_arrange()
print(map)


# matrix_arrange()
# print(map)
# 定义函数,将二维列表所有元素向上移动
# 思想： 矩阵转置
#       调用向左移动
#       矩阵转置
def move_up():
    matrix_arrange()
    move_left()
    matrix_arrange()


# 测试
# move_down()
# print(map)
# 定义函数,将二维列表所有元素向下移动
# 思想： 矩阵转置
#       调用向右移动
#       矩阵
def move_down():
    matrix_arrange()
    move_right()
    matrix_arrange()

# 测试
# move_down()
# print(map)
