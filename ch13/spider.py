from urllib import request
import re


class Spider:
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    @staticmethod
    def __fetch_content():
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    @staticmethod
    def __analysis(htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    @staticmethod
    def __refine(anchors):
        l = lambda anchor: {'name': anchor['name'][0].strip(),
                            'number': anchor['number'][0]
                            }
        return map(l, anchors)

    def __sort(self, anchors):
        return sorted(anchors, key=self.__sort_seed, reverse=True)

    @staticmethod
    def __sort_seed(anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    @staticmethod
    def __show(anchors):
        for rank in range(0, len(anchors)):
            print('rank  ' + str(rank + 1)
                  + '  :  ' + anchors[rank]['name']
                  + '   ' + anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
