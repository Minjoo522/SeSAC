import smtplib

smtp = smtplib.SMTP_SSL('smtp.naver.com', 465)

smtp.ehlo()
#  ehlo => hello와 동일, server와 메시지 주고 받음
my_password = open("secret.txt", "r").read()
smtp.login('m0522j@naver.com', my_password)
# '메일 주소', '비밀번호'

from email.message import EmailMessage
msg = EmailMessage()

msg['Subject'] = '메일제목'
msg['FROM'] = 'm0522j@naver.com'
msg['To'] = 'm0522inju@gmail.com'
msg.set_content('메일본문, 멀티라인도 가능, 여기에 각자 쓰고 싶은 메세지 작성')

smtp.send_message(msg)

smtp.quit()