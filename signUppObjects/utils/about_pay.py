

#-------------------微信回调验证签名----------------------------》
#-------------------成功后返回dict------------------------------------》
import xml.etree.ElementTree as ElementTree
import sys

PY2 = sys.version_info[0] == 2
if not PY2:
    # Python 3.x and up
    text_type = str
    string_types = (str,)
    xrange = range

    def as_text(v):  ## 生成unicode字符串
        if v is None:
            return None
        elif isinstance(v, bytes):
            return v.decode('utf-8', errors='ignore')
        elif isinstance(v, str):
            return v
        else:
            raise ValueError('Unknown type %r' % type(v))

    def is_text(v):
        return isinstance(v, text_type)

def xml2dict(xml_str):
    """xml to dict

    @:param xml_str: string in XML format
    @:return: Dictionary
    """
    # return xmltodict.parse(xml_str)['xml']
    root = ElementTree.fromstring(xml_str)
    assert as_text(root.tag) == as_text('xml')
    result = {}
    for child in root:
        tag = child.tag
        text = child.text
        result[tag] = text
    return result
from pywxpay import WXPay
wxpay = WXPay(app_id='wx98e346c1131740ca',
              mch_id='1488403182',
              key='DFSDSFDSxzdsagdsxcdsfds123098765',
              cert_pem_path='',
              key_pem_path='',
              timeout=6000)

#拿到这些签名进行比对
def response_dict(xml_str):
    resp_dict = xml2dict(xml_str)
    if 'return_code' in resp_dict:
        return_code = resp_dict.get('return_code')
    else:
        raise Exception('no return_code in responxe data: {}'.format(ult))
    if return_code == 'SUCCESS':
        #检查微信响应的xml数据中签名是否合法，先转换成dict
        #wxpay    is_pay_result_notify_signature_valid
        if wxpay.is_pay_result_notify_signature_valid(resp_dict):
            return resp_dict
        else:
            raise Exception('the sign not valid')
    elif return_code == 'FAIL':
        return resp_dict

#------------------返回支付路由（支付宝,微信 ）---------------------->
from utils.alipay import AliPay
from Lyonline.settings import private_key_path, ali_pub_key_path, QR_code_path


def get_alipayUrl(order_no, pay_mount):
    alipay = AliPay(
        appid="2016091100490098",
        app_notify_url="test.tuobaba.cn:5020/pay/notyfile_return/",
        app_private_key_path=private_key_path,
        alipay_public_key_path=ali_pub_key_path,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=True,  # 默认False,
        return_url="test.tuobaba.cn:5020/pay/alipay_return/"
    )
    url = alipay.direct_pay(
        subject="测试订单2",
        out_trade_no=order_no,
        total_amount=pay_mount,
        return_url="test.tuobaba.cn:5020/pay/alipay_return/"

    )
    re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
    return re_url



from pywxpay import WXPay


def get_wxpayUrl(order_no, pay_mount):
    wxpay = WXPay(app_id='wx98e346c1131740ca',
                  mch_id='1488403182',
                  key='DFSDSFDSxzdsagdsxcdsfds123098765',
                  cert_pem_path='',
                  key_pem_path='',
                  timeout=6000)  # 毫秒

    wxpay_resp_dict = wxpay.unifiedorder(dict(device_info='WEB',
                                              body='测试商家-商品类目',
                                              detail='',
                                              out_trade_no=order_no,
                                              total_fee=int(pay_mount),
                                              fee_type='CNY',
                                              notify_url='http://xxd.tuobaba.cn/pay/wxnotify/',
                                              spbill_create_ip='192.168.192.132',
                                              trade_type='NATIVE')
                                         )

    code_url = wxpay_resp_dict.get('code_url', '')
    print('????????------》》》》》》', wxpay_resp_dict)
    wxpayUrl = 'http://192.168.192.131:8000/pay/wxpay?code_url={0}'.format(code_url)
    return wxpayUrl
