import sys
import requests
import json

def main():
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    try:
        payload = {'q': 'value1'}
        response = requests.get('http://xxxxx', params=payload)
        if response.status_code == 200:
            data = response.json()
            print(data["hash"])
        else:
            print("400 Bad Request")
    except requests.exceptions.RequestException as e:
        print("エラー : ",e)

if __name__ == '__main__':
    main()