from flask import Flask, request, render_template, redirect, Blueprint
import models.ph_model as mo

bp = Blueprint('ph', __name__, url_prefix='/ph')

service = mo.PhysicalService()

@bp.route('/phinfo', methods=['POST'])
def route_info():
    minClass = request.form['minClass']
    ph:list = service.getByNm(min=minClass)
    return render_template('ph/phinfo.html', names=ph)

@bp.route('/free/<string:min>')
def getFree(min):
    print(min)
    names = service.getFree(min)
    return render_template('ph/phinfo.html', names=names)

@bp.route('/phmain')
def phMain():
    return render_template('ph/phmain.html')