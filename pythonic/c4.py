# 迭代器

# for in iterable iterator


class BookCollection:
    def __init__(self):
        self.data = ['book1', 'booktu', 'booksui']
        self.cur = 0
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r


books = BookCollection()
# for book in books:
#     print(book)
print(next(books))
print(next(books))
print(next(books))  # 遍历完，不能再接着遍历，除非copy或者再实例化一个新的对象

# import copy
#
# books_copy = copy.copy(books)
# for book in books_copy:
#     print(book)
