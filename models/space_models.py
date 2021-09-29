import requests
from bs4 import BeautifulSoup

class Space:
    def __init__(self, svcid =None, svcstatnm=None, maxclassnm=None, minclassnm=None, placenm=None, payatnm=None, svcurl=None, rcptbgndt=None, rcptenddt=None, areanm=None, telno=None, v_min=None, v_max=None, imgurl=None, x=None, y=None):
        self.svcid = svcid
        self.svcstatnm = svcstatnm #서비스상태
        self.maxclassnm = maxclassnm #대분류명
        self.minclassnm = minclassnm #소분류명
        self.placenm = placenm #장소명
        self.payatnm = payatnm #결제방법
        self.svcurl = svcurl #바로가기URL
        self.rcptbgndt = rcptbgndt #접수시작일시
        self.rcptenddt = rcptenddt #접수종료일시
        self.areanm = areanm #지역명
        self.telno = telno #전화번호
        self.v_min = v_min #서비스이용 시작시간
        self.v_max = v_max #서비스이용 종료시간
        self.imgurl = imgurl
        self.x = x
        self.y = y

class SpaceService:
    def __init__(self):
        self.base_url = 'http://openapi.seoul.go.kr:8088/456d59434a686172383748774f4441/xml/ListPublicReservationInstitution/1/70'

    def getSpaceList(self):
        url = 'http://openapi.seoul.go.kr:8088/456d59434a686172383748774f4441/xml/ListPublicReservationInstitution/1/70'
        result = requests.get(url)
        soup = BeautifulSoup(result.text, 'lxml')

        items = soup.find_all("row")
        spaceList = []

        for root in items:
            svcid = root.find('svcid').string
            svcstatnm = root.find('svcstatnm').string
            maxclassnm = root.find('maxclassnm').string
            minclassnm = root.find('minclassnm').string
            placenm = root.find('placenm').string
            payatnm = root.find('payatnm').string
            svcurl = root.find('svcurl').string
            rcptbgndt = root.find('rcptbgndt').string
            rcptenddt = root.find('rcptenddt').string
            areanm = root.find('areanm').string
            telno = root.find('telno').string
            v_min = root.find('v_min').string
            v_max = root.find('v_max').string
            imgurl = root.find('imgurl').string
            x = root.find('x').string
            y = root.find('y').string

            spaceList.append(Space(svcid=svcid, svcstatnm=svcstatnm, maxclassnm=maxclassnm, minclassnm=minclassnm,
                                   placenm=placenm, payatnm=payatnm, svcurl=svcurl, rcptbgndt=rcptbgndt,
                                   rcptenddt=rcptenddt, areanm=areanm, telno=telno, v_min=v_min, v_max=v_max,
                                   imgurl=imgurl, x=x, y=y))
        return spaceList

    def search(self, userSearch):
        spaceList = self.getSpaceList()
        searchList = []

        for s in spaceList:
            if userSearch in s.placenm:
                searchList.append(s)

        return searchList

    def areaSearch(self, area):
        spaceList = self.getSpaceList()
        searchList = []

        for s in spaceList:
            if area in s.areanm:
                searchList.append(s)

        return searchList

    def spaceType(self, type):
        spaceList = self.getSpaceList()
        searchList = []

        for s in spaceList:
            if type in s.minclassnm:
                searchList.append(s)

        return searchList

    def getSpaceDetail(self, svcid):
        spaceList = self.getSpaceList()
        searchList = []

        for s in spaceList:
            if svcid in s.svcid:
                searchList.append(s)

        return searchList