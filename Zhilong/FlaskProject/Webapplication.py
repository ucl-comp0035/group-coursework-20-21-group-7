from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    agencyname ='UCL'
    contactnumber = '+44 (0) 20 7679 2000'
    superlink='https://www.ucl.ac.uk/'
    address='Gower Street,London,United Kingdom'
    imagelink='https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2739117239,1572755614&fm=26&gp=0.jpg'
    return render_template('hello.html',
                           agencyname=agencyname,
                           contactnumber=contactnumber,
                           address=address,
                           imagelink=imagelink,
                           superlink=superlink
                           )
if __name__ == '__main__':
    app.run(port=5002,debug=True)