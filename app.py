from flask import Flask, request, render_template, redirect
<<<<<<< Updated upstream
import routes.space_route as sp

app = Flask(__name__)

#블루프린트 객체 생성
app.register_blueprint(sp.bp)
=======
import routes.edu_routes as er

app = Flask(__name__)

app.register_blueprint(er.bp)
>>>>>>> Stashed changes

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
<<<<<<< Updated upstream
    app.run()
=======
    app.run()#flask 서버 실행
>>>>>>> Stashed changes
