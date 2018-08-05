from flask import jsonify
import datetime


def today():
    return datetime.date.today().strftime('%Y%m%d')


def make_readable(xml):
    return xml


def make_return_format(buttons, text=None):
    return jsonify({
        'keyboard': {
            'type': 'buttons',
            'buttons': buttons
        },
        'message': {
            'text': text
        }
    })
