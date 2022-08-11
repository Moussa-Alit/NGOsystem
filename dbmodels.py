from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask import Flask
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vmfbelplxyvepj:a2979b6807823c413e08a119955da592e94ab4f38696d568553ef3b11dbac674@ec2-54-87-179-4.compute-1.amazonaws.com:5432/deljs855e01f1t'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    date_added = db.Column(db.DateTime)
    date_edited = db.Column(db.DateTime)

    def __init__(self, name, surname, username, email, password_hash, date_added, date_edited):
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password_hash)
        self.date_added = date_added
        self.date_edited = date_edited
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)

class AdhaActivitiesRating(db.Model):
    __tablename__ = "adhaactsrating"
    id = db.Column(db.Integer, primary_key=True)
    starting_date_time = db.Column(db.DateTime) #note that in form start date time are separated but in database are combined(no time data type in mysql)
    finishing_date_time = db.Column(db.DateTime)
    gps_location = db.Column(db.String)
    governorate = db.Column(db.String)    
    location = db.Column(db.String) 
    its_name = db.Column(db.String) 
    p_code = db.Column(db.String)
    nb_of_families = db.Column(db.Integer)
    activity_type = db.Column(db.String)
    if_other_type = db.Column(db.String) 
    donor = db.Column(db.String)
    team_leader = db.Column(db.String)
    targeted_nb_in_camp = db.Column(db.Integer)
    distributed_items = db.Column(db.Integer)
    nb_of_itmes_to_be_distributed_in_this_act = db.Column(db.Integer)
    exists_of_written_scheduled = db.Column(db.Integer)
    voucher_distributed = db.Column(db.Integer)
    beneficiaries_list_ready_used = db.Column(db.Integer)
    protect_policies_respect_rate = db.Column(db.Integer)
    controllcing_workplacce_rate = db.Column(db.Integer)
    commitment_to_Covid_precautions = db.Column(db.Integer)
    existing_of_requirements = db.Column(db.Integer)
    if_shortcoming_in_requirements = db.Column(db.String)
    randomly_checked_item_rate = db.Column(db.Integer)
    staff_performance = db.Column(db.Integer)
    general_notes = db.Column(db.String)
    added_by = db.Column(db.Integer)
    date_added = db.Column(db.DateTime)
    date_edited = db.Column(db.DateTime)
   
    def __init__(self, starting_date_time, finishing_date_time, gps_location, governorate, location, its_name, p_code, nb_of_families, activity_type, if_other_type, donor, team_leader, targeted_nb_in_camp, distributed_items, 
    nb_of_itmes_to_be_distributed_in_this_act, exists_of_written_scheduled, voucher_distributed, beneficiaries_list_ready_used,
    protect_policies_respect_rate, controlling_workplacce_rate, commitment_to_Covid_precautions, existing_of_requirements,
     if_shortcoming_in_requirements, randomly_checked_item_rate, staff_performance, general_notes, added_by, date_added, date_edited):
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
        self.added_by = added_by
        self.date_added = date_added
        self.date_edited = date_edited


class eyeryeyDb(db.Model):
    __tablename__ = '555544hh'
    id = db.Column(db.Integer, primary_key=True)

class eyeryeyDb(db.Model):
    __tablename__ = 'hdfhfd'
    id = db.Column(db.Integer, primary_key=True)