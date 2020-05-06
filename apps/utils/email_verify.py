from django.core.mail import send_mail
from bloggl import settings
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'bloggl.settings'


class EmailVerify():

    def check_mail(self, code, email):
        title = "jomornt blog注册验证信息"
        msg = "您的验证码是{code}，验证码5分钟内有效。如非本人操作，请忽略本短信".format(code=code)
        email_from = settings.DEFAULT_FROM_EMAIL
        # 发送邮件
        res_dict = {}
        try:
            send_mail(title, msg, email_from, [email])
            res_dict['status'] = 1
            res_dict['msg'] = "邮件发送成功"
        except:
            res_dict['status'] = 0
            res_dict['msg'] = "邮件发送失败，请稍后再试"
        return res_dict


if __name__ == "__main__":
    email_verify = EmailVerify()
    status = email_verify.check_mail('1234', '1270392394@qq.com')
    print(status)
