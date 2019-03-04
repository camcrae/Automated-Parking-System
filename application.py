'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Flask, render_template, request
from application import db
from application.models import Customer, Reservation
from application.forms import EnterDBInfo, RetrieveDBInfo
from application.forms import EnterFirstName, EnterLastName, EnterVehicleInfo, EnterEstimatedDuration

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'   


@application.route('/', methods=['GET', 'POST'])
@application.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@application.route('/checkin', methods=['GET', 'POST'])
def checkin():
    form1 = EnterFirstName(request.form)
    form2 = EnterLastName(request.form)
    form3 = EnterVehicleInfo(request.form)
    form4 = EnterEstimatedDuration(request.form)

    if request.method == 'POST' and form1.validate() and form2.validate() and form3.validate() and form4.validate():
        data_entered = Customer(notes=form1.dbNotes.data)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return render_template('parking.html', notes=form1.dbNotes.data)

    return render_template('checkin.html', form1=form1, form2=form2, form3=form3, form4=form4)


@application.route('/parking', methods=['GET', 'POST'])
def parking():
    return render_template('parking.html')



if __name__ == '__main__':
    application.run(host='0.0.0.0')
