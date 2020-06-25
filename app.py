from flask import Flask, request, render_template, redirect, url_for, abort
app = Flask(__name__)

@app.route('/')
def index():
    return "메인페이지"

@app.route('/hello')
def hello():
    return 'Hello, world!'



@app.route('/hello/<name>')
def hellovar(name):
    return 'Hello, {}'.format(name)


@app.route('/input/<int:num>')    
def input(num):
    name =''
    if num == 1:
        name = '도라에몽'
    elif num == 2:        
        name = '진구'
    elif num ==3:
        name = '퉁퉁이'
    else:
        return "없어요"
    return "hello {}".format(name)


@app.route('/naver')    
def naver():
    return render_template("naver.html")

@app.route('/daum')
def daum():
    return redirect("https://www.daum.net/")

@app.route('/move/daum')
def url_test():
    return redirect(url_for('daum'))


@app.route('/move/naver')
def url_test2():
    return redirect(url_for('naver'))


@app.route('/img')
def img():
    return render_template("image.html")

@app.route('/urltest')
def url_test3():
    return redirect(url_for('naver'))

@app.route('/move/<site>')    
def move_site(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'daum':
        return redirect(url_for('daum'))
    else: 
        return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL을 확인하세요." , 404


if __name__ == '__main__':
    # with app.test_request_context():
        # print(url_for('daum'))
        # print(url_for('naver'))
    app.run(debug=True)


