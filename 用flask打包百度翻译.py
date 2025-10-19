from flask import Flask, request, jsonify,Response
import requests, random, hashlib, json

app = Flask(__name__)

# 首页路由（Day9 保留）
@app.route('/')
def home():
    return 'Hello Flask'

# ====== Day10 新接口 ======
BAIDU_APPID = '20251015002475797'          # ← ① 改成自己的
BAIDU_KEY   = '7Mf6SAsxw4gQBxwGEMCk'           # ← ② 同上

@app.route('/ai/trans')
def trans():
    q     = request.args.get('q', 'hello')          # 取查询参数
    salt  = random.randint(32768, 65536)
    sign  = hashlib.md5((BAIDU_APPID + q + str(salt) + BAIDU_KEY).encode()).hexdigest()
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    params= {
        'q'     : q,
        'from'  : 'auto',
        'to'    : 'zh',
        'appid' : BAIDU_APPID,
        'salt'  : salt,
        'sign'  : sign
    }
    resp = requests.get(url, params=params)
    try:
        dst = resp.json()['trans_result'][0]['dst']
        return Response(
            json.dumps({'src': q, 'dst': dst},ensure_ascii=False),
            mimetype='application/json;charset=utf-8'
        )
    except Exception as e:
        return jsonify({'error': resp.text}), 500

if __name__ == '__main__':
    app.run(debug=True)
