from urllib import request


class Spider():
    url = 'https://www.panda.tv/cate/lol'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        return r.read()

    # def __analysis(self, htmls):

    def go(self):
        htmls = self.__fetch_content()


spider = Spider()
spider.go()
