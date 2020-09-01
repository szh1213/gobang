import random
########使用时将棋盘列表和你要走的棋子作为参数
def ai(qipan, me):
    code = ""
    size = len(qipan)
    chess_color = 0
    xxx = 1
    yyy = 1
    # 保存棋盘
    chess = qipan
    # 保存棋盘权值
    #2是白1是黑
    chess_Value = [[0 for i in range(size)] for i in range(size)]
    if me == 2:
        dic = {"0": 0, "1": 8, "2": 10, "11": 50, "22": 1000, "111": 6000, "222": 3000, "1111": 5000, "2222": 20000,
               "21": 4, "12": 2, "211": 25, "122": 20, "11112": 3000, "112": 30, "1112": 2800, "221": 500, "2221": 2000,
               "22221": 10000}
    if me == 1:
        dic = {"0": 0, "2": 8, "1": 10, "22": 50, "11": 1000, "222": 6000, "111": 3000, "2222": 5000, "1111": 20000,
               "12": 4, "21": 2, "122": 25, "211": 20, "22221": 3000, "221": 30, "2221": 2800, "112": 500, "1112": 2000,
               "11112": 10000}
    for i in range(0, size):
        for j in range(0, size):
            if chess[i][j] == 0:
                code = ""
                chess_color = 0
                for x in range(i + 1, size):
                    # 如果向右的第一位置为空就跳出循环
                    if chess[x][j] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是右边第一颗棋子
                            code += str(chess[x][j])  # 记录它的颜色
                            chess_color = chess[x][j]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][j]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][j])  # 记录它的颜色
                            else:  # 右边找到一颗不同颜色的棋子
                                code += str(chess[x][j])
                                break
                # 取出对应的权值
                value = dic.get(code)
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
                # 向左
                for x in range(i - 1, 0, -1):
                    # 如果向左的第一位置为空就跳出循环
                    if chess[x][j] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是左边第一颗棋子
                            code += str(chess[x][j])  # 记录它的颜色
                            chess_color = chess[x][j]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][j]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][j])  # 记录它的颜色
                            else:  # 左边找到一颗不同颜色的棋子
                                code += str(chess[x][j])
                                break
                #  取出对应的权值
                value = dic.get(code)
                if value:
                    chess_Value[i][j] += value
                #  把code，chess_color清空
                code = ""
                chess_color = 0
                #  向上
                for y in range(j - 1, 0, -1):
                    #  如果向上的第一位置为空就跳出循环
                    if chess[i][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是上边第一颗棋子
                            code += str(chess[i][y])  # 记录它的颜色
                            chess_color = chess[i][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[i][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[i][y])  # 记录它的颜色
                            else:  # 上边找到一颗不同颜色的棋子
                                code += str(chess[i][y])
                                break
                #  取出对应的权值
                value = dic.get(code)
                if value:
                    chess_Value[i][j] += value
                #  把code，chess_color清空
                code = ""
                chess_color = 0
                # 向下
                for y in range(j + 1, size):
                    # 如果向下的第一位置为空就跳出循环
                    if chess[i][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是下边第一颗棋子
                            code += str(chess[i][y])  # 记录它的颜色
                            chess_color = chess[i][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[i][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[i][y])  # 记录它的颜色
                            else:  # 下边找到一颗不同颜色的棋子
                                code += str(chess[i][y])
                                break
                # 取出对应的权值
                value = dic.get(code)
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
                # 向左下
                for x, y in zip(range(i - 1, 0, -1), range(j + 1, size)):
                    # 如果向左下的第一位置为空就跳出循环
                    if chess[x][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是左下边第一颗棋子
                            code += str(chess[x][y])  # 记录它的颜色
                            chess_color = chess[x][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][y])  # 记录它的颜色
                            else:  # 左下找到一颗不同颜色的棋子
                                code += str(chess[x][y])
                                break
                # 取出对应的权值
                value = dic.get(code)
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
                # 向右上
                for x, y in zip(range(i + 1, size), range(j - 1, 0, -1)):
                    # 如果向右上的第一位置为空就跳出循环
                    if chess[x][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是右上边第一颗棋子
                            code += str(chess[x][y])  # 记录它的颜色
                            chess_color = chess[x][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][y])  # 记录它的颜色
                            else:  # 右上找到一颗不同颜色的棋子
                                code += str(chess[x][y])
                                break
                # 取出对应的权值
                value = dic.get(code)
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
                # 向左上
                for x, y in zip(range(i - 1, 0, -1), range(j - 1, 0, -1)):
                    # 如果向左上的第一位置为空就跳出循环
                    if chess[x][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是左
                            # 上边第一颗棋子
                            code += str(chess[x][y])  # 记录它的颜色
                            chess_color = chess[x][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][y])  # 记录它的颜色
                            else:  # 左上找到一颗不同颜色的棋子
                                code += str(chess[x][y])
                                break
                # 取出对应的权值
                value = dic.get(code)
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
                # 向右下
                for x, y in zip(range(i + 1, size), range(j + 1, size)):
                    # 如果向右下的第一位置为空就跳出循环
                    if chess[x][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是右下
                            # 上边第一颗棋子
                            code += str(chess[x][y])  # 记录它的颜色
                            chess_color = chess[x][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][y])  # 记录它的颜色
                            else:  # 右下找到一颗不同颜色的棋子
                                code += str(chess[x][y])
                                break
                # 取出对应的权值
                value = dic.get(code)
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
    mymax = 0
    for a in range(0, size):
        for b in range(0, size):
            if chess_Value[a][b] > mymax and chess[a][b] == 0:
                mymax = chess_Value[a][b]
                xxx = a
                yyy = b
    if mymax == 0:
        xxx, yyy = random.randint(1, len(qipan)-1),random.randint(1, len(qipan)-1)
    #chess[xxx][yyy] = me
    return xxx, yyy
