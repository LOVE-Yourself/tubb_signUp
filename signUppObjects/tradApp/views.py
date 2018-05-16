from django.shortcuts import render
# Create your views here.
import json

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views.generic import View

from .forms import CoachOrdersForm
from .models import Coach_Orders

from urllib.parse import urlparse, parse_qs
from utils.alipay import AliPay
from Lyonline.settings import private_key_path,ali_pub_key_path
from datetime import datetime

from users.models import UserProfile
from driverSchool.models import Coach

from utils.about_pay import get_wxpayUrl,get_alipayUrl

class Payfor(View):
    def post(self,request):

        course_name = request.POST.get('curriculumName','')
        username = request.POST.get('userName','')
        orderMount = request.POST.get('totalPayMoney','')
        style_pay = request.POST.get('payMethod','')
        ordersn1 = request.POST.get('orderId','')
        print('---kecheng?--->',ordersn1)
        coachOrder = Coach_Orders()
        coachOrder.order_sn = ordersn1

        coachOrder.course_name = course_name
        coachOrder.username = username
        coachOrder.order_mount = orderMount
        coachOrder.pay_type = style_pay
        coachOrder.pay_mount = '1'
        coachOrder.order_status = 'WAIT_BUYER_PAY'
        coachOrder.user = request.user
        coachOrder.save()

        if style_pay == 'weixinPay':
            #微信支付
            payUrl = get_wxpayUrl(coachOrder.order_sn,coachOrder.pay_mount)
            print('---那个url---》',payUrl)
            #返回给前段
            resp = {'status': 200, 'payUrl': payUrl,}
            return HttpResponse(json.dumps(resp), content_type='application/json')

        else:
            payUrl = get_alipayUrl(coachOrder.order_sn, coachOrder.pay_mount)
            print('---那个url---》', payUrl)
            resp = {'status': 200, 'payUrl': payUrl,}
            return HttpResponse(json.dumps(resp), content_type='application/json')

#对返回来的url进行验证加密  防止别人伪造你的请求 pc端口
class AlipayReturnView(View):
    def get(self,request):
        alipay = AliPay(
            appid="2016091100490098",
            app_notify_url="test.tuobaba.cn:5020/pay/notyfile_return/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="test.tuobaba.cn:5020/pay/alipay_return/"
        )
        #sss = request.GET.get('trade_no','')
        #支付成功 跳转回来
        o = urlparse(request.get_full_path())
        query = parse_qs(o.query)
        processed_query = {}
        ali_sign = query.pop("sign")[0]
        for key, value in query.items():
            print('---??---->',key)
            processed_query[key] = value[0]
        s = alipay.verify(processed_query,ali_sign)#比对跳转回来的信息参数与之前发过去的信息参数（加密的sign）
        if s:
            #获取数据库里的记录
            trade_no = processed_query['trade_no']
            # order_status = processed_query['trade_status']
            order_status = 'TRADE_SUCCESS'
            order_sn = processed_query['out_trade_no']
            coachOrders = Coach_Orders.objects.filter(order_sn=order_sn)
            for coachOrder in coachOrders:
                coachOrder.trade_no = trade_no
                coachOrder.order_status = order_status
                coachOrder.pay_time = datetime.now()
                coachOrder.save()
                users = UserProfile.objects.filter(Coach_Orders_id=coachOrder.id)
                for user in users:
                    user.order_name = coachOrder.coach_name
                    user.save()
                #改变教练的学生人数
                coachs = Coach.objects.filter(name=coachOrder.coach_name)
                for coach in coachs:
                    coach.students += 1
                    coach.save()
            resp = 'success'
        else:
            resp = {'code': 500, 'detail': 'postchengg'}

        #更改用户表教练名称

        return HttpResponse(json.dumps(resp),content_type='application/json')


    def post(self,request):
        resp = {'code':300,'detail':'postchengg'}

        print('------------------------------?>>>>>>>>>>>>')
        #支付成功 跳转回来
        return HttpResponse(json.dumps(resp),content_type='application/json')

#手机支付回调
class NotyfileReturnView(View):
    def get(self,request):

        resp = {'code':666,'detail':'postchengg'}
        print('---------------get---------------?>>>>>>>>>>>>')
        #支付成功 跳转回来
        return HttpResponse(json.dumps(resp),content_type='application/json')


    def post(self,request):
        resp = {'code':333,'detail':'postchengg'}
        print('--------------post----------------?>>>>>>>>>>>>')
        #支付成功 跳转回来
        return HttpResponse(json.dumps(resp),content_type='application/json')



#-------------------------微信扫码支付------------------------------------------->

from utils.QR_code import Gnerate_code

class wxpay_View(View):
    def get(self,request):
        #拿到code_url 生成二维码
        code_url = request.GET.get('code_url')
        if code_url == '':
            print('微信支付失败,查看订单状态')
            error = '微信支付失败,查看订单状态'
            return render(request,'wxPay.html',{'error':error})
        else:
            qrcode = Gnerate_code(code_url)
            image_name = qrcode.get_codeImage()

            return render(request,'wxPay.html',{'image_name':'QRcode/'+image_name})

'''
{'appid': 'wx98e346c1131740ca', ------》
'bank_type': 'CFT', 
'cash_fee': '1', 
'device_info': 'WEB', 
'fee_type': 'CNY', 
'is_subscribe': 'Y', 
'mch_id': '1488403182', ---》
'nonce_str': 'b0afff883df911e88720000c29a6fa69', 
'openid': 'o0k-JvwY7ZHdZeLT5KKCN2mFYIzY', 
'out_trade_no': '20150320010101135', 
'result_code': 'SUCCESS', 
'return_code': 'SUCCESS', 
'sign': 'A8B65B3132B20B66805B9DA0D53242E0', 
'time_end': '20180412103230', 
'total_fee': '1', 
'trade_type': 'NATIVE',
'transaction_id': '4200000058201804126858423343'}

'''


from utils.about_pay import response_dict
from utils.util import dict_xml
#支付成功回调
class Notify_ReturnView(View):
    def get(self):
        print('---get--->')

    def post(self, request):
        resp = request.body
        if isinstance(resp, bytes):
            ult = str(resp, encoding='utf-8')
            #验证签名成功后会返回字典
            body_dict = response_dict(ult)
            #模型加入微信生成的订单
            #返回接受成功 result_code =sucess 要不微信系统一值在尝试请求
            if body_dict:
                data = {'return_code': 'SUCCESS', 'return_msg': 'OK'}
                s = dict_xml(data)
                return HttpResponse(s,content_type='text/xml')
            else:
                print('【+error】微信支付返回字典为空')
        elif isinstance(resp, str):
            body_dict = response_dict(resp)
            if body_dict:
                data = {'return_code': 'SUCCESS', 'return_msg': 'OK'}
                s = dict_xml(data)
                return HttpResponse(s,content_type='text/xml')
            else:
                print('【+error】微信支付返回字典为空')
        else:
            raise Exception('no type is str or bytes')



