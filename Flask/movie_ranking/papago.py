import os
import sys
import json
import urllib.request

def papago_translate(ko_data):
    client_id = "23rMCvEBKJKQe73NXqcO"
    client_secret = open("secret.txt", "r").read()

    encText = urllib.parse.quote(ko_data)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        data = json.loads(response_body)
    else:
        print("Error Code:" + rescode)
    return data['message']['result']['translatedText']