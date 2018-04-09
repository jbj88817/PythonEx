# 旅行者 走路 每走一次算一步
# 走了3
# 再走了5
# 再走了 6

# x = 0
# 3 result = 3
# 5 result = 8
# 6 result = 14

# -------- 非闭包解法-------------
# origin = 0
#
#
# def go(step):
#     global origin
#     new_pos = origin + step
#     origin = new_pos
#     return origin
#
#
# print(go(3))
# print(go(5))
# print(go(6))

# -------- 闭包解法-------------


def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return go


t = factory(0)
print(t(3))
print(t(5))
print(t(6))
