from flask import Flask, request, render_template, redirect

import routes.space_route as sp
import routes.edu_routes as er
app = Flask(__name__)

#블루프린트 객체 생성
app.register_blueprint(sp.bp)
app.register_blueprint(er.bp)



@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
