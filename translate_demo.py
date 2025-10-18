import requests ,random, hashlib,json
appid='20251015002475797'
secretKey='7Mf6SAsxw4gQBxwGEMCk'
q='hello world'
from_lang='auto'
to_lang='zh'
salt=random.randint(32768,65536)
sign=hashlib.md5( (appid+q+str(salt)+secretKey).encode()).hexdigest()
url='https://fanyi-api.baidu.com/api/trans/vip/translate'
params={
    'q':q,
    'from':from_lang,
    'to':to_lang,
    'appid':appid,
    'salt':salt,
    'sign':sign
}
resp=requests.get(url,params=params)
result=resp.json()
print('翻译结果：',result['trans_result'][0]['dst'])