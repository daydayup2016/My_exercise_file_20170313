
# _*_ coding:utf-8 _*_

import urllib.request
def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html
	
html = getHtml("http://www.baidu.com")

print(html)