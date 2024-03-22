from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts/')
def contacts():
    #Где взяли данные
    developer_name = 'ssa'
    developer_home = 'chebocsar'

    return render_template('contacts.html', name=developer_name, home=developer_home)
@app.route('/register/')
def register():


    return render_template('register.html')




if __name__ == '__main__':
    app.run(debug=True)
