import sys
import urllib.request
import urllib3
import bs4
import re

baseUrl = "https://www.easy-youtube-mp3.com/download.php?"

url = sys.argv[1]

vPoint = re.search("v=",url)

print(url[vPoint.start():])


url = baseUrl + url[vPoint.start():]


print("開始します")
urllib3.disable_warnings()
http = urllib3.PoolManager()

try:
    res = http.request("GET",url)
except:
    print("url先が存在しません")


if res.status == 200:
    print("OK\n")
else:
    print("url先が読み込めませんでした")

soup = bs4.BeautifulSoup(res.data,"html.parser")

print(str(soup.title) + "\n")

a = soup.find_all("a",class_="btn btn-lg btn-success")

print(a[0].get("href"))

url = a[0].get("href")

savemane = "test.mp3"
urllib.request.urlretrieve(url,savemane)

print("保存しました")

"""
https://www.easy-youtube-mp3.com/download.php?v=GElbyAZBTCk
https://www.youtube.com/watch?v=kijnyfoRk4g
https://www.youtube.com/watch?v=FtutLA63Cp8
https://www.youtube.com/watch?v=GElbyAZBTCk
"""
