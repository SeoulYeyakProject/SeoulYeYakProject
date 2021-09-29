from flask import Blueprint, render_template, request
from models import cul_model as m

bp = Blueprint('cul', __name__, url_prefix='/culture')

service = m.CulService()

@bp.route('/list')
def getList():
    culList = service.getList()
    return render_template('culture/list.html', culList=culList)

@bp.route('/free')
def getFree():
    culList = service.getFree()
    return render_template('culture/list.html', culList=culList)

@bp.route('/ongoing')
def getOngoing():
    culList = service.getOngoing()
    return render_template('culture/list.html', culList=culList)

@bp.route('/map')
def getMap():
    culList = service.getList()
    return render_template('culture/mapK.html', culList=culList)

@bp.route('/search', methods=['POST'])
def search():
    condition = request.form['select1']
    keyword = request.form['keyword']
    culList = service.getByCondition(condition, keyword)
    return render_template('culture/list.html', culList=culList)

