import math
import sqlite3


from flask import Flask, request, render_template, redirect, Blueprint,session


from models import edu_models as edu
service = edu.EduService()

bp = Blueprint('edu', __name__, url_prefix='/edu')

# @bp.route('/edu-info', methods=['POST'])
# def edu_info():
#     MINCLASSNM = request.form['MINCLASSNM']
#     edu = service.getInfoByMinClass(MINCLASSNM=MINCLASSNM)
#     return render_template('edu/eduinfo.html', edu=edu)

@bp.route('/eduinfo')
def getInfo():
    eduInfo = service.getInfo()
    return render_template('edu/eduinfo.html', eduInfo=eduInfo)

@bp.route('/free')
def getFree():
    eduInfo = service.getInfoFree()
    return render_template('edu/eduinfo.html', eduInfo=eduInfo)

@bp.route('/active')
def getOngoing():
    eduInfo = service.getInfoActive()
    return render_template('edu/eduinfo.html', eduInfo=eduInfo)

@bp.route('/eduinfo')
def getNow():
    nlist = service.getByNow()
    return render_template('edu/eduinfo.html', nlist=nlist)

@bp.route('/search', methods=['POST'])
def search():
    condition = request.form['condition']
    keyword = request.form['keyword']
    eduInfo = service.getByCondition(condition, keyword)
    return render_template('edu/eduinfo.html', eduInfo=eduInfo)


@bp.route("/edu-info")
def board_list():
    board = mongo.db.board
    # 페이지 값 (디폴트값 = 1)
    page = request.args.get("page", 1, type=int)
    # 한 페이지 당 몇 개의 게시물을 출력할 것인가
    limit = 20
    datas = board.find({}).skip((page - 1) * limit).limit(limit)  # board컬럭션에 있는 모든 데이터를 가져옴
    # 게시물의 총 개수 세기
    tot_count = board.find({}).count()
    # 마지막 페이지의 수 구하기
    last_page_num = math.ceil(tot_count / limit) # 반드시 올림을 해줘야함

    # 페이지 블럭을 5개씩 표기
    block_size = 5
    # 현재 블럭의 위치 (첫 번째 블럭이라면, block_num = 0)
    block_num = int((page - 1) / block_size)
    # 현재 블럭의 맨 처음 페이지 넘버 (첫 번째 블럭이라면, block_start = 1, 두 번째 블럭이라면, block_start = 6)
    block_start = (block_size * block_num) + 1
    # 현재 블럭의 맨 끝 페이지 넘버 (첫 번째 블럭이라면, block_end = 5)
    block_end = block_start + (block_size - 1)
    return render_template("edu/eduinfo.html", datas=datas,limit=limit,page=page,block_start=block_start,block_end=block_end,last_page_num=last_page_num)

# @bp.route('/edu-info', methods=['POST'])
# def edu_info():
#     MINCLASSNM = request.form['MINCLASSNM']
#     SVCSTATNM = request.form['SVCSTATNM']
#     SVCNM = request.form['SVCNM']
#     PAYATNM = request.form['PAYATNM']
#     PLACENM = request.form['PLACENM']
#     USETGTINFO = request.form['USETGTINFO']
#     edu = service.getInfoByMinClass(MINCLASSNM=MINCLASSNM, SVCSTATNM=SVCSTATNM, SVCNM=SVCNM, PAYATNM=PAYATNM,
#                                     PLACENM=PLACENM,USETGTINFO=USETGTINFO)
#     return render_template('edu/eduinfo.html', edu=edu)


# @bp.route('/route-path', methods=['POST'])
# def route_path():
#     routeid = request.form['routeid']
#     stList:list = service.getStListByRouteId(routeId=routeid)
#     return render_template('bus/stationList.html', stList=stList, routeid=routeid)
#
# @bp.route('/graph')
# def graph():
#     img_path = 'static/graph/my_plot.png'
#
#     x = [1, 2, 3, 4]
#     y = [3, 8, 5, 6]
#     fig, ax = plt.subplots()
#     plt.plot(x, y)
#     fig.savefig(img_path)
#     img_path = '/' + img_path
#     return render_template('bus/graph.html', img_path=img_path)