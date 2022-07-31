from flask import Flask, render_template, redirect, url_for, request, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, SelectField, IntegerField, HiddenField, DateField, TimeField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from datetime import datetime
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
from datetime import datetime


app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:batata@localhost/database1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vmfbelplxyvepj:a2979b6807823c413e08a119955da592e94ab4f38696d568553ef3b11dbac674@ec2-54-87-179-4.compute-1.amazonaws.com:5432/deljs855e01f1t'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'FW3434ff545h4RFE55$#f$t%yhtFF'

db = SQLAlchemy(app)

#Flask_login Stuff

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#functions
#def send(message):
#    now = datetime.now()
#    nowlst = str(now).split()
#    time = nowlst[1]
#    timelst = time.split(":")
#    hour = int(timelst[0])
#    min = int(timelst[1])
#    pwt.sendwhatmsg("+96170594811", message, hour, min+2)


#def generate_key():
#    encrypting_key = Fernet.generate_key()
#    file = open("key_file.key", "wb")
#    file.write(encrypting_key)
#    file.close()

def encrypt(data):
    #open_file = open(".key_file.key", "rb")
    #key = open_file.read()
    key = b'kaYShGLbw1PD58npID1sf_mwnnVO4nmehsq5RNAro_I='
    encoded_data = data.encode()
    ferneted_key = Fernet(key)
    encrypted_data = ferneted_key.encrypt(encoded_data)
    #key.close()
    return encrypted_data

def decrypt(encrypted_data):
    #open_file = open(".key_file.key", "rb")
    #key = open_file.read()
    key = b'kaYShGLbw1PD58npID1sf_mwnnVO4nmehsq5RNAro_I='
    ferneted_key = Fernet(key)
    decrypted_data = ferneted_key.decrypt(encrypted_data)
    data = decrypted_data.decode()
    #key.close()
    return data

#Sqlalchemy classes


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    staff_type = db.Column(db.String)

    def __init__(self, name, surname, username, email, password_hash, staff_type):
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password_hash)
        self.staff_type = staff_type
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)

class AdhaActivitiesRating(db.Model):
    __tablename__ = "AdhaActivitiesRating"
    id = db.Column(db.Integer, primary_key=True)
    starting_date_time = db.Column(db.String) #note that in form start date time are separated but in database are combined(no time data type in mysql)
    finishing_date_time = db.Column(db.String)
    gps_location = db.Column(db.String)
    governorate = db.Column(db.String)    
    location = db.Column(db.String) 
    its_name = db.Column(db.String) 
    p_code = db.Column(db.String)
    nb_of_families = db.Column(db.Integer)
    activity_type = db.Column(db.String)
    if_other_type = db.Column(db.String) 
    donor = db.Column(db.String)
    team_leader = db.Column(db.Integer)
    targeted_nb_in_camp = db.Column(db.Integer)
    distributed_items = db.Column(db.Integer)
    nb_of_itmes_to_be_distributed_in_this_act = db.Column(db.Integer)
    exists_of_written_scheduled = db.Column(db.Integer)
    voucher_distributed = db.Column(db.Integer)
    beneficiaries_list_ready_used = db.Column(db.Integer)
    protect_policies_respect_rate = db.Column(db.Integer)
    controllcing_workplacce_rate = db.Column(db.Integer)
    commitment_to_Covid_precautions = db.Column(db.Integer)
    existing_of_requicrements = db.Column(db.Integer)
    if_shortcoming_in_requirements = db.Column(db.String)
    randomly_checked_item_rate = db.Column(db.Integer)
    staff_performance = db.Column(db.Integer)
    general_notes = db.Column(db.String)
   
    def __init__(self, starting_date_time, finishing_date_time, gps_location, governorate, location, its_name, p_code, nb_of_families, activity_type, if_other_type, donor, team_leader, targeted_nb_in_camp, distributed_items, 
    nb_of_itmes_to_be_distributed_in_this_act, exists_of_written_scheduled, voucher_distributed, beneficiaries_list_ready_used,
    protect_policies_respect_rate, controlling_workplacce_rate, commitment_to_Covid_precautions, existing_of_requirements,
     if_shortcoming_in_requirements, randomly_checked_item_rate, staff_performance, general_notes):
        self.starting_date_time = starting_date_time
        self.finishing_date_time = finishing_date_time
        self.gps_location = gps_location
        self.governorate = governorate
        self.location = location
        self.its_name = its_name
        self.p_code = p_code
        self.nb_of_families = nb_of_families
        self.activity_type = activity_type
        self.if_other_type = if_other_type
        self.donor = donor
        self.team_leader = team_leader
        self.targeted_nb_in_camp = targeted_nb_in_camp
        self.distributed_items = distributed_items
        self.nb_of_itmes_to_be_distributed_in_this_act = nb_of_itmes_to_be_distributed_in_this_act
        self.exists_of_written_scheduled = exists_of_written_scheduled
        self.voucher_distributed = voucher_distributed
        self.beneficiaries_list_ready_used = beneficiaries_list_ready_used
        self.protect_policies_respect_rate = protect_policies_respect_rate
        self.controlling_workplacce_rate = controlling_workplacce_rate
        self.commitment_to_Covid_precautions = commitment_to_Covid_precautions
        self.existing_of_requirements = existing_of_requirements
        self.if_shortcoming_in_requirements = if_shortcoming_in_requirements
        self.randomly_checked_item_rate = randomly_checked_item_rate
        self.staff_performance = staff_performance
        self.general_notes = general_notes
        
#Forms classes:

class RegisterForm(FlaskForm):
    name = StringField('Name', [InputRequired(), Regexp(r'^[A-Za-z\s\-\']+$', message='Invalid location!'),
        Length(min=3, max=20, message="The name length should be between 3 and 20")])
    surname = StringField('Surname', [InputRequired(), Regexp(r'^[A-Za-z\s\-\']+$', message='Invalid location!'),
        Length(min=3, max=20, message="The name length should be between 3 and 20") ])
    username = StringField('Username',[InputRequired(), Regexp(r'^[A-Za-z\s\-\']+$', message='Invalid location!'),
        Length(min=5, max=20, message="The name length should be between 5 and 20") ])
    email = StringField('Email', [InputRequired(), Regexp(r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', message="Invalid email")])
    password = PasswordField('Password', [InputRequired(), Length(min=8, max=16, message="No more than 16 No less than 8")])
    #staff_type = SelectField('Staff type', [InputRequired()], choices=[('', ''), ('admin', 'Admin'), ('data_entry', 'Data Entry')])
    submit = SubmitField()

class loginform(FlaskForm):
    username = StringField('إسم المستخدم',[InputRequired()])
    password = PasswordField('كلمة المرور',[InputRequired()])

class AdhaActivities(FlaskForm):
    id_field = HiddenField()
    starting_date = DateField('تاريخ بدء التنفيذ/Execution starting date', [InputRequired(),
     Regexp(r'/^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$/', message='The date format should be YYYY-MM-DD')])
    #starting_time = TimeField('موعد بدء التنفيذ/Execution starting time', [InputRequired(), Regexp(r'^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$',
     #message='The time format should be HH:MM:SS')])
    #dont forget date time
    governorate = SelectField('المحافظة/Governorate', [InputRequired()], choices=[('', ''), ('baalbek-hermel', 'بعلبك الهرمل'), ('bekaa', 'البقاع'), ('akkar', 'عكار'),
     ('saida', 'صيدا'), ('alshamal', 'الشمال'), ('beirut', 'بيروت'), ('jabal_lobnan', 'جبل لبنان'), ('alnabatiyeh', 'النبطية'), ('aljanoub', 'الجنوب')])
    location = StringField('المنطقة/location', [InputRequired(), Regexp(r'^[A-Za-z\s\-\']+$', message='Invalid location!'), 
            Length(min=8, max=70, message='The location length should be between 8 and 70')])
    its_name = StringField('إسم المخيم/ITS Name', [InputRequired(), Regexp(r'^[A-Za-z\s\-\']+$', message='Invalid ITS Name!'), 
            Length(min=2, max=35, message='The ITS name length should be between 2 and 35')])
    p_code = StringField('كود المخيم/P Code', [InputRequired(), Length(min=2, max=5, message='The P-code length should be between 2 and 5')])
    #GPS location I should use location API of HTML5
    nb_of_families = IntegerField('عدد العائلات/Nb. Of Families', [InputRequired(), NumberRange(min=5, max=5000, message="The nb. of families should be between 5 and 5000")])
    activity_type = SelectField('نوع النشاط/Activity Type', [InputRequired()], choices=[('', ''), ('food_items', 'حصص غذائية/Food Items'), ('clothes', 'ألبسة/Clothes'), 
    ('iftar_meal', 'وجبة إفطار/Iftar Meal'), ('eid_festival', 'مهرجان للعيد/Eid Festival'),
     ('adha_food_item', 'حصص من الأضاحي/Adha Food Items'), ('hygiene_kits', 'حصص نظافة/Hygiene Kits'), ('others', 'غيره/Others')])
    if_other_type = StringField('حدد نوع النشاط إن لم يكن ضمن القائمة', [Regexp(r'^[A-Za-z\s\-\']+$', message='Invalid activity type!'), 
                    Length(min=2, max=35, message='The avtivity type length should be between 2 and 35')])
    donor = StringField('الجهة المانحة/Donor', [InputRequired(), Regexp(r'^[A-Za-z\s\-\']+$', message='Invalid donor name!'), 
            Length(min=2, max=35, message='The donor name length should be between 2 and 35')])
    team_leader = StringField('المسؤول عن الفريق/Team Leader', [InputRequired(), Regexp(r'^[A-Za-z\s\-\']+$', message='Invalid name!'), 
            Length(min=2, max=35, message='The name length should be between 2 and 35')])
    targeted_nb_in_camp = IntegerField('الهدف الكلي في هذا المخيم/Overall target in this camp', [InputRequired(), NumberRange(min=50, max=25000, message="The overall target should be between 50 and 25000") ])
    distributed_items = IntegerField('عدد الحصص الموزع/Distributed items Count',[InputRequired(), NumberRange(min=50, max=25000, message="The overall target should be between 50 and 25000")])
    nb_of_itmes_to_be_distributed_in_this_act = IntegerField('عدد الحصص التي سيتم توزيعها في هذا النشاط/Nb. Of Items To Be Distributed In This Activity', [InputRequired(), NumberRange(min=50, max=25000, message="The overall target should be between 50 and 25000")] )
    exists_of_written_scheduled = SelectField('Written schedule exists that was approved by the sector management/تم التأكّد من وجود جدول منظم للأنشطة موافق عليه من إدارة القطاع؟', [InputRequired(message="Please input!")], choices=[('', ''), (1, 'نعم'), (0, 'كلا')])
    voucher_distributed = SelectField('The vouchers were distributed before the activity | هل تم توزيع بونات قبل تنفيذ النشاط؟ ', [InputRequired(message="Please input!")], choices=[('', ''), (1, 'نعم'), (0, 'كلا')])
    beneficiaries_list_ready_used = SelectField('Family lists are ready and used during distribution| هل يوجد قوائم المستفيدين وتمت الاستعانة بها خلال التوزيع ', [InputRequired(message="Please input!")], choices=[('', ''), (1, 'نعم'), (0, 'كلا')] )
    existing_of_requirements = SelectField('All requirements related to distribution are in the place |التأكد من وجود كافة لوازم التنفيذ اللوجستية وغيرها في المكان', [InputRequired(message="Please input!")], choices=[('', ''), (1, 'نعم'), (0,'كلا')])
    if_shortcoming_in_requirements = StringField('حدد اللوازم الناقصة إن وُجِدَت.', [Length(min=0, max=100, message='The explanation length should be between 0 and 100') ])
    general_notes = StringField('ملاحظات/Notes', [InputRequired(), Length(min=0, max=150, message='The explanation length should be between 0 and 150')])
    submit = SubmitField(' إضافة ')

class Main_Records(FlaskForm):
    id_field = HiddenField()

#functions

def finish_datetime():
    finish_datetime = datetime.now()
    return finish_datetime

# routes
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginform()
    if form.validate_on_submit():
        req_username = request.form["username"]
        #enc_requested_email = encrypt(req_email)
        username = Users.query.filter_by(username=req_username).first()
        password = request.form['password']
        if username:
            if username.verify_password(password):
                login_user(username)
                flash("تم تسجيل الدخول بنجاح")
                return redirect(url_for("welcome"))
            else:
                flash("كلمة المرور غير صحيحة!")
        else:
            flash("البريد الإلكتروني غير صحيح")
    return render_template('login.html', form=form)

@app.route('/admin/register', methods=['POST', 'GET'])
@login_required
def register():
    id = current_user.id
    if id == 3:
        form = RegisterForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                name = request.form["name"]
                surname = request.form["surname"]
                username = request.form["username"]
                email = request.form["email"]
                password = request.form["password"]
                enc_name = encrypt(name)
                enc_surname = encrypt(surname)
                #enc_username = encrypt(username)
                enc_email = encrypt(email)
                record = Users(enc_name, enc_surname, username, enc_email, password, staff_type="")
                db.session.add(record)
                db.session.commit()
                flash("The new user has been added successfully")
                return redirect(url_for('register'))
            else:
                return render_template("register.html", form=form, cu_id=id)
        else:
            return render_template("/data_entry/register.html", form=form, cu_id=id)
    #message = "An error occured try to logout then login again"
    return redirect(url_for("welcome"))


@app.route('/')
@login_required
def welcome():
    cu_id = current_user.id
    cu_enc_username = current_user.username
    #message = f"The user {cu_enc_username} has logged in to the system"
    #send(message)
    #time.sleep(150)
    #return render_template("index.html", cu_id=cu_id)
    return render_template("departmentsnavigation.html", cu_id=cu_id)

@app.route('/Ba3dayn_bsewihoun')
@login_required
def welcome_mo2akkate():
    return "<h1> hello this is under development</h1>"

@app.route('/DataEntry')
@login_required
def de_welcome():
    cu_id = current_user.id
    return render_template("/indexes/de_index.html", cu_id=cu_id)

@app.route('/Graphs_Statistics')
@login_required
def gs_welcome():
    cu_id = current_user.id
    return "<h1>Hello this is under development</h1>"

@app.route("/A_A_R", methods=['GET', 'POST'])
@login_required
def A_A_R():
    cu_id = current_user.id
    form1 = AdhaActivities()
    if request.method == 'POST':
        if form1.validate_on_submit:
            #date_time_start_should_be_cobining_2_request
        #date_time_of_finish_sshould_be_taken_from_a_function
        #gps_location_should_be_taken_auto
            starting_date = request.form["starting_date"]
            #starting_date = "2020-11-22" 
            #starting_time = request.form["starting_time"]
            starting_time = "11:11:11.321333"
            starting_datetime = starting_date + "," + starting_time
            finish_date_time = finish_datetime()
            governorate = request.form['governorate']
            location = request.form['location']
        #gps = request.form["gps"] #la 7atta ysir l site taba3e https la tsir tshti8il l gps
            gps = "12.123123,88,312342"
            its_name = request.form['its_name']
            p_code = request.form['p_code']
            nb_of_families = request.form['nb_of_families']
            activity_type = request.form['activity_type']
            if_other_type = request.form['if_other_type']
            donor = request.form['donor']
            team_leader = request.form['team_leader']
            targeted_nb_in_camp = request.form['targeted_nb_in_camp']
            distributed_items = request.form['distributed_items']
            nb_of_itmes_to_be_distributed_in_this_act = request.form['nb_of_itmes_to_be_distributed_in_this_act']
            exists_of_written_scheduled = request.form['exists_of_written_scheduled']
            voucher_distributed = request.form['voucher_distributed']
            beneficiaries_list_ready_used = request.form['beneficiaries_list_ready_used']
            protect_policies_respect_rate = request.form['pprr']
            #protect_policies_respect_rate = 7
            controlling_workplacce_rate = request.form["controlling_workplacce_rate"]
            commitment_to_covid_precautions = request.form["commitment_to_covid_precautions"]
            #controlling_workplacce_rate = 10
            #commitment_to_covid_precautions = 4
            existing_of_requirements = request.form['existing_of_requirements'] #tawejoud l ma3added wl mostalzamet llojistiyye
            if_shortcoming_in_requirements = request.form['if_shortcoming_in_requirements'] #iza fi nawa2es bl mostalzamet
            randomly_checked_item_rate = request.form["randomly_checked_item_rate"]
            #randomly_checked_item_rate = 8
            staff_performance = request.form["staff_performance"]
            #staff_performance = 7
            general_notes = request.form['general_notes']
            record = AdhaActivitiesRating(starting_datetime, finish_date_time, gps, governorate, location, its_name, p_code, nb_of_families, activity_type, if_other_type, donor, team_leader, targeted_nb_in_camp, distributed_items, nb_of_itmes_to_be_distributed_in_this_act,
        exists_of_written_scheduled, voucher_distributed, beneficiaries_list_ready_used, protect_policies_respect_rate, controlling_workplacce_rate,
        commitment_to_covid_precautions, existing_of_requirements, if_shortcoming_in_requirements, randomly_checked_item_rate,
        staff_performance, general_notes)
            db.session.add(record)
            db.session.commit()
            flash("لقد تمت إضافة المعلومات بنجاح!")
            #form1.data = ""
            form1.activity_type.data = ''
            return redirect(url_for("A_A_R"))
        else:
            for field, errors in form1.errors.items():
                for error in errors:
                    flash("Error in {}: {}".format(
                        getattr(form1, field).label.text,
                        error
                        ), 'error')
                    message = "Error in {}: {}".format(
                        getattr(form1, field).label.text,
                        error
                        )#, 'error'
            return render_template("/data_entry/adhaactrating.html", form=form1, cu_id=cu_id, message=message)
    return render_template("/data_entry/adhaactrating.html", status4="active", form=form1, cu_id=cu_id)

@app.route('/data_entry/main_records', methods=['POST', 'GET'])
@login_required
def main_records():
    form = Main_Records()
    if request.method == 'POST':
        name = request.form["name"]
        mobile_nb = request.form["mobile_number"]
        phone_nb = request.form["phone_nb"]
        city = request.form["city"]
        address = request.form["address"]
        family_master_relation = request.form["family_master_relation"] #silat lli 3am ne5od menno l ma3loumet b rab l 2osra
        family_father_exists = request.form["family_father_exists"]
        family_mother_exists = request.form["family_mother_exists"]
        family_count = request.form["family_count"]
        family_adults_count = request.form["family_adults_count"]
        family_children_count = request.form["family_children_count"]
        family_kids_girls_count = request.form["family_kids_girls_count"]
        family_married_kids_count = request.form["family_married_kids_count"]
        # = request.form[""] #t5ab3out l up down
        wrorking_member = request.form["field_1611230997"] #who is working actually from the family members
        more_info = request.form["field_1611235066"] #more info about working member
        members_btw_0_4 = request.form["field_1612518121"]
        members_btw_5_8 = request.form["field_1612518141"]
        members_btw_9_13 = request.form["field_1612518165"]
        members_btw_14_18 = request.form["field_1612518219"]
        members_btw_19_25 = request.form["field_1612518623"]
        members_btw_26_50 = request.form["field_1612518638"]
        members_btw_51_64 = request.form["field_1612518659"]
        members_above_64 = request.form["field_1612518673"]
        nationality = request.form["field_1617714362"] 
        #new tab about حالة عقد الزواج
        #we can include them in a separete table
        marriage_contract_status = request.form["marriage_contract_status"]
        marriage_contract_level = request.form["marriage_contract_level"]
        contract_unregistered_causes = request.form["contruct_unregistered_causes"]
        children_registered = request.form["children_registered"]
        child_reg_place = request.form["child_reg_place"]
        challanges_no_contract = request.form["challanges_no_contract"]
        helps_source = request.form["helps_source"]
        helps_duration = request.form["helps_duration"]
        urda_using = request.form["urda_using"]
        urda_using_enough = request.form["urda_using_enough"]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        #= request.form[""]
        print(name, phone_nb)
        return redirect(url_for("main_records"))
    return render_template("mainrecords.html", form=form)



@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    flash("تم تسجيل الخروج")
    return redirect(url_for("login"))

@app.route('/admin/cookies')
def cookies():
    id = current_user.id
    role = ""
    if id == 3:
        role = "admin"
    else:
        role = "normaluser"
    res = make_response("Cookies", 200)
    res.set_cookie(str(id), value=role,
    max_age=36000,
    expires=None,
    path=request.path,
    secure=True
    )
    return res

if __name__ == "__main__":
    app.run(debug=True, ssl_context='adhoc')