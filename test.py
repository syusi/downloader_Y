import sys
import csv
import urllib.request
import urllib3
import bs4
import re
import os

baseUrl = "https://www.easy-youtube-mp3.com/download.php?"
defaultDir = "./music"
def getDirpath(name):
    dirpath = defaultDir + "/" + name + "/"
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)
    return dirpath

filename = sys.argv[1]

#init
urllib3.disable_warnings()
http = urllib3.PoolManager()
if not os.path.isdir(defaultDir):
    os.makedirs(defaultDir)

csv_file = open(filename,"r",encoding="utf-8")

reader = csv.reader(csv_file)
for row in reader:
    dirname = row[0]
    savemane = row[1]
    youtubeUrl = row[2]
    vPoint = re.search("v=",youtubeUrl)
    #print(url[vPoint.start():])

    url = baseUrl + youtubeUrl[vPoint.start():]


    print("開始します")
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    try:
        res = http.request("GET",url)
    except:
        print("url先が存在しません")
        continue


    if res.status == 200:
        print("OK\n")
    else:
        print("url先が読み込めませんでした")
        continue

    soup = bs4.BeautifulSoup(res.data,"html.parser")

    print(str(soup.title) + "\n")

    a = soup.find_all("a",class_="btn btn-lg btn-success")

    ##print(a[0].get("href"))

    url = a[0].get("href")
    path = getDirpath(dirname)
    urllib.request.urlretrieve(url,path + savemane+".mp3")

    print("保存しました")

print("全て終了しました")