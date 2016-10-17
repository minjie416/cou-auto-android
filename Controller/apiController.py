import json
import re
import urllib2
from urllib2 import Request
def normalize(args, keyword):
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    for k, v in args.items():
        if v is None:
            del args[k]
    return args

def format_unicode(string):
    format_str = filter(lambda x: not re.match(r'^\s*$', x), string)
    format_str = format_str.replace(" ","")
    return format_str.encode("utf-8")

def create_product(**args):
    keyword = ['name','region','bucket','publishKey','publishSecurity']
    encoded = json.dumps(normalize(args, keyword))
    url = "http://%s/%s/hubs" % ("10.200.20.28:7777", "v1")
    return Request(url=url, data=encoded)

def parse_json(json,i=0):
    if (isinstance(json,dict)):
        for item in json:
            if (isinstance(json[item],dict)):
                print ("****"*i+"%s : %s"%(item,json[item]))
                parse_json(json[item],i=i+1)
            else:
                print("****"*i+"%s : %s"%(item,json[item]))
    else:
        print ("param is not a json object!")

def get_num(x):
    try:
        if x is None or x == '':
            return 0
        num = str(''.join(ele for ele in x if ele.isdigit() or ele == ',')).replace(",","")
        return int(num)
    except Exception:
        return 0

class CAPI():

    def __init__(self):
        self.host = "capi.coupang.com"
        self.version = "v3"


    def get_product_details(self,productID,ItemID):
        info = {}
        url = "http://%s/%s/products/%s/?itemId=%s&usePage=true&type=multiple" \
              %(self.host,self.version,str(productID),str(ItemID))
        request = urllib2.Request(url=url)
        request.add_header('coupang-app','COUPANG|Android|5.1.1|4.3.9||cRdei2lE2uA:APA91bFryQh7HXk0DRooTOvvBn5d_BMspNT3M'
                                         'JHHK5nxL0plg5rxGo1JaJwpdiK0nuuBIosteqH8pp4UPViNADJ3nwdqSGOX-XJcQC5txQGdY6Ca34T'
                                         'omXH2Myk2AwfmqFvSi9N9-agp|00000000-477d-e359-d86d-4f9f39f7b412|Y|SM-J500N0|'
                                         '35cce34cda25eb78d20c1f9290c7ab82|4e30b1f5-d973-4a1c-bd79-58a5a1a7642b|XHDPI|'
                                         '14760960870590122794956||0||wifi|-1||')
        res = urllib2.urlopen(request)
        # response = json.loads(res.read())
        # return response
        response = json.loads(res.read())
        info.update({'buyableQuantity':int(response['rData']['vendorItem']['buyableQuantity']),
                     'productName':format_unicode(response['rData']['vendorItem']['title']),
                     'vendorItemId':int(response['rData']['vendorItem']['vendorItemId']),
                     'fee':format_unicode(response['rData']['vendorItem']['shippingFeeMessage'][0]['text']),
                     'feeValue':get_num(response['rData']['vendorItem']['shippingFeeMessage'][0]['text'])
                     })
        return info

    def get_product_info(self,productID,itemID):
        info = {}
        url = "http://%s/%s/products/%s/?itemId=%s&usePage=true&type=multiple" \
              %(self.host,self.version,str(productID),str(itemID))
        request = urllib2.Request(url=url)
        res = urllib2.urlopen(request)
        response = json.loads(res.read())
        info.update({'remainAmount':int(response['rData']['vendorItemDetail']['item']['remainCount']),
                     'salePrice':int(response['rData']['vendorItemDetail']['item']['salesPrice'])
                     })
        return info


    def get_options(self,productID,vendorID):
        url = "http://%s/vp/products/%s/loadOptions?vendorItemId=%s" \
              %(self.host,str(productID),str(vendorID))
        request = urllib2.Request(url=url)
        res = urllib2.urlopen(request)
        response = res.read()
        return response






if __name__ == "__main__":
    pass
    api = CAPI()
    # res = api.get_sale_price(2025032,3016279164,'8e76b55d054d47589ce577e324a4d48a2fad1fa7',10868038)
    res2 = api.get_product_details(8332740,3522475)
    print parse_json(res2,0)
    # print res2



