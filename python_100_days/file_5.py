import requests
import json


def main():
    data = [[4,2],[3,8],[5,9],[1,7]]
    # 将Python对象编码成json字符串
    data = sorted(data)
    print(data)

if __name__ == '__main__':
    main()