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
    # 2是白1是黑
    if me == 1:
        enemy = 2
    elif me == 2:
        enemy = 1
    chess_Value = [[0 for i in range(size)] for i in range(size)]
    if me == 2:
        dic = {"0": 0, "1": 1, "2": 2, "11": 40, "22": 40, "111": 300, "222": 800, "1111": 10, "2222": 95,
               "21": 4, "12": 1, "211": 4, "122": 1, "11112": 1000, "112": 30, "1112": 70, "221": 30, "2221": 40,
               "22221": 50}
    if me == 1:
        dic = {"0": 0, "2": 1, "1": 2, "22": 40, "11": 40, "222": 300, "111": 80, "2222": 10, "1111": 95,
               "12": 4, "21": 1, "122": 4, "211": 1, "22221": 1000, "221": 30, "2221": 70, "112": 30, "1112": 40,
               "11112": 50}

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
                                if x == size - 1:
                                    if me == 1:
                                        code += str(2)
                                    elif me == 2:
                                        code += str(1)

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
                for x in range(i - 1, -1, -1):
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
                                if x == 0:
                                    if me == 1:
                                        code += str(2)
                                    elif me == 2:
                                        code += str(1)
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
                for y in range(j - 1, -1, -1):
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
                                if y == 0:
                                    if me == 1:
                                        code += str(2)
                                    elif me == 2:
                                        code += str(1)
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
                                if y == size - 1:
                                    if me == 1:
                                        code += str(2)
                                    elif me == 2:
                                        code += str(1)
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
                for x, y in zip(range(i - 1, -1, -1), range(j + 1, size)):
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
                                if x == 0 or y == size - 1:
                                    if me == 1:
                                        code += str(2)
                                    elif me == 2:
                                        code += str(1)
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
                for x, y in zip(range(i + 1, size), range(j - 1, -1, -1)):
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
                                if x == size - 1 or y == 0:
                                    if me == 1:
                                        code += str(2)
                                    elif me == 2:
                                        code += str(1)
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
                for x, y in zip(range(i - 1, -1, -1), range(j - 1, -1, -1)):
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
                                if x == 0 or y == 0:
                                    if me == 1:
                                        code += str(2)
                                    elif me == 2:
                                        code += str(1)
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
                                if x == size - 1 or y == size - 1:  # 如果下一个是墙
                                    if me == 1:
                                        code += str(2)
                                    elif me == 2:
                                        code += str(1)
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
                xxx= a
                yyy= b
    if mymax == 0:
        #xxx, yyy = int(len(qipan) / 2), int(len(qipan) / 2)
        xxx,yyy=random.randint(1, len(qipan)-1),random.randint(1, len(qipan)-1)
        chess[xxx][yyy] = me
        return xxx, yyy
    else:
        if mymax > 1000:
            chess[xxx][yyy] = me
            return xxx, yyy
        else:
            for i in range(len(qipan)):  # 横
                for j in range(1, len(qipan[0]) - 4):
                    if qipan[i][j] == \
                            qipan[i][j + 3] == enemy:
                        if qipan[i][j + 1] == enemy \
                                and qipan[i][j + 2] == 0:
                            return (i, j + 2)
                        if qipan[i][j + 2] == enemy \
                                and qipan[i][j + 1] == 0:
                            return (i, j + 1)
            for i in range(1, len(qipan) - 4):  # 竖
                for j in range(len(qipan[0])):
                    if qipan[i][j] == \
                            qipan[i + 3][j] == enemy:
                        if qipan[i + 1][j] == enemy \
                                and qipan[i + 2][j] == 0:
                            return (i + 2, j)
                        if qipan[i + 2][j] == enemy \
                                and qipan[i + 1][j] == 0:
                            return (i + 1, j)
            for i in range(1, len(qipan) - 4):  # 下斜
                for j in range(1, len(qipan[0]) - 4):
                    if qipan[i][j] == \
                            qipan[i + 3][j + 3] == enemy:
                        if qipan[i + 1][j + 1] == enemy \
                                and qipan[i + 2][j + 2] == 0:
                            return (i + 2, j + 2)
                        if qipan[i + 2][j + 2] == enemy \
                                and qipan[i + 1][j + 1] == 0:
                            return (i + 1, j + 1)
            for i in range(4, len(qipan) - 1):  # 上斜
                for j in range(1, len(qipan[0]) - 4):
                    if qipan[i][j] == \
                            qipan[i - 3][j + 3] == enemy:
                        if qipan[i - 1][j + 1] == enemy \
                                and qipan[i - 2][j + 2] == 0:
                            return (i - 2, j + 2)
                        if qipan[i - 2][j + 2] == enemy \
                                and qipan[i - 1][j + 1] == 0:
                            return (i - 1, j + 1)
            chess[xxx][yyy] = me
            return xxx, yyy





