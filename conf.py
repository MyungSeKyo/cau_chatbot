URL = 'http://cautis.cau.ac.kr/TIS/portlet/comm/cPortlet001/selectList.do'

BODY_TEMPLATE = '<map><userid value="0"/><calvalue value="0"/><gb value="{campus}"/><today value="{today}"/><store value="{store}"/><storediv value="{store}"/><campfg value="{campus}"/></map>'

CAMPUSES = {
    '서울': 1,
    '안성': 2,
}

SEOUL_STORES = {
    '참슬기식당(310관 B4층)': '13',
    '생활관식당(블루미르308관)': '08',
    '생활관식당(블루미르309관)': '12',
    '학생식당(303관B1층)': '06',
    '교직원식당(303관B1층)': '07',
    'University Club(102관11층)': '11',
}

ANSUNG_STORES ={
    '안성학생식당': '09',
    '안성교직원식당': '10',
}
