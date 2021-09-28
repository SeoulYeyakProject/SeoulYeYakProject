from flask import Flask, request, render_template, redirect
import routes.space_route as sp

app = Flask(__name__)

#블루프린트 객체 생성
app.register_blueprint(sp.bp)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()