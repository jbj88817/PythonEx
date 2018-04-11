# len 和 bool 能影响 class bool取值


class Test:
    # pass
    def __len__(self):
        print('len called')
        return 0  # 有了这个0就返回 False

    def __bool__(self):
        print('bool called')
        return False  # 有了这个bool函数，len就不能控制返回了


test = Test()

print(len(test))
print(bool(None))
print(bool([]))
print(bool(test))
