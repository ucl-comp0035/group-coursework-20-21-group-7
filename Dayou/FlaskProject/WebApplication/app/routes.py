#导入模板模块
from flask import render_template,flash,redirect
from app import app
from app.form import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Visitor'}
    posts = [
        {
            'author':{'username':'John Rambo'},
            'body':'This stock graph is really helpful'

        },
        {
            'author': {'username': 'Ferrari_430'},
            'body': 'Of course'
        }
    ]
    return render_template('index.html',title='Index',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Your Username is:{} , Remember me:{}'.format(
            form.username.data,form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Log In',form=form)

@app.route('/news')
def newspage():
    newsContent="10月19日消息，早盘指数悉数高开，随后指数相继冲高回落，\
    其中沪指一度涨1%，但好景不长，创指率先翻绿。盘面上，大金融、玉米等农业股\
    早盘表现强势，煤炭概念出现回调，量子通信概念全线大涨，军工板块再度走强。\
    个股总体涨多跌少，资金指数小幅高开，炸板率逐渐走高。临近午盘，三大指数全线翻绿。"
    return render_template("news.html",title='News',data=newsContent)
