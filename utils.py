from flask import jsonify
from datetime import date, datetime
import xmltodict


def today():
    return date.today().strftime('%Y%m%d')


# 중앙대학교 식단 api에 식당별로 예외가 많음
def make_readable(xml):
    data = xmltodict.parse(xml)

    if data.get('map').get('msgCode').get('value') == 'error':
        return '오류가 발생했습니다.'

    meal_list = data.get('map').get('vector').get('map')
    if meal_list:
        result = datetime.now().strftime('<%Y년%m월%d일%H시>\n')
        if isinstance(meal_list, dict):
            result += meal_list.get('menunm').get('@value') + '\n'
            result += meal_list.get('tm').get('@value') + '\n'
            result += meal_list.get('amt').get('@value') + '\n'
            result += meal_list.get('menunm1').get('@value') + '\n'
            return result.replace('<br>', '\n')
        elif isinstance(meal_list, list):
            for meal in meal_list:
                result += meal.get('menunm').get('@value') + '\n'
                result += meal.get('tm').get('@value') + '\n'
                result += meal.get('amt').get('@value') + '\n'
                result += meal.get('menunm1').get('@value') + '\n\n'
            return result.replace('<br>', '\n')
    return '오늘은 메뉴가 없어요!'


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
