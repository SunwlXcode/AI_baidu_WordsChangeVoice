# Write By Sunwl
# 2018/02/02
#
# 百度语音识别库
# 
# python 3.6.2
# 运行环境 Win10
# 注意：如果在 Mac 下运行，"d:/test.mp3" 要改成 "./test.mp3",并赋予权限


import requests
import os


# 构建 headers 
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

while 1:
	text = str(input("请输入语音的文字:"))
	a = requests.get("http://fanyi.baidu.com/gettts?lan=zh&text=" + text + "&spd=5&source=web",headers=headers)
	with open("d:/test.mp3","wb") as f :
		f.write(a.content)
	os.system("d:/test.mp3")

