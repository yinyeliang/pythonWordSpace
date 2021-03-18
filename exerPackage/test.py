import requests

order_url = f'https://testapi.imgo.tv/mg.fenxiao.order.create'
header = {'Content-Type':'content-type: application/json'}
#header={'Content-Type':'application/x-www-form-urlencoded'}
payload = {
        'access_token':'2ca5f6b8a5bdf875629add85a15882cd',
        'app_key':100023,
        'timestamp':'2021-03-15 17:29:30',
        'sign':'',
        'channelId':7,
        'outOrderNo':234568888884,
        'consignee':'张三四',
        'province':'湖南',
        'city':'长沙市',
        'district':'雨花区',
        'address':'的发的放大放大发',
        'mobile':18588239071,
        'goodsNum':1,
        'addTime':'2021-03-15 13:33:21',
        'payTime':'2021-03-15 13:34:21',
        'transactionId':'213389939220303955',
        'transactionPayId':'3424245354565766',
        'userNote':'QQQQQQQ',
        'adminNote':'WWWWWWW',
        'orderType':0,
        'orderSource':2,
        'isBorder':0,
        'goodsList':[{
                     "sku_id":"4017",
                     "goods_num":1
                     }]
        }
reps = requests.post(order_url,data = payload,headers = header)
#print(reps.headers)
print(reps.text)