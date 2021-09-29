import requests
from bs4 import BeautifulSoup
import pandas as pd


# vo
class Education:
    def __init__(self, MINCLASSNM,SVCSTATNM,SVCNM,PAYATNM,PLACENM,USETGTINFO,IMGURL,SVCURL):
        self.MINCLASSNM=MINCLASSNM
        self.SVCSTATNM=SVCSTATNM
        self.SVCNM=SVCNM
        self.PAYATNM=PAYATNM
        self.PLACENM=PLACENM
        self.USETGTINFO=USETGTINFO
        self.IMGURL=IMGURL
        self.SVCURL=SVCURL

# 서버스 : 기능구현, 멤버변수, 메서드
class EduService:
    # 이 클래스의 메서드들이 공통으로 사용하는 값
    def __init__(self):
        self.base_url='http://openAPI.seoul.go.kr:8088/'
        self.api_key='7670445453746a6436386250476b75'
        self.cmd='/xml/ListPublicReservationEducation/1/100/'

    # route_id을 받아서 정보 검색은 open-api에 요청
    # 요청에 대한 응답으로 xml 받음
    # 받음 xml 파싱 -> 정보를 추출 -> vo에 담아서 반환

    # 리스트 출력
    def getInfo(self):
        url = self.base_url+self.api_key+self.cmd
        print(url)
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml') #터미널에 설치 안되어있으면 설치하기
        code = root.find('CODE').get_text()  # 결과코드
        information = []
        if code == 'INFO-000':
            rows = root.find_all('row')  # 배열
            for r in rows:
                MINCLASSNM = r.find('MINCLASSNM').get_text() #소분류명
                SVCSTATNM = r.find('SVCSTATNM').get_text() #서비스상태
                SVCNM = r.find('SVCNM').get_text() #서비스명

                #에러글자 수정
                SVCNM = SVCNM.replace('&#39;', '')
                SVCNM = SVCNM.replace('&quot;', '')
                SVCNM = SVCNM.replace('&uarr;', '')
                SVCNM = SVCNM.replace('&lt;', '')
                SVCNM = SVCNM.replace('&gt;', '')
                SVCNM = SVCNM.replace('& amp;', '')
                SVCNM = SVCNM.replace('&lsquo;', '')
                SVCNM = SVCNM.replace('&rsquo;', '')

                PAYATNM = r.find('PAYATNM').get_text() #결제방법
                PLACENM = r.find('PLACENM').get_text() #장소명
                USETGTINFO = r.find('USETGTINFO').get_text() #서비스대상
                IMGURL = r.find('IMGURL').get_text() #이미지
                SVCURL = r.find('SVCURL').get_text() #바로가기링크
                information.append(Education(MINCLASSNM=MINCLASSNM, SVCSTATNM=SVCSTATNM, SVCNM=SVCNM, PAYATNM=PAYATNM, PLACENM=PLACENM, USETGTINFO=USETGTINFO,
                                                IMGURL=IMGURL, SVCURL=SVCURL))
        else:
            print('오류 발생 code:', code)

        return information

    #무료
    def getInfoFree(self):
        eduInfo = self.getInfo()
        freeList = []
        for e in eduInfo:
            if e.PAYATNM == '무료':
                freeList.append(e)
        return freeList

    #접수중
    def getInfoActive(self):
        eduInfo = self.getInfo()
        activeList = []
        for e in eduInfo:
            if e.SVCSTATNM == '접수중':
                activeList.append(e)
        return activeList

    def getByNow(self):
        newdf = pd.read_csv('static/csv/seoul_edu.csv', encoding='cp949')
        nlist= newdf[newdf['서비스상태'] == '접수중']
        if nlist.empty:
            print('찾을 수 없습니다.')
        else:
            print('현재 접수 중인 프로그램은 총 ', len(nlist),'개 입니다.')
        return len(nlist)

    #분류
    def getByKeywordClass(self, eduInfo, keyword):
        result = []
        if keyword == None:
            return eduInfo
        else:
            for e in eduInfo:
                if keyword in e.MINCLASSNM:
                    result.append(e)
            return result

    #행사
    def getByKeywordSvc(self, eduInfo, keyword):
        result = []
        if keyword == None:
            return eduInfo
        else:
            for e in eduInfo:
                if keyword in e.SVCNM:
                    result.append(e)
            return result

    #장소
    def getByKeywordPlace(self, eduInfo, keyword):
        result = []
        if keyword == None:
            return eduInfo
        else:
            for e in eduInfo:
                if keyword in e.PLACENM:
                    result.append(e)
            return result

    #이용대상
    def getByKeywordTarget(self, eduInfo, keyword):
        result = []
        if keyword == None:
            return eduInfo
        else:
            for e in eduInfo:
                if keyword in e.USETGTINFO:
                    result.append(e)
            return result

    #조건검색
    def getByCondition(self, condition, keyword):
            if condition == 'class':
                eduInfo = self.getInfo()
                result = self.getByKeywordClass(eduInfo, keyword)
            elif condition == 'svc':
                eduInfo = self.getInfo()
                result = self.getByKeywordSvc(eduInfo, keyword)
            elif condition == 'place':
                eduInfo = self.getInfo()
                result = self.getByKeywordPlace(eduInfo, keyword)
            elif condition == 'target':
                eduInfo = self.getInfo()
                result = self.getByKeywordTarget(eduInfo, keyword)
            else:
                print('검색 결과를 찾을 수 없습니다.')
            return result


