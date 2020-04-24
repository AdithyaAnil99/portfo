from flask import Flask,render_template,redirect,request,send_from_directory
import csv
app = Flask(__name__)

#This opens the initial starting page
@app.route('/')
def index():
    return render_template('./index.html')

#To dynamically accept the url
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_func(data):
	with open('database.txt','a') as file:
		file.write('\n*****************************')
		name=data['name']
		email=data['email']
		file.write(f'\nName:{name},Email:{email}\n')
		file.write('*****************************\n')

def write_csv(data):
	with open('database.csv',newline='',mode='a') as file1:
		name=data['name']
		email=data['email']
		subject=data['subject']
		csv_writer= csv.writer(file1, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,subject])
	


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data=request.form.to_dict()
    	write_csv(data)
    	return redirect('thankyou.html')
    else:
    	return 'something is wrong .... try again'