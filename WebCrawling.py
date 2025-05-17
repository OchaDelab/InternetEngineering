#
#by le [202412]
#MIT License
#

from bs4 import BeautifulSoup
import requests
import sys, getopt

def main(argv):
    url=""
    mode=""
    modeList={"all", "title", "text"}
    try:
        opts, args = getopt.getopt(argv,"hu:m:", ["url=", "mode="])
    except getopt.GetoptError:
        print ('python WebCrawling.py -u https://www.google.com -m <all|title|text>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('python WebCrawling.py -u https://www.google.com -m <all|title|text>')
            sys.exit(2)
        elif opt in ("-u", "--url"):
            url = arg
        elif opt in ("-m", "--mode"):
            mode = arg
            if mode not in modeList:
                print("ERROR: modeは次の値のみ入れてください: ", modeList)
                sys.exit(2)
    print ('Webページからデータ取得: "', url)
    # ターゲットURLからHTMLを取得
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 必要なデータを抽出
    match mode:
        case "all":
            print("Content:")
            print(soup.prettify())
        case "title":
            titles = soup.find_all('h2')
            for title in titles:
                print("Title:"+ title.text)
        case "text":
            print("Text only")
            texts = soup.find_all('p')
            for text in texts:
                print(text.get_text())
    
if __name__ == "__main__":
    main(sys.argv[1:])
