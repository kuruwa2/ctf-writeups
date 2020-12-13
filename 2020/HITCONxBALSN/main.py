import io
import os
import json
import pyzipper
import traceback
import aiohttp
import aiofiles
import asyncio

from Crypto.Cipher import AES
from aiohttp import web

flags = [
b'g7f{***_s7aCK_sma5HiNG_dEt3cted_***}',
'GTF{這一隻手，今天已經不是我的手，這隻手，是人民的手，人民的意志，人民的法槌}'.encode('utf8'),
b'BALSN{printable ascii+}',
b'GTF{io game hint: window.socket.emit(\'scorepersecondsssup\');}',
b'GtF{d0 yOU knoW h0W2haCK?}',
'GTF{玫瑰是藍的 紫羅藍是紅的 我真的要去PP了}'.encode('utf8'),
b'GTF{curl kaibro.tw | sh}',
b'g7F{php 1$ 7HE b3s7 lanGUaGe 1N 7h3 w0rlD}',
b'GTf{hOuse 0f 0ranGe}',
'GTF{只要呼吸就好}'.encode('utf8'),
'GTF{🛵🏍️欸幹😲！穿山甲欸🧐🧐！嗚呼😎😎😤😤！這可以養嗎🤪🤪！？欸蟑螂這可以養嗎🤔🤔！我不知道🧐🧐你抓回家😤😤！欸借過借過不要跑😲😲😲！嗚嗚他跑掉了😱😱！嗚呼呼😤😤😤！喔好屌🍆喔！}'.encode('utf8'),
b'GTf{5egMEntati0N FAult (Core DumPEd)}',
'🥕{はおー！ヒメヒナでーす！}'.encode('utf8'),
b'gTF{wash your hand beFor3 Return tO l1bC}',
'GTF{飛天義大利麵神教}'.encode('utf8'),
b'gTF{SUdo rM -Rf /*}',
'GTF{今晚，我想來點星巴克的特選馥郁那堤配起司牛肉可頌}'.encode('utf8')]

def pad(s):
    if len(s)%16!=0:
        s += b'\0'*(-len(s)%16)
    return s

scoreboard_host = os.environ.get('SCOREBOARD', '127.0.0.1')
bind_host = os.environ.get('HOST', '127.0.0.1')

MAX_HIST = 3000
MAX_SIZE = 1024
FAILED_SCORE = 9999
score, history = 0, []
#  round, key, flag, correct = 0, None, None, False
round, key, flag, correct = 0, b'0' * 16, b'0'*32, False

flag = flags[round]
key = os.urandom(16)
flag = pad(flag)
iv = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
flag = iv+cipher.encrypt( flag)

routes = web.RouteTableDef()


def check_flag():
    if round < 0:
        raise web.HTTPPreconditionFailed()
    if flag is None or key is None:
        raise web.HTTPServiceUnavailable()


@routes.get('/admin/next_round')
async def _(req):
    global round, key, flag, correct, history, score

    #  try:
    #      token = req.query['token']
    #      assert token == req.app['scoreboard_token']
    #  except Exception:
    #      raise web.HTTPForbidden()

    try:
        new_round = int(req.query['round'])
        new_key = bytes.fromhex(req.query['key'])
        new_flag = bytes.fromhex(req.query['flag'])
        assert len(new_key) == 16
        assert len(new_flag) > 16
        assert len(new_flag) % 16 == 0
        old_score = FAILED_SCORE if not correct else min(FAILED_SCORE, score)
        old_history = history
        old_correct = correct
        resp = {'round': round ,'correct': old_correct, 'history': old_history, 'score': old_score}
        #  with open(f'/backup/{os.urandom(6).hex()}.json', 'w') as f:
        #      json.dump(resp, f)
    except Exception:
        raise web.HTTPBadRequest()

    print(f'[+] New round {new_round}')
    # print(f'[+] New round {new_round} {new_key.hex()} {new_flag.hex()}')
    round, key, flag, correct, history, score = new_round, new_key, new_flag, False, [], 0

    return web.json_response(resp)


@routes.get('/status')
async def _(req):
    check_flag()

    return web.json_response({'round': round, 'correct': correct, 'score': score, 'flag': flag.hex()})


@routes.get('/compress')
async def _(req):
    global score
    check_flag()

    try:
        data = bytes.fromhex(req.query['x'])
        assert 16 < len(data) <= MAX_SIZE
        assert len(data) % 16 == 0
    except Exception:
        raise web.HTTPBadRequest()

    aes = AES.new(key, AES.MODE_CBC, data[:16])
    ptxt = aes.decrypt(data[16:]).strip(b'\0')

    score += 1
    if len(history) < MAX_HIST:
        history.append([0, data.hex()])

    out = io.BytesIO()
    with pyzipper.AESZipFile(out,
                             'w',
                             compression=pyzipper.ZIP_LZMA,
                             encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(key)
        zf.writestr('flag', ptxt)

    return web.Response(
        headers={'Content-Disposition': 'Attachment; filename=flag.zip'},
        body=out.getvalue())


@routes.get('/submit')
async def _(req):
    global correct, score, key, flag, round

    check_flag()

    try:
        data = req.query['x'].encode('utf8')
    except Exception:
        raise web.HTTPBadRequest()

    score += 1
    if len(history) < MAX_HIST:
        history.append([1, data.hex()])

    aes = AES.new(key, AES.MODE_CBC, flag[:16])
    ptxt = aes.decrypt(flag[16:]).strip(b'\0')

    if data == ptxt:
        correct = True
        round += 1
        if round == len(flags):
            round = 0
        flag = flags[round]
        key = os.urandom(16)
        flag = pad(flag)
        iv = os.urandom(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        flag = iv + cipher.encrypt(flag)

    return web.Response(text='⊂((・▽・))⊃' if data == ptxt else '（ ´థ౪థ） ( ´థ,_‥థ｀)')


@routes.get('/')
async def _(req):
    return aiohttp.web.HTTPFound('/index.html')


routes.static('/', './')



@web.middleware
async def error_middleware(request, handler):
    resp = web.HTTPInternalServerError()
    try:
        resp = await handler(request)
    except web.HTTPException as ex:
        resp = ex
    except:
        traceback.print_exc()
        resp = web.HTTPInternalServerError()
    if resp is None or resp.status < 400:
        return resp
    if resp.status == 403:
        raise web.HTTPForbidden(text='( ･∀･)つ＝≡≡ξ)Д`) 403')
    if resp.status == 404:
        raise web.HTTPNotFound(text='(ﾟヘﾟ) 404')
    if resp.status == 412:
        raise web.HTTPPreconditionFailed(text='Not started yet. 412')
    if resp.status < 500:
        raise web.HTTPBadRequest(text='¯\_༼ ಥ ‿ ಥ ༽_/¯ 500')
    if resp.status == 503:
        raise web.HTTPServiceUnavailable(text=''
            'Congrats\n'
            'You might have crashed the server.\n'
            'There is no flag on this server now.\n'
            '(σﾟ∀ﾟ)σﾟ∀ﾟ)σﾟ∀ﾟ)σ\n'
            '(σﾟ∀ﾟ)σﾟ∀ﾟ)σﾟ∀ﾟ)σ\n'
            '(σﾟ∀ﾟ)σﾟ∀ﾟ)σﾟ∀ﾟ)σ\n'
            '(σﾟ∀ﾟ)σﾟ∀ﾟ)σﾟ∀ﾟ)σ\n'
            '\n'
            'Please contact admin if you stop all your exploits\n'
            'but the problem still exists in the next round.\n'
            )
    raise web.HTTPInternalServerError(text='((((；ﾟДﾟ))) wtf')


async def get_scoreboard_token(app):
    return 'admin'
    #  async with aiohttp.ClientSession() as sess:
    #      while True:
    #          try:
    #              async with sess.get(f'http://{scoreboard_host}:31337/token') as res:
    #                  app['scoreboard_token'] = await res.text()
    #          except Exception:
    #              traceback.print_exc()
    #              print('')
    #              await asyncio.sleep(1)
    #          else:
    #              break


app = web.Application(middlewares=[error_middleware])
app.on_startup.append(get_scoreboard_token)
app.add_routes(routes)
web.run_app(app, host=bind_host, port=11337)
