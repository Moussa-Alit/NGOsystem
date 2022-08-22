from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, HiddenField, DateField, TimeField, SubmitField, PasswordField, RadioField, FormField, FieldList
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
    targeted_nb_in_camp = IntegerField('الهدف الكلي في هذا المخيم/Overall target in this camp', [InputRequired(), NumberRange(min=3, max=25000, message="The overall target should be between 3 and 25000") ])
    distributed_items = IntegerField('عدد الحصص الموزع/Distributed items Count',[InputRequired(), NumberRange(min=3, max=25000, message="The overall target should be between 3 and 25000")])
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

class SelectingFormToEdit(FlaskForm): #selecting form type
    id_field = HiddenField()
    form = SelectField('Select what type of forms you want to edit | إختر نوع الإستمارة اللتي تود تعديلها', [InputRequired()], choices=[('', ''), ('register', 'Register'), ('AdhaActivities', 'تقييم نشاطات الأضحى')])
    submit = SubmitField('إختيار')

class SelectQueringBase(FlaskForm):
    type = RadioField("Select querying base", [InputRequired()], choices=[('', ''), ('records', 'Records'), ('columns', 'Fields'), ('cells', 'Cells')]) 


class QueryingRecordsTDateTime(FlaskForm):
    #id_field = HiddenField()
    table = SelectField('Select what form to query from it | إختر أي إستمكارة لتاخذ منها', [InputRequired()], choices=[('', ''), ('users', 'Register'), ('adhaactsrating', 'تقييم نشاطات الأضحى')])
    first_date = DateField('', [InputRequired(), Regexp(r'/^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$/', message='The date format should be YYYY-MM-DD')])
    last_date = DateField('', [InputRequired(), Regexp(r'/^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$/', message='The date format should be YYYY-MM-DD')])
    #first_time = TimeField("", [InputRequired(), Regexp(r'^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$',
     #message='The time format should be HH:MM:SS')])
    #last_time = TimeField("", [InputRequired(), Regexp(r'^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$',
     #message='The time format should be HH:MM:SS')])
    how_much = IntegerField('How much', [InputRequired(), NumberRange(min=1, max=25000, message="The overall target should be between 1 and 25000")])
    order = SelectField('Order (Acsending is preffered)', [InputRequired()], choices=[('', ''), ('asc', 'Ascendind'), ('desc', 'Descending')])

class Titles(FlaskForm):
    form_title = StringField("Give a title for the form (can be in arabic)", [InputRequired(), 
    Regexp(r'^[A-Za-z\s\-\']+$', message='Invalid Title, it should be special character free(#$%^&*,;:...)!'),
    Length(min=3, max=20, message='The Title length should be between 3 and 20') ])
    form_class = StringField('Give the form an english name without spaces(CamelCase is preffered)',[InputRequired(), Regexp(r'^[A-Za-z\s\-\']+$', message='Invalid Title, it should be special character free(#$%^&*,;:...)!'),
    Length(min=3, max=20, message='The Name length should be between 3 and 20')])
    table = StringField('Give an english name without spaces/numbers/characters/uppercase letters to the table that the data will be stored in.',[InputRequired(), Regexp(r'^[a-z\s\-\']+$', message='Invalid Title, it should be special character free(#$%^&*,;:...)!'),
    Length(min=3, max=20, message='The Name length should be between 3 and 20')])
    #db_class is a function
    access_by = SelectField("Who can access this form?", choices=[('', ''), ('only_admins', 'Only Admins'), ('any', 'Anybody')])

class MakeForm(FlaskForm):
    field_name = StringField('Give this field a short name(no sprcial characters/uppercase/numbers/spaces).', [InputRequired(), Regexp(r'^[\.a-zA-Z0-9,;.? ]*$', message='Only text, nb, ,;.?'), Length(min=3, max=30, message='Min length=3, max=30')])
    flabel = StringField('Write a label for the field', [InputRequired(), Regexp(r'^[\.a-zA-Z0-9,;.? ]*$', message='Only text, nb, ,;.?'), Length(min=3, max=200, message='Min length=3, max=200')])
    min_nb = StringField('Min nb', [Regexp(r'^\\d+$', message='Only numbers')])
    max_nb = StringField('Max nb', [Regexp(r'^\\d+$', message='Only numbers')])
    min_char = StringField('Min char', [Regexp(r'^\\d+$', message='Only numbers')])
    max_char = StringField('Max char', [Regexp(r'^\\d+$', message='Only numbers')])

class yityjtj(FlaskForm):
    a = 1
class wfqwfqwf(FlaskForm):
    a = 1
class ktyjtjtyj(FlaskForm):
    a = 1
class dsvdsdvs(FlaskForm):
    a = 1
class thrh(FlaskForm):
    a = 1
class ergrgnthrh(FlaskForm):
    a = 1
class ergrgnergergthrh(FlaskForm):
    a = 1
    rthtrhz = RadioField('srhhrse')
    sdfasfas = RadioField('asdfasd')
    ergwerg = RadioField('wegewrgyjj', [InputRequired(), 
                    
                   ])
    sfasf = RadioField('aefafewe', [InputRequired(), 
                    
                   ])
    fbzzb = RadioField('dz zdbnbz', [InputRequired(), 
                    
                   ])
    dhrfhea = RadioField('eahhaerh')
    hsthsth = RadioField('thhsth')
    ddssdv = SelectField('gvsvsdv')
    hdfhdh = RadioField('fdhfhf', [InputRequired(), 
                    
                   ])
    thrthrth = PasswordField('rth#$%')
    #aaghthj = RadioField('lyilyuiuil', choices=[('jrtyjrytytr', 'yjrtyjyy'), ('jyrjytjyuo', 'yjrtyjydyjjry'), ('xcmdjsdj', 'yodfnhdsgkiu')]
    #aaghthj = RadioField('lyilyuiuil', choices=[('jrtyjrytytr', 'yjrtyjyy'), ('jyrjytjyuo', 'yjrtyjydyjjry'), ('xcmdjsdj', 'yodfnhdsgkiu')]
    rkukuruuyk = SelectField('oiutj', choices=[('jyetyj', 'etyjetyj')])
    kits_nb = RadioField('ما هو عدد الحصص الموزعة', choices=[('ألف', '1000'), ('الف و خمسمية', '1500'), ('ألفان', '2000')])
    #hhhhhh bl 2olb 2leb l choice wl value
    ergrgg = RadioField('wrgwrgwrg', [InputRequired(), 
                    
                   ], choices=[('sdhsh', 'shshdfh'), ('esgrg', 'hyjtuk')])
    password = PasswordField('password', [InputRequired(), 
                    
                   ])
    password = PasswordField('password', [InputRequired(), 
                    
                   ])
    radio_f = RadioField('radio just select', choices=[('regaeg', 'agrge'), ('jytjty', 'gerg'), ('rgdrgg', 'et4ete4t'), ('drgrdgdg', 'dgdrgrd')])

    etydrdfh = PasswordField('dhdfhdhdfh', [InputRequired(), 
                    
                   ])
    fghfhthrth = SelectField('rthrthrt', [InputRequired(), 
                    
                   ], choices=[('hrthrthjtyj', 'rthrthrt')])
    casaga = DateField('asgassgas', [InputRequired(), 
                    
                   ])
    casaga = RadioField('asgassgas', [InputRequired(), 
                    
                   ], choices=[('ertertert', 'terte')])
    afsaesfeasf = RadioField('effasfe', choices=[('rhthsrthtrsh', 'tthtsrhtshs')])
    eafawas = RadioField('fasfasfasf', choices=[('sgsdgsdghmk', 'sggdg'), ('aerrye', 'xffhffgh'), ('fgzfdgdfz', 'aeraggzg')])