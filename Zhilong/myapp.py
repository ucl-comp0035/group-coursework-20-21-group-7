from flask import Flask
from flask import render_template #渲染

app=Flask(__name__)
@app.route('/') #主页地址，装饰器
def news():
    the_news = {
        'Dayou':'全栈工程师',
        'Zhilong':'勇敢的打工人',
        'Aileen':'网页架构师',
        'Wenteng':'项目经理',
        'John':'团队甲方',
    }
    context={
        'title':'小组007',
        'the_news': the_news,
    }
    return render_template('index.html',context=context)#读取index.html并交给浏览器

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=80)#127.0.0.1 回路，自己返回自己
