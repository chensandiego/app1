from application import app



@app.route('/')
def hello():
    return 'hello world'



@app.route('/contact')
def contact():
	return 'you can reach me at 555-5555,or email me at test@example.com'

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method =='POST':
		#logic for handling login
		pass
	else:
		#display login form
		pass
