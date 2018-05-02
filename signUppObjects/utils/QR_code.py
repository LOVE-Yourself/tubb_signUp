#weixin://wxpay/bizpayurl?pr=Tt14r6t
#weixin://wxpay/bizpayurl?pr=4yTHV7y
#weixin://wxpay/bizpayurl?pr=0NZDzxj

from Lyonline.settings import QR_code_path
# OR_code_path = '/home/nanfengpo/Documents/lastJD/webMuKe/xiangmu2/Lyonline/media/QRcode/'
import os
import qrcode
import string
import random
class Gnerate_code(object):
    def __init__(self,code_url):
        self.code_url = code_url

    def get_codeImage(self):
        img = qrcode.make(self.code_url)
        image_name = ''.join(random.sample(string.ascii_letters + string.digits, 6))+'.png'
        s = os.path.join(QR_code_path, image_name)
        img.save(s)
        print('--你的名字--->',image_name)
        return image_name

