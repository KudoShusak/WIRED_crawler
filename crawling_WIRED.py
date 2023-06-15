import re
import requests
import time
import os
from datetime import datetime
import json
from bs4 import BeautifulSoup
import urllib.robotparser


# クロールするサイト
start_url = "https://wired.jp"

# robots.txt
robots = "robots.txt"

# データ取得前に待つ時間
sleeptime = 0.5

# ループ回数
loop = 1024

# クロールしてもテキスト抽出しないサイトのリスト
# 'https://wired.jp/business/'など、カテゴリーページは、
# 'https://wired.jp/[a-z\-]+?/$'で引っかけてはじく
noscraping_list = [
    'https://wired.jp',
    'https://wired.jp/',
    'https://wired.jp/membership/about/',
    'https://wired.jp/membership/myaccount/',
    'https://wired.jp/membership/terms-and-conditions'
]

prefix = '{:%Y%m%d_%H%M%S}_'.format(datetime.now())

# クローリング結果保存ファイル
result_file = f"{prefix}wired_cwlLog.jsonl"

# テキストデータ保存ファイル
text_file = f"{prefix}wired.jsonl"

# 取得したhtmlのリストを保存するファイル
logfile = f"{prefix}wired_html_list.jsonl"

# htmlファイルの名前
sub_filename = "_wired_article.html"

# htmlファイルを保存するディレクトリ（フォルダ）
directory = f'{prefix}html'
os.mkdir(directory)

# ログファイル
log = f'{prefix}operation.log'

#### テキスト抽出 ####
def gettext(soup) :

    bodyhtmllist = []
    bodytxtlist = []

    ### タイトルの抽出 ###
    title = soup.find('h1')
    bodyhtmllist.append(str(title))
    bodytxtlist.append(title.text)

    ### タイトル下イントロの抽出 ###
    # 一般的な記事
    intro = soup.find('div', class_='ContentHeaderDek-bIqFFZ eudPTt')
    if intro != None :
        bodyhtmllist.append(str(intro))
        bodytxtlist.append(intro.text)

    # 特集記事
    intro = soup.find('div', class_='article__intro')
    if intro != None :
        bodyhtmllist.append(str(intro))
        bodytxtlist.append(intro.text)

    # 特集記事
    intro = soup.find('div', class_='BaseText-ewhhUZ')
    if intro != None :
        bodyhtmllist.append(str(intro))
        bodytxtlist.append(intro.text)

    # 特集記事
    intro = soup.find('p', class_='td__text')
    if intro != None :
        bodyhtmllist.append(str(intro))
        bodytxtlist.append(intro.text)

    # figcaptionタグの中身を全部削除
    for figcaption in soup.find_all('figcaption') :
        figcaption.decompose()

    ### 本文の抽出 ###
    # 一般的な記事
    for article in soup.find_all('div', class_='body__inner-container') :
        # 記事中のdivタグ（広告等）を削除
        for div in article.find_all('div') :
            div.decompose()
        # テキスト抽出
        for p_tag in article.find_all(['p','h2','h3','h4']) :
            # 本文中にbrタグがあった場合は改行に変換
            paragraph = str(p_tag).replace('<br/>', '\n')
            paragraph_html = BeautifulSoup(paragraph, "html.parser")
            bodyhtmllist.append(str(paragraph_html))
            bodytxtlist.append(paragraph_html.text)

    # 特集記事
    body = soup.find('div', class_='article-body')
    if body != None :
        for article in body.find_all(['p','h2','h3','h4']) :
            bodyhtmllist.append(str(article))
            bodytxtlist.append(article.text)

    # Wired Japanese Edition
    body = soup.find('div', class_='BodyWrapper-kufPGa gbtryP body')
    if body != None :
        for paragraph in body.find_all('p') :
            bodyhtmllist.append(str(paragraph))
            bodytxtlist.append(paragraph.text)

    return [bodyhtmllist, bodytxtlist]


#### JSONL形式で保存 ####

# save_dataをJSON形式でresult_fileに追記する。
def save_result(cont_txt, url="None", filename=result_file):

    save_data = {"url":url, "contents": [str(cont_txt[0]), cont_txt[1]]}

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(save_data, ensure_ascii=False) + '\n')
    f.close()

    return

# テキストデータのlistを指定の形式でtext_fileに追記する
def save_text(textlist, url="None", filename=text_file):

    jointxt = '\n'.join(textlist)
    save_data = {"url" : url, "text" : jointxt}

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(save_data, ensure_ascii=False) + '\n')
    f.close()

    return


#### アクセスログに記録 ####
def savelog(url:str, fileneme='operation.log', error=False) :
    now = '{:%Y.%m.%d %H:%M:%S}'.format(datetime.now())

    flg = 'Access'
    if error == True :
        flg = 'Error'

    message = {'time': now, flg: url}
    with open(fileneme, 'a', encoding='utf-8') as f:
        f.write(json.dumps(message)+'\n')
    f.close()


### クローリング ###

# robot.txtを読む
rp = urllib.robotparser.RobotFileParser()
rp.set_url(f"{start_url}/{robots}")
rp.read()

# サイトマップをクロール対象にする
sitemap = rp.site_maps()

url_list = [start_url]
url_list.extend(sitemap)

crawled_list = []

count = 0
for i in range(loop):
    locs = []
    atags = []
    for url in url_list :
        if url in crawled_list :
            # クロール済みのURLはスキップする
            continue
        # robots.txtでクロール禁止になっていないかチェック
        canf = rp.can_fetch("*",url)
        if canf == False :
            # can_fetch()がFalseを返した場合は、このURLはスキップする
            continue

        time.sleep(sleeptime) #しばし待つ

        try :
            res = requests.get(url)
            ## アクセスログに記録
            savelog(url, log)
            # headerから'Content-Type'を抽出
            conttype = res.headers['Content-Type']
            print(conttype, url)
            if 'xml' in conttype :
                soup = BeautifulSoup(res.content, 'xml')
                locs.extend(soup.find_all('loc'))
            elif 'html' in conttype :
                soup = BeautifulSoup(res.content, 'html.parser')
                # 次のループで使うURLの候補として<a>タグのリストをため込む
                for tag_a in soup.find_all("a") :
                    atags.append(str(tag_a))

                # テキスト抽出するかどうか確認
                scraping_flg = True
                for noscraping in noscraping_list:
                    if url == noscraping :
                        scraping_flg = False
                        break
                # カテゴリーページかどうかの確認
                noscraping = re.match('https://wired.jp/[a-z0-9\-]+?/$', url)
                if noscraping != None :
                    scraping_flg = False
                noscraping = re.match('https://wired.jp/tag/[a-z0-9\-]+?/$', url)
                if noscraping != None :
                    scraping_flg = False
                noscraping = re.match('https://wired.jp/membership/theme/[a-z0-9\-]+?/$', url)
                if noscraping != None :
                    scraping_flg = False
                # アーカイブのトップページかどうかの確認
                noscraping = re.match('https://wired.jp/archive/[0-9]+?/[0-9]+?/[0-9]+?/$', url)
                if noscraping != None :
                    scraping_flg = False
                noscraping = re.match('https://wired.jp/archive/[0-9]+?/[0-9]+?/$', url)
                if noscraping != None :
                    scraping_flg = False
                noscraping = re.match('https://wired.jp/archive/[0-9]+?/$', url)
                if noscraping != None :
                    scraping_flg = False

                if scraping_flg == True :
                    # テキスト抽出
                    cont_txt = gettext(soup)
                    count += 1
                    # テキスト抽出結果を保存
                    save_result(cont_txt, url=url, filename = result_file)
                    save_text(cont_txt[1], url=url, filename = text_file)
                    print(count, cont_txt[1]) # 動作確認用

                    # 取得したhtmlをファイルに保存
                    filename = str(count).zfill(5) + sub_filename
                    filepath = os.path.join(directory,filename)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(str(res.text))
                    f.close()

                    # ファイル名とurlのセットを記録しておく
                    logdata = {'filename': filename, 'url': url}
                    with open(logfile, 'a', encoding='utf-8') as f:
                        f.write(json.dumps(logdata)+'\n')
                    f.close()

        except :
            # エラーの場合は、urlをログに記載して継続
            print(f'Error: "{url}"')
            ## エラーログに記録
            savelog(url, log, error=True)


    # 使い終わったurl_listをクロール済みリストに追加
    crawled_list.extend(url_list)
    crawled_list = list(set(crawled_list)) # 重複削除

    # 次のループのためのurl_listを作る
    url_list = []
    # html
    for atag in atags :
        # <a.+?href="(.+?)".*?>
        for url in re.findall('<a.+?href="(.+?)".*?>', str(atag)) :
            if url[0] == '/' :
                url = f'{start_url}{url}'
            url = re.sub('[?#].+','',url)
            # wired.jpのサイトだけをurl_listに追加
            if start_url in url :
                url_list.append(url)

    # xml
    for loc in locs :
        for url in re.findall('<loc>(.+?)</loc>', str(loc)):
            url_list.append(url)

    url_list = list(set(url_list)) # 重複削除
