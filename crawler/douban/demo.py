import requests
import json

def main():
    data = requests.get('http://v3.wufazhuce.com:8000/api/channel/reading/more/0').content

    print(json.loads(data))

if __name__ == '__main__':
    main()