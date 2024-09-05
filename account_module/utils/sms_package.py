from .melipayamak import Api
class SMSHandler:
    username = '09022990626'
    password = '24PO$'
    api = Api(username, password)
    sms = api.sms()
    def __init__(self, to , message):

        self._from = '50002710090626'
        self._to = to
        self._message = message

    def send_otp(self):
        welcome_message = f'''به سامانه فروشگاه نقش جهان خوش آمدید.
کد ورود به حساب کاربری شما:
{self._message}
لغو11'''


        response = self.sms.send(self._to, self._from, welcome_message)
        error = response.get('StrRetStatus')

        if error == 'Ok':
            return True
        else:
            return False
    def send_factor_code(self, download_url, title):
        download_url = str(download_url)
        title = str(title)
        factor_message = (f''' مشترک گرامی یک فاکتور به نام شما با عنوان {title} در سامانه فروشگاه نقش جهان صادر شد.
کد فاکتور:
{self._message}
لینک دانلود:
{download_url}
لغو11''')
        response = self.sms.send(self._to, self._from, factor_message)
        error = response.get('StrRetStatus')


        if error == 'Ok':
            return True
        else:
            return False
