from flask import Flask, request, render_template, redirect, Blueprint
import models.space_models as sp

bp = Blueprint('space', __name__, url_prefix='/space')
service = sp.SpaceService()

#리스트 출력
@bp.route('/list')
def space_list():
    spaceList = service.getSpaceList()
    return render_template('space/space_home.html', spaceList=spaceList)

#검색 : 장소명
@bp.route('/search', methods=['POST'])
def search():
    userSearch = request.form['userSearch']
    spaceList = service.search(userSearch)

    return render_template('space/space_home.html', spaceList=spaceList)

#검색 : 지역
@bp.route('/AreaSearch', methods=['POST'])
def AreaSearch():
    area = request.form['area']
    spaceList = service.areaSearch(area)

    return render_template('space/space_home.html', spaceList=spaceList)

#검색 : 타입
@bp.route('/spaceType', methods=['POST'])
def spaceType():
    type = request.form['type']
    spaceList = service.spaceType(type)

    return render_template('space/space_home.html', spaceList=spaceList)

#지도
@bp.route('/detail/<string:svcid>')
def detail(svcid):
    spaceList = service.getSpaceDetail(svcid)
    return render_template('space/space_map.html', spaceList=spaceList)