import requests
from bs4 import BeautifulSoup

class Physical:
    def __init__(self, minClass=None, tat=None, pay=None, place=None, area=None, tel=None):
        self.minClass = minClass
        self.tat = tat
        self.pay = pay
        self.place = place
        self.area = area
        self.tel = tel

class PhysicalService:
    def __init__(self):
        self.base_url = 'http://openAPI.seoul.go.kr:8088/'
        self.api_key = '58726677796e616b36304542787759'

    def getByNm(self, min: str):
        url = self.base_url + self.api_key + '/xml/ListPublicReservationSport/1/1000/'+min
        html = requests.get(url).text
        names = []
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('CODE').get_text()
        if code == 'INFO-000':
            rows = root.find_all('row')
            for row in rows:
                minClass=row.find('MINCLASSNM').get_text()
                if min == minClass:
                    tat=row.find('SVCSTATNM').get_text()
                    pay = row.find('PAYATNM').get_text()
                    place = row.find('PLACENM').get_text()
                    area = row.find('AREANM').get_text()
                    tel = row.find('TELNO').get_text()

                    names.append(Physical(minClass, tat, pay, place, area, tel))
        else:
            print('오류발생 code:', code)
        return names

    def getFree(self, min:str):
        names = self.getByNm(min)
        freeList = []
        for ph in names:
            if ph.pay=='무료':
                freeList.append(ph)
        return freeList