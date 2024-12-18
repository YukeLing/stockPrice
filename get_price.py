import requests
import time
import json

def get_price():
    url = r'https://finance.pae.baidu.com/vapi/v1/getquotation?srcid=5353&all=1&pointType=string&group=quotation_index_minute&query=000001&code=000001&market_type=ab&newFormat=1&name=上证指数&finClientType=pc'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Cookie': 'BIDUPSID=3D8559141ADD315DAD1EA09E8B92E778; PSTM=1732673126; BAIDUID=3D8559141ADD315DAD1EA09E8B92E778:FG=1; BDUSS=ZPa0dmbDAtVnQyZnkxa05lY2dxUllGNlFCbDJpbU1XU3V5N2tZVU85WlRQRzVuSVFBQUFBJCQAAAAAAAAAAAEAAABNlxV8Rm9yZXZlcsHo0~Dp8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFOvRmdTr0Znaj; BDUSS_BFESS=ZPa0dmbDAtVnQyZnkxa05lY2dxUllGNlFCbDJpbU1XU3V5N2tZVU85WlRQRzVuSVFBQUFBJCQAAAAAAAAAAAEAAABNlxV8Rm9yZXZlcsHo0~Dp8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFOvRmdTr0Znaj; MCITY=-179%3A; H_WISE_SIDS_BFESS=61027_61206_61211_61213_61209_61234_61278_61301_60851_61338; H_PS_PSSID=61027_61301_60851_61338; H_WISE_SIDS=61027_61301_60851_61338; BAIDUID_BFESS=3D8559141ADD315DAD1EA09E8B92E778:FG=1; delPer=0; PSINO=5; BA_HECTOR=240l81a001ak212k24ah840hbld5s51jlf3f31v; ZFY=4hUJl0kk4KA0mt0ZHDR:B0L8zDoBrj43iQlFZm7wQQMQ:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_YTY5NDgwYzdkNjI2ZjQyYTZiYzZjZWQ0OTRhY2RiN2U0YzM4MjVhNDRlYzQ4NTNkNzk3MGU0MGY5OTE1ZjdiNzgwMWRkYzEwNWUxNjgzYWY4MDY0YzFhODRiYjE3YTU3N2Q0N2VlNGRiMDZkOTdjODljNTA5OTFkMmU0ODhiZmJlZGZlZWIyMTEzNDM2YzU3Yjk3OGEwYWMwMzg3MGMwMw==',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh'
    }
    resp = requests.get(url,headers=head)
    resp.close()
    # jjson = resp.
    # resp.encoding = 
    # print(resp.text)

# get_price()
    resp_json = json.loads(resp.text)
    timee = resp_json["Result"]["update"]["text"]
    price = resp_json["Result"]["cur"]["price"]
    # dt_object = datetime.datetime.fromtimestamp(timee)
    return timee,price
# print(dt_object) 
if __name__ == "__main__":
    print("上证指数")
    a = 0
    while 1:
        timme,price = get_price()
        print("当前时间为：" + str(timme) + "   当前价格为：" + str(price) + "    ", end="\r")
        time.sleep(5)
        a += 1 
        if a == 12:
            print("当前时间为：" + str(timme) + "   当前价格为：" + str(price) + "    ")
            a = 0
# print(resp.text)

