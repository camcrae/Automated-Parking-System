from flask.ext.wtf import Form
from wtforms import StringField, validators

class EnterFirstName(Form):
    fn = StringField(label="First Name: ", description="fn_enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])

class EnterLastName(Form):
    ln = StringField(label="Last Name: ", description="fn_enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])

class EnterVehicleInfo(Form):
    vInfo = StringField(label="Car Year/Make/Model/Color", description="v_enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])

class EnterEstimatedDuration(Form):
    dur = StringField(label="Estimated Parking Duration", description="dur_enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])

class EnterDBInfo(Form):
    dbNotes = StringField(label='Items to add to DB', description="db_enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])

class RetrieveDBInfo(Form):
    numRetrieve = StringField(label='Number of DB Items to Get', description="db_get", validators=[validators.required(), validators.Regexp('^\d{1}$', message=u'Enter a number between 1 and 10')])
