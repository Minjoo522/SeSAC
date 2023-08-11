# 메일 보내기
> - SMTP
> - POP3
> - IMAP

~~~python

# 메일 보내는 라이브러리
import smtplib
~~~
- MIME 포멧으로 인코딩을 해서 보낸다(인코딩, 변환 ➡️ 라이브러리가 해줌 ⤵️)

~~~python
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
~~~
- gmail : GCP를 통해 이메일 발송 권한 추가적으로 가능하다

## 네이버 메일 사용하는 경우
- 메일설정에서 smtp/pop3 사용 할 수 있도록 해야 함 : 보내는 것만 가능
