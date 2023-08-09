# API
> Application Programming Interface
> - 내가 원하는 애플리케이션을 개발하기 위한 백엔드 스펙
- API 키 필요
- Client Secret : 절대 노출되면 안됨!

~~~zsh
curl "https://openapi.naver.com/v1/papago/n2mt" \
-H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
-H "X-Naver-Client-Id: " \
-H "X-Naver-Client-Secret: " \ # 노출되면 안됨!
-d "source=ko&target=en&text=만나서 반갑습니다." -v

# response
{"message":{"result":{"srcLangType":"ko","tarLangType":"en","translatedText":"Good to meet you.","engineType":"PRETRANS"},"@type":"response","@service":"naverservice.nmt.proxy","@version":"1.0.0"}}
~~~

## 영상처리
~~~zsh
pip install opencv-python
~~~