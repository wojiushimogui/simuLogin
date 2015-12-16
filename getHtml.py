#encoding=utf-8
import urllib2
import urllib
import cookielib
import re
import gzip
#解压gzip包
def ungzip(data):
	try:     #尝试解压
		print(u"解压中...")
		data=gzip.decompress(data)
		print(u"解压完成")
	except:
		print(u"未经压缩，无需解压")
	return data
header = {
	'Connection': 'Keep-Alive',
	'Accept': 'text/html, application/xhtml+xml, */*',
	'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Accept-Encoding': 'gzip, deflate',
	'Host': 'www.zhihu.com',
	'Dnt': '1'
}
#获取opener

def getopener(head):#接收一个head参数
	#第一步：得到一个cookie实例对象来保存Cookie内容
	cookie=cookielib.CookieJar()
	#第二步：利用urllib2库中的HTTPCookieProcessor得到一个cookie的处理器
	pro=urllib2.HTTPCookieProcessor(cookie)
	#第三步：得到ｏｐｅｎｅｒ
	opener=urllib2.build_opener(pro)
	header=[]
	for key,value in head.items():
		elem=(key,value)
		header.append(elem)
	opener.addheaders=header
	return opener
def getXSRF(data):
	#<input type="hidden" name="_xsrf" value="e9d826c0fa34d68b3320d10c60df8588">
	#<input type="hidden" name="_xsrf" value="e9d826c0fa34d68b3320d10c60df8588">
	pattern= re.compile(r'<input type="hidden" name="_xsrf" value="(.*?)"',re.S)
	strlist = re.findall(pattern,data)
	print u"xsrf:"+strlist[0] #测试输出
	return strlist[0]
# response=urllib2.urlopen("http://www.xingjiakmite.com")
url="http://www.zhihu.com/"
response=urllib2.urlopen(url)
#print response.read().decode("utf-8")
data=response.read()
_xsrf=getXSRF(data)  #得到_xsrf，之后就可以模拟登陆了
#模拟浏览器
opener=getopener(header)
url+="login/email"
id="xxxx@qq.com"
password="123456"
postDict={"_xsrf":_xsrf,
		"email":id,
		"password":password,
		"rememberme":"true"
		}
postData=urllib.urlencode(postDict).encode()
html=opener.open(url,postData)
print html.read()#到这里原以为就能够登陆成功，但是，还差一步，知乎现在有验证码，因此，还需要破解验证码之后才能登陆成功
print html.info().get("Content-Encoding")
#对数据进行解压
data=ungzip(html.read().decode())
print data