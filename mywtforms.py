from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, HiddenField, DateField, TimeField, SubmitField, PasswordField, RadioField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange



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
    starting_time = TimeField('موعد بدء التنفيذ/Execution starting time', [InputRequired(), Regexp(r'^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$',
     message='The time format should be HH:MM:SS')])
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

class SelectinFormToEdit(FlaskForm): #selecting form type
    id_field = HiddenField()
    form = SelectField('Select what type of forms you want to edit | إختر نوع الإستمارة اللتي تود تعديلها', [InputRequired()], choices=[('', ''), ('register', 'Register'), ('AdhaActivities', 'تقييم نشاطات الأضحى')])
    submit = SubmitField('إختيار')

class SelectingWichFormBlZabt(FlaskForm): #ya3ne 2aya form mn bayn 2e5ir 3 form 3melnehoun
    id_field = HiddenField()
    records = RadioField('Select wich form to edit | إختر الإستمارة التي تريد تعيديلها', [InputRequired()], choices=[('', ''), ('top', '')])