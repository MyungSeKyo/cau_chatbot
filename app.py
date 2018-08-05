from flask import Flask, request, jsonify
from utils import today, make_readable, make_return_format
from conf import URL, BODY_TEMPLATE, CAMPUSES, SEOUL_STORES, ANSUNG_STORES
import requests

app = Flask(__name__)


@app.route('/keyboard', methods=['GET'])
def keyboard():
    return jsonify({
        'type': 'buttons',
        'buttons': list(CAMPUSES)
    })


@app.route('/message', methods=['POST'])
def message():
    content = request.get_json().get('content')

    if content == '서울':
        return make_return_format(list(SEOUL_STORES), '식당을 선택해주세요.')

    elif content == '안성':
        return make_return_format(list(ANSUNG_STORES), '식당을 선택해주세요.')

    elif content == '뒤로가기':
        return make_return_format(list(CAMPUSES), '캠퍼스를 선택해주세요.')

    elif content in SEOUL_STORES:
        body = BODY_TEMPLATE.format(
            campus=CAMPUSES['서울'],
            store=SEOUL_STORES[content],
            today=today()
        )
        try:
            response = requests.post(URL, body)
        except Exception:
            return make_return_format(list(SEOUL_STORES), '오류가 발생했습니다.')
        return make_return_format(list(SEOUL_STORES), make_readable(response.text))

    elif content in ANSUNG_STORES:
        body = BODY_TEMPLATE.format(
            campus=CAMPUSES['안성'],
            store=ANSUNG_STORES[content],
            today=today()
        )
        try:
            response = requests.post(URL, body)
        except Exception:
            return make_return_format(list(SEOUL_STORES), '오류가 발생했습니다.')
        return make_return_format(list(ANSUNG_STORES), make_readable(response.text))

    else:
        return make_return_format(list(CAMPUSES), '오류가 발생했습니다.')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
