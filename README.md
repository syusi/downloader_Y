Youtube Music Downloder
--------
# 注意事項
あくまで適当に作ったので、自己責任でお願いします。

# 概要
youtubeのリンクとアーティスト、曲名をcsv形式で投げ込むと、mp3(320kbps)でダウンロードしてくれるもの。

## 動作環境
手元では以下の通り
- windows7
- python3.7
    - urllib3
    - beautifulsoup4

## 使い方
1. 適当にこのリポジトリを落とす
2. pythonをインストールする
3. パッケージをpipでインストールする
    - urllib3
    - beautifulsoup4
4. python test.py [CSVのファイル指定] で実行

### CSVフォーマット
アーティスト,曲名,youtubeのリンク

### ライセンス
- 変換をお願いしているサイト(大丈夫かどうか不明)
    - https://www.easy-youtube-mp3.com
- python3
