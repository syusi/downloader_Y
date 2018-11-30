import sys
import urllib.request


print("hello")

url = sys.argv[1]
savemane = "sa.mp3"


urllib.request.urlretrieve(url,savemane)

print("保存しました")

"""
https://www.easy-youtube-mp3.com/download.php?v=GElbyAZBTCk
https://www.youtube.com/watch?v=kijnyfoRk4g
https://www.youtube.com/watch?v=FtutLA63Cp8
https://www.youtube.com/watch?v=GElbyAZBTCk
"""
