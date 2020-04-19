
from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)


# @app.route('/')
# def hello_world():
#     return 'maink'

@app.route('/index.html')
def my_home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/works.html')
def works():
    return render_template('works.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/thank_you.html')
def thanks():
    return render_template('thank_you.html')


# def write_to_file(data):
#     with open('database.txt', mode='a') as database2:
#         email = data["email"]
#       #  subject = data["subject"]
#         message = data["message"]
#         file = database2.write(f'\n{email},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
      #  subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thank_you.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
