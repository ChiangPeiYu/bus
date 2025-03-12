import urllib.request

url = "https://www.microsoft.com/zh-tw/"

print('第一種方法')
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))
