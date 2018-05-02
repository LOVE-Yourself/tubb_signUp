# #
# # coding: utf-8
# from pywxpay import WXPay
#
# wxpay = WXPay(app_id='wx8888888998',
#               mch_id='8888888',
#               key='123434556677888999987766543543322',
#               # cert_pem_path='/path/to/apiclient_cert.pem',
#               # key_pem_path='/path/to/apiclient_key.pem',
#               timeout=6000)  # 毫秒
#
# wxpay_resp_dict = wxpay.unifiedorder(dict(device_info='WEB',
#                                           body='测试商家-商品类目',
#                                           detail='',
#                                           out_trade_no='2016090910595900000012',
#                                           total_fee=0.01,
#                                           fee_type='CNY',
#                                           notify_url='http://xxd.tuobaba.cn/wxpay/notify',
#                                           spbill_create_ip='39.107.243.161',
#                                           trade_type='NATIVE')
#                                      )
#
# print(wxpay_resp_dict)
#
#
# from datetime import datetime
# import time
# import random
# import _md5
# import string
#
# s = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #转换成时间数组
# timeArray = time.strptime(s, "%Y-%m-%d %H:%M:%S")
# #转换成时间戳
# timestamp = int(time.mktime(timeArray))
# ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
#
# appid = 'wx98e346c1131740ca'  #微信分配的公众账号ID
# mach_id = '1488403182' #微信支付分配的商户号
# time_stamp = timestamp
# nonce_str = ran_str
# product_id = '20170202172'
#
# stringA="appid=wx98e346c1131740ca&body=test&device_info=0.01&mch_id=1488403182&nonce_str=ibuaiVcKdpRxkhJA"
# stringSignTemp=stringA+"&key=DFSDSFDSxzdsagdsxcdsfds123098765"
#
# import hashlib
# # 生成MD5
# def genearteMD5(str):
#     # 创建md5对象
#     hl = hashlib.md5()
#
#     # Tips
#     # 此处必须声明encode
#     # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
#     hl.update(str.encode(encoding='utf-8'))
#
#     print('MD5加密前为 ：' + str)
#     print('MD5加密后为 ：' + hl.hexdigest())
#     return hl.hexdigest()
# sign = genearteMD5(stringSignTemp)
# url1 = 'weixin：//wxpay/bizpayurl?sign=0ef1ce6c47b8896df960999231b80f8f&appid=wx98e346c1131740ca&mch_id=20170202172&product_id=20170202172&time_stamp=1522655996&nonce_str=ibuaiVcKdpRxkhJA'
# url = ''
# print('---->',timestamp)


def dict_xml(data):
    xml = []
    for k in sorted(data.keys()):
        v = data.get(k)
        if k == 'return_code' and k == 'return_msg' and not v.startswith('<![CDATA['):
            v = '<![CDATA[{}]]>'.format(v)
        xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
    return '<xml>{}</xml>'.format(''.join(xml))


data = {'return_code':'SUCCESS','return_msg':'OK'}

s = dict_xml(data)
print(s)


'''
<xml>

  <return_code><![CDATA[SUCCESS]]></return_code>
  <return_msg><![CDATA[OK]]></return_msg>
</xml>

<xml>
<code>![CADATA[SUCCESS]]</code>
<type>xml</type>
</xml>
'''