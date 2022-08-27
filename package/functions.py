from datetime import datetime
import re
import pandas as pd
from package.dbmodels import Users, AdhaActivitiesRating, TrackFields
import os
import json
from package import db, app, mail #lamma ba3nil imprt mnl package ya3ne import mnl __init__.py
from package import request, session #look at this, ma henne saro mawjoudin bl init 3mellon import bsatr we7id
from flask_mail import Message
uri = 'postgresql://vmfbelplxyvepj:a2979b6807823c413e08a119955da592e94ab4f38696d568553ef3b11dbac674@ec2-54-87-179-4.compute-1.amazonaws.com:5432/deljs855e01f1t'

def finish_datetime():
    finish_datetime = datetime.now()
    return finish_datetime

def get_script_path(): #this will return the path till the parent directory of functions.py bwich is "/package" without /functions.py
    return os.path.dirname(os.path.abspath(__file__))

def determine_model(table_name): #lezim 2a3mil dict l model variable bi3ayyit lal value taba3 l key l metlo
    if table_name == 'Users':
        model = Users
    elif table_name == 'AdhaActivitiesRating':
        model = AdhaActivitiesRating
    return model

def columns_names(model): #!!!!!!!!!!!!!!!!!!!1
    columns_list = model.__table__.columns.keys()
    return columns_list

def query_to_csv_excel(query_cmd): 
    df = pd.read_sql(query_cmd, con = uri)
    df.to_csv("query.csv", index = False)
    df1 = pd.read_csv("query.csv")
    excel_file = pd.ExcelWriter("query.xlsx")
    df1.to_excel(excel_file, index = False)
    excel_file.save()

def add_comma_if_validator(validators): #not used no need
    for validator in validators:
        if validator:
            index = validators.index(validator)
            validator += ","
            validators[index] = validator
    return validators

#nav item func

def append_form_nav(form_title, form_class): #we cant use logic with jinja cause of format mode
    with open(get_script_path() + "/templates/navbar.html", "r") as file:
        lines = file.readlines()
    with open(get_script_path() + "/new_navbar.html", "w") as file:
        lines.insert(30, f"""<li class="nav-item">\n    <a class="nav-link" href="/data_entry/{form_class}" >{form_title}</a>\n</li>""")
        for i in lines:
            file.write(i)

#make teplate funcs

def create_template(form_title, form_class): #no longer needed
    with open(get_script_path() + f'/{form_title}template.html', 'w') as file:
        file.write(f"""{{%extends "base.html"%}}\n{{% block title %}}{form_class}{{% endblock %}}\n{{% block content %}}\n\n\n{{% endblock %}}""")

def prpr_templ_flds(field_name, form_title, form_class): #iza rje3na lal shakl ml 2adim badna n7ot fields badal field
    templ_lines = [ '{%extends "base.html"%}', f"\n{{% block title %}}{form_class}{{% endblock %}}", "\n{% block content %}", "\n", "\n", "\n{% endblock %}" ]
    #for field in fields:
    #    field_name = field[0]
    #    flds_list = []
    #    wtf_fld_l_el = ["{{ ", "", " }}"] #hayde l 7araket 7atta ma tpannik l format #el: elements list
    #    wtf_fld_el = ["{{ ", "", " }}"]
    #    wtf_fld_l_el[1] = f'form.{field_name}.label(class_="form-label")'
    #    wtf_fld_el[1] = f'form.{field_name}(class_="form-control")'
    #    wtf_fld_l = wtf_fld_l_el[0] + wtf_fld_l_el[1] + wtf_fld_l_el[2] #wtf_fld_label
    #    wtf_fld = wtf_fld_el[0] + wtf_fld_el[1] + wtf_fld_el[2]
    #    templ_lines.insert(4, wtf_fld_l)
    #    templ_lines.insert(4, wtf_fld)"""
        #flds_list.append(wtf_fld_l)
        #flds_list.append(wtf_fld)
    #hayk l flds list bikoun fiha strings bl dawr label byerja3 control la kol fld bl fields lli 3emelon l user
    #field_name = field[0]
    wtf_fld_l_el = ["{{ ", "", " }}"] #hayde l 7araket 7atta ma tpannik l format #el: elements list
    wtf_fld_el = ["{{ ", "", " }}"]
    wtf_fld_l_el[1] = f'form.{field_name}.label(class_="form-label")'
    wtf_fld_el[1] = f'form.{field_name}(class_="form-control")'
    wtf_fld_l = wtf_fld_l_el[0] + wtf_fld_l_el[1] + wtf_fld_l_el[2] #wtf_fld_label
    wtf_fld = wtf_fld_el[0] + wtf_fld_el[1] + wtf_fld_el[2]
    templ_lines.insert(4, wtf_fld_l)
    templ_lines.insert(4, wtf_fld)
    print(templ_lines)     
    with open(get_script_path() + f'/{form_title}template.html', 'w') as file:
        for line in templ_lines:
            file.write(line)

def rm_sended_templ(form_title):
    os.remove(get_script_path() + f'/{form_title}template.html')
    os.remove(get_script_path() + '/new_navbar.html')
    print("templates removed")


#wtf funcs

def append_wtf_title(form_class):
    with open(get_script_path() + "/newformclass.txt", "a") as file:
        file.write(f"""\n\nclass {form_class}(FlaskForm):""")
        file.close()

def check_for_validators(validators): #not that usefull
    for i in validators:
        if i:
            return True

def mk_choices_code(choices):
    choices_code = ""
    c = 0
    for i in choices:
        c += 1
        if c == len(choices): #la2an 2e5ir we7de ma lezim ykoun waraha fasle
            chv_tuples = f"('{choices[i]}', '{i}')"
            choices_code += chv_tuples
        else:
            chv_tuples = f"('{choices[i]}', '{i}'), "
            choices_code += chv_tuples
    return choices_code

def customize_wtf_fld_code(possible_validators, field_type, field_name, field_label, in_req, regex,
                             length, min_char, max_char, nb_range, min_nb, max_nb, choices): #should be the arg of append_wtform
    #if choices:
     #           choices_dict = json.loads(choices)
    if check_for_validators(possible_validators):
        if field_type == "StringField":
            if length:
                length = f"Length(min={min_char}, max={max_char}, message='The length here should be betweeen {min_char} and {max_char}'),"
            else:
                length=""
            code = f"\n    {field_name} = {field_type}('{field_label}', [{in_req} {regex} {length}])"
        elif field_type == "IntegerField":
            if nb_range:
                nb_range = f"NumberRange(min={min_nb}, max={max_nb}, message='The number here should be between {min_nb} and {max_nb}')"
            else:
                nb_range=""
            code = f"\n    {field_name} = {field_type}('{field_label}', [{in_req} {nb_range}])"
        elif field_type == "PasswordField":
            code = f"\n    {field_name} = {field_type}('{field_label}', [{in_req}])"
        elif field_type == "DateField":
        #la tensa badna default time hawn w sho8lon bikoun bl done w bl route
            code = f"\n    {field_name} = {field_type}('{field_label}', [{in_req} Regexp(r'/^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$/', message='The date format should be YYYY-MM-DD')])"
        elif field_type == "TimeField":
            code = f"\n    {field_name} = {field_type}('{field_label}', [{in_req} Regexp(r'^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$', message='The time format should be HH:MM:SS')])"
        #la tnsa default date
        elif field_type == "SelectField" or field_type == "RadioField":
            choices_code = mk_choices_code(choices)#_dict)
            code = f"""\n    {field_name} = {field_type}('{field_label}', [{in_req}], choices=[{choices_code}])"""
        else:
            return "An error occured!"
    elif  choices and not check_for_validators(possible_validators):
        choices_code = mk_choices_code(choices)#_dict)
        code = f"""\n    {field_name} = {field_type}('{field_label}', choices=[{choices_code}])"""
    elif field_type == "DateField" and not check_for_validators(possible_validators): #3melt hay 7atta iza l user ma 7at in_req wa2ta l func ma ra7 ta3mil datefield bala hay la2an l regex tab3etha msh mawjoude bl validators
        code = f"\n    {field_name} = {field_type}('{field_label}', [Regexp(r'/^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$/', message='The date format should be YYYY-MM-DD')])"
    elif field_type == "TimeField" and not check_for_validators(possible_validators):
        code = f"\n    {field_name} = {field_type}('{field_label}', [Regexp(r'^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$', message='The time format should be HH:MM:SS')])"
    else:
        code = f"""\n    {field_name} = {field_type}('{field_label}')"""
    return code

def append_wtform(field_code): # field_code arg ma3rouf b code bl func l 2abla
    with open(get_script_path() + "/newformclass.txt", "a") as cr:
        cr.write(field_code)
        cr.close()

# write dbmodels funcs

def db_model(form_class):
    db_class = form_class + "Db"
    return db_class

def append_db_class_title(form_class, table):
    db_class = db_model(form_class)
    with open(get_script_path() + "/dbmodels.txt", "a") as file:
        file.write(f"""\n\nclass {db_class}(db.Model):\n    __tablename__ = '{table}'\n    id = db.Column(db.Integer, primary_key=True)""")
        file.close()

def datatype(field_type):
    str_data = ["StringField", "RadioField", "SelectField", "PasswordField"]
    datetime_data = ["DateField", "TimeField"]
    if field_type in str_data:
        datatype = "String"
    elif field_type == "IntegerField":
        datatype = "Integer"
    elif field_type in datetime_data:
        datatype = "DateTime"
    else:
        datatype = "Undifined"
    return datatype

def append_column(field_name, field_type):
    data_type = datatype(field_type)
    column = f"""\n    {field_name} = db.Column(db.{data_type})"""
    with open(get_script_path() + "/dbmodels.txt", 'a') as file:
        file.write(column)

def add_init_arg(field_name):  
    with open(get_script_path() + "/init_arg.txt") as file:
        lines = file.readlines()
        lines[1] += f", {field_name}"
    with open(get_script_path() + "/init_arg.txt", "w") as file:
        for i in lines:
            file.write(i)

def append_init_psswd(field_name):
    element = f"\n        self.{field_name} = generate_password_hash({field_name})"
    with open(get_script_path() + "/init_db.txt", "a") as file:
        file.write(element)

def append_init_except_psswd(field_name): #hawn fte7 append mode
    element = f"\n        self.{field_name} = {field_name}"    
    with open(get_script_path() + "/init_db.txt", "a") as file:
        file.write(element)

def append_init(field_type, field_name):
    if field_type == "PasswordField":
        append_init_psswd(field_name)
    else:
        append_init_except_psswd(field_name)

def set_psswd_func(field_type, field_name): #it may cause bugs if 2 or more password fields is setted
    if field_type == "PasswordField":
        with open(get_script_path() + "/password_funcs.txt", "a") as file:
            file.write(f"""\n    @property\n    def password():\n        raise AttributeError('password is not a readable attribute!')\n    def verify_password(self, psswd):\n        return check__password_hash(self.{field_name}, psswd)""")

def continue_dbmodel():
    #2awwal shi bte5od password_funcs if exists w bta3mellon append 3al init_db.txt ba3dayn bte5odon kollon w 3al dbmodels.py
    with open(get_script_path() + "/password_funcs.txt") as file:
        lines = file.readlines()
    if lines:
        with open(get_script_path() + "/password_funcs.txt") as file:
            psswd_funcs_lines = file.readlines()
        with open(get_script_path() + "/init_db.txt") as file:
            init_lines = file.readlines()
        with open(get_script_path() + "/init_arg.txt") as file: #configuring def__init__ before appending to it by adding ):
            arg_lines = file.readlines()
            arg_lines.append("):")
            all_lines = arg_lines
            for i in init_lines: #laysh la 2efta7 append mode , w 2et3azzab 3mel append 3al list do8re
                all_lines.append(i)
            for i in psswd_funcs_lines:
                all_lines.append(i)
        with open(get_script_path() + "/dbmodels.txt", "a") as file:
            for i in all_lines:
                file.write(i)
        with open(get_script_path() + "/password_funcs.txt", "w") as file:
            file.write("")
        with open(get_script_path() + "/init_db.txt", "w") as file:
            file.write("") 
        with open(get_script_path() + "/init_arg.txt", "w") as file:
            file.write("\n    def __init__(self")     
    else:
        with open(get_script_path() + "/init_db.txt") as file:
            init_lines = file.readlines()
        with open(get_script_path() + "/init_arg.txt") as file:
            all_lines = file.readlines()
            all_lines.append("):")
            for i in init_lines:
                all_lines.append(i)
        with open(get_script_path() + "/dbmodels.txt", "a") as file:
            for i in all_lines:
                file.write(i)
        with open(get_script_path() + "/init_db.txt", "w") as file:
            file.write("")
        with open(get_script_path() + "/init_arg.txt", "w") as file:
            file.write("\n    def __init__(self")



#writing route funcs' funcs

def route_function(form_class):
    route_func = f"{form_class}route"
    return route_func

def append_route(form_class):
    route_func = route_function(form_class)
    with open(get_script_path() + "/routes.txt", "a") as file:
        file.write(f"""\n@app.route('/data_entry/{form_class}', methods=['GET', 'POST'])\n@login_required\ndef {route_func}():\n    cu_id = current_user.id\n    form = {form_class}""")

def organize_access(access_by):
    if access_by == 'only_admins':
        with open(get_script_path() + "/routes.txt", "a") as file:
            file.write("""\n    if cu_id in sys_admins:\n        if request.method == "POST":\n            if form.validate_on_submit():""")
    else:
        with open(get_script_path() + "/routes.txt", "a") as file:
            file.write("""\n    if request.method == "POST":\n        if form.validate_on_submit():""")
    return access_by

def track_fields(field_name):
    record = TrackFields(f"{field_name}")
    db.session.add(record)
    db.session.commit() 

def count_fields(): #not needed
    count = TrackFields.query.count()
    return count       

def query_track():
    query_cmd = "select track from fieldscount"
    query = db.engine.execute(query_cmd)
    #query = TrackFields.query.all()
    return query

def clear_track():
    records = TrackFields.query.all()
    for record in records:
        db.session.delete(record)
        db.session.commit()

def write_requests(access_by): #ken fina na3mil function kol marra ta3mil append 3l routes.txt bas hay 2a7san bfard marra b execute wwe7de b open we7de bta3mil kol shi
    query = query_track()
    if access_by == "only_admins":
        with open(get_script_path() + "/routes.txt", "a") as file:
            for field in query:
                request_code = f"""\n              {field[0]} = request.form["{field[0]}"]"""
                file.write(request_code)
    else:
        with open(get_script_path() + "/routes.txt", "a") as file:
            for field in query:
                request_code = f"""\n          {field[0]} = request.form["{field[0]}"]"""
                file.write(request_code)
            
def write_return(access_by, form_title):
    if access_by == 'only_admins':
        with open(get_script_path() + "/routes.txt", "a") as file:
            returns = f"""\n    flash("Only for admins!")\n    return redirect(url_for("de_welcome"))\n        return render_template("/data_entry/{form_title}template.html", form=form, cu_id=cu_id)\n            flash("One or Some inputs are not valid, fix!")\n            return render_template("/data_entry/{form_title}template.html", form=form, cu_id=cu_id))"""
    else:
        with open(get_script_path() + "/routes.txt", "a") as file:
            returns = f"""\n    return render_template("/data_entry/{form_title}template.html", form=form, cu_id=cu_id)\n        flash("One or Some inputs are not valid, fix!")\n        return render_template("/data_entry/{form_title}template.html", form=form, cu_id=cu_id))"""
#not completed

def notify_dev(form_title):
    template = f'{form_title}template.html'
    msg = Message(subject='New form added', recipients=["moussaalit@outlook.com"])#, attachments=['routes.txt', 'newformclass.txt', 'dbmodels.txt', template]) #fine 7ot bl list add ma badde recipient,,, bas hawn 2ana meni3 2ajtar mn 1 recepient bl config hhhh
    #msg.body = 'A new form has been created, Your turn!!!'
    #msg.html = '<p>A new form has been created,<span style="color:red"> Your turn!!!</span></p>'
    list = ['routes.txt', 'newformclass.txt', 'dbmodels.txt', template, "new_navbar.html"]
    c = 0
    for i in list:
        c += 1
        if c == 5:
            with app.open_resource(f"{get_script_path()}/{i}") as file:
                msg.attach(i, 'text/plain', file.read())
            mail.send(msg) #didn't undertanded laysh ma ride tkoun l mail.send barra l loop, wl laysh attachments= ma shta8lat
            
        else:
            with app.open_resource(f"{get_script_path()}/{i}") as file:
                msg.attach(i, 'text/plain', file.read()) #hayk la 7atta yjammi3 attaches

def clear_sended_files():
    with open(get_script_path() + "/routes.txt", "w") as file, open(get_script_path() + "/newformclass.txt", "w") as file1, open(get_script_path() + "/dbmodels.txt", "w") as file2: 
        file.write("")
        file1.write("")
        file2.write("")
