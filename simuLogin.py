#encoding=utf-8
#模拟登陆，以知乎网为例
import urllib2
import urllib
import re
class SimuLogin:
	def __init__(self,url):
		self.url=url
	#爬取知乎首页的html源码
	def getPageHtml(self):
		user_agent="Mozilla /5.0 (Windows NT (6.1))"
		headers={"User-Agent":user_agent}
		request=urllib2.Request(self.url,headers=headers)
		html=urllib2.urlopen(request)
		print html #测试输出
		return html

#测试
url=raw_input("input a url:")
sLogin=SimuLogin(url)
sLogin.getPageHtml() 
#报错，仔细一看, 发现知乎网传给我们的是经过 gzip 压缩之后的数据. 
#这样我们就需要先对数据解压. Python 进行 gzip 解压很方便, 因为内置有库可以用. 
#如何解压缩，看下一个版本