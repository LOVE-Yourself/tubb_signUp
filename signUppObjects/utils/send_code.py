import requests,json,random

class YunPian(object):
    def __init__(self,api_key):
        self.api_key = api_key
        self.signle_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_code(self,code,mobile,send_type):
        parmas = {
            'apikey':self.api_key,
            'text':"【拓叭吧学车】您的验证码是{0}".format(code),
            'mobile':mobile,
        }
        response = requests.post(self.signle_send_url,data=parmas)
        re_dict = json.loads(response.text)
        print('---发送验证码-返回信息-》',re_dict)
        return re_dict['msg']
    def get_code(self):
        l = [0,1,2,3,4,5,6,7,8,9]
        code = ''
        for i in random.sample(l,4):
            code += str(i)
        return code

if __name__ == '__main__':
    yun_pain = YunPian('05e6858c497059ebea9bc5b81b08f37d')
    l = [0,1,2,3,4,5,6,7,8,9]
    code = ''
    for i in random.sample(l,6):
        code += str(i)
    #如果在表里面存在从新生成
    yun_pain.send_code(code,'18268056200')

