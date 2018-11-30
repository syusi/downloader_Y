import sys
import urllib.request
import urllib3



print("開始します")
urllib3.disable_warnings()
http = urllib3.PoolManager()

url = sys.argv[1]
try:
    res = http.request("GET",url)
except:
    print("url先が存在しません")


if res.status == 200:
    print(res.data)
else:
    print("url先が読み込めませんでした")




#savemane = "sa.mp3"



#urllib.request.urlretrieve(url,savemane)

#print("保存しました")

"""
https://www.easy-youtube-mp3.com/download.php?v=GElbyAZBTCk
https://www.youtube.com/watch?v=kijnyfoRk4g
https://www.youtube.com/watch?v=FtutLA63Cp8
https://www.youtube.com/watch?v=GElbyAZBTCk
"""
