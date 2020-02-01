from urllib import request
import re

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Spider():
  url = 'https://www.huya.com/g/lol'
  root_pattern = '<li class="game-live-item" gid="1">([\s\S]*?)</li>'
  name_pattern = '<i class="nick" title=".*">(.*)</i>'
  number_pattern = '<i class="js-num">(.*)</i>'

  def __fetch_content(self):
    r = request.urlopen(self.url)
    htmls = str(r.read(), encoding= 'utf-8')
    return htmls
  
  def __analysis(self, htmls):
    root_html = re.findall(self.root_pattern, htmls)
    anchors = []
    
    for html in root_html:
      name = re.findall(self.name_pattern, html)
      number = re.findall(self.number_pattern, html)
      anchor = {'name': name, 'number': number}
      anchors.append(anchor)
    
    return anchors

  def __refine(self, anchors):
    l = lambda anchor: {'name': anchor['name'][0], 'number': anchor['number'][0]}

    return list(map(l, anchors))

  def __sort(self, anchors):
    return sorted(anchors, key = self.__sort_seed, reverse= True)

  def __sort_seed(self, anchor):
      number = float(anchor['number'][:-1])
      number *= 10000
      return number

  def go(self):
    htmls = self.__fetch_content()
    anchors = self.__analysis(htmls)
      
    _anchors = self.__refine(anchors)

    _anchors = self.__sort(_anchors)

    print(_anchors)

spider = Spider()

spider.go()