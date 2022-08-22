from datetime import datetime
import pandas as pd
from package.dbmodels import Users, AdhaActivitiesRating, TrackFields
import os
import json
from package import db #lamma ba3nil imprt mnl package ya3ne import mnl __init__.py
from package import request #look at this

uri = 'postgresql://vmfbelplxyvepj:a2979b6807823c413e08a119955da592e94ab4f38696d568553ef3b11dbac674@ec2-54-87-179-4.compute-1.amazonaws.com:5432/deljs855e01f1t'

def finish_datetime():
    finish_datetime = datetime.now()
    return finish_datetime

def get_script_path(): #this will return the path till /"flask tests" without /functions.py
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

def append_form_nav(form_title):
    with open(get_script_path() + "/templates/navbar.html", "r") as file:
        lines = file.readlines()
    with open(get_script_path() + "/templates/navbar.html", "w") as file:
        lines.insert(30, f"""<li class="nav-item">\n    <a class="nav-link">{form_title}</a>\n</li>""")
        for i in lines:
            file.write(i)

#wtf funcs

def append_wtf_title(form_class):
    with open("mywtforms.py", "a") as file:
        file.write(f"""\nclass {form_class}(FlaskForm):\n    a = 1""")
        file.close()
        return

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

def customize_wtf_fld_code(possible_validators, field_type, field_name, field_label, in_req, text_only,
                            some_char, length, min_char, max_char, nb_range, min_nb, max_nb, choices): #should be the arg of append_wtform
    if choices:
                choices_dict = json.loads(choices)
    if check_for_validators(possible_validators):
        if field_type == "StringField":
            if length:
                length = f"Length(min={min_char}, max={max_char}, message='The length here should be betweeen {min_char} and {max_char}'),"
            else:
                length=""
            code = f"\n    {field_name} = {field_type}('{field_label}', [{in_req} {text_only} {some_char} {length}])"
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
            choices_code = mk_choices_code(choices_dict)
            code = f"""\n    {field_name} = {field_type}('{field_label}', [{in_req}], choices=[{choices_code}])"""
        else:
            return "An error occured!"
    elif  choices and not check_for_validators(possible_validators):
        choices_code = mk_choices_code(choices_dict)
        code = f"""\n    {field_name} = {field_type}('{field_label}', choices=[{choices_code}])"""
    elif field_type == "DateField" and not check_for_validators(possible_validators): #3melt hay 7atta iza l user ma 7at in_req wa2ta l func ma ra7 ta3mil datefield bala hay la2an l regex tab3etha msh mawjoude bl validators
        code = f"\n    {field_name} = {field_type}('{field_label}', [Regexp(r'/^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$/', message='The date format should be YYYY-MM-DD')])"
    elif field_type == "TimeField" and not check_for_validators(possible_validators):
        code = f"\n    {field_name} = {field_type}('{field_label}', [Regexp(r'^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$', message='The time format should be HH:MM:SS')])"
    else:
        code = f"""\n    {field_name} = {field_type}('{field_label}')"""
    return code

def append_wtform(field_code): # field_code arg ma3rouf b code bl func l 2abla
    with open("mywtforms.py", "a") as cr:
        cr.write(field_code)
        cr.close()
        return

# write dbmodels funcs

def db_model(form_class):
    db_class = form_class + "Db"
    return db_class

def append_db_class_title(form_class, table):
    db_class = db_model(form_class)
    with open("dbmodels.py", "a") as file:
        file.write(f"""\n\nclass {db_class}(db.Model):\n    __tablename__ = '{table}'\n    id = db.Column(db.Integer, primary_key=True)""")
        file.close()
        return

def datatype(field_type):
    str_data = ["StringField", "RadioField", "SelectField"]
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
    with open("dbmodels.py", 'a') as file:
        file.write(column)

def add_init_arg(field_name):  
    with open("init_arg.txt") as file:
        lines = file.readlines()
        lines[1] += f", {field_name}"
    with open("init_arg.txt", "w") as file:
        for i in lines:
            file.write(i)

def append_init_psswd(field_name):
    element = f"\n        self.{field_name} = generate_password_hash({field_name})"
    with open("init_db.txt", "a") as file:
        file.write(element)

def append_init_except_psswd(field_name): #hawn fte7 append mode
    element = f"\n        self.{field_name} = {field_name}"    
    with open("init_db.txt", "a") as file:
        file.write(element)

def append_init(field_type, field_name):
    if field_type == "PasswordField":
        append_init_psswd(field_name)
    else:
        append_init_except_psswd(field_name)

def set_psswd_func(field_type, field_name): #it may cause bugs if 2 or more password fields is setted
    if field_type == "PasswordField":
        with open("password_funcs.txt", "a") as file:
            file.write(f"""\n    @property\n    def password():\n        raise AttributeError('password is not a readable attribute!')\n    def verify_password(self, psswd):\n        return check__password_hash(self.{field_name}, psswd)""")
    else:
        return

def continue_dbmodel():
    #2awwal shi bte5od password_funcs if exists w bta3mellon append 3al init_db.txt ba3dayn bte5odon kollon w 3al dbmodels.py
    with open("password_funcs.txt") as file:
        lines = file.readlines()
    if lines:
        with open("password_funcs.txt") as file:
            psswd_funcs_lines = file.readlines()
        #with open("init_db.txt", "a") as file: #replaced below
         #   for i in psswd_funcs_lines:
          #      file.write(i)
        with open("init_db.txt") as file:
            init_lines = file.readlines()
        with open("init_arg.txt") as file: #configuring def__init__ before appending to it by adding ):
            arg_lines = file.readlines()
            arg_lines.append("):")
            all_lines = arg_lines
            for i in init_lines: #laysh la 2efta7 append mode , w 2et3azzab 3mel append 3al list do8re
                all_lines.append(i)
            for i in psswd_funcs_lines:
                all_lines.append(i)
        #with open("init_arg.txt",  "a") as file: #replaced above
         #   for i in init_lines:
         #       file.write(i)
        #with open("init_arg.txt") as file:
        #    all_lines = file.readlines()
        with open("dbmodels.py", "a") as file:
            for i in all_lines:
                file.write(i)
        with open("password_funcs.txt", "w") as file:
            file.write("")
        with open("init_db.txt", "w") as file:
            file.write("") 
        with open("init_arg.txt", "w") as file:
            file.write("\n    def __init__(self")     
    else:
        with open("init_db.txt") as file:
            init_lines = file.readlines()
        #with open("init_arg", "a") as file:
        #    for i in init_lines:
        #        file.write(i)
        with open("init_arg.txt") as file:
            all_lines = file.readlines()
            all_lines.append("):")
            for i in init_lines:
                all_lines.append(i)
        with open("dbmodels.py", "a") as file:
            for i in all_lines:
                file.write(i)
        with open("init_db.txt", "w") as file:
            file.write("")
        with open("init_arg.txt", "w") as file:
            file.write("\n    def __init__(self")



#writing route funcs' funcs

def route_function(form_class):
    route_func = f"{form_class}route"
    return route_func

def append_route(form_class):
    route_func = route_function(form_class)
    with open("create_form.py", "a") as file:
        file.write(f"""\n@app.route('/data_entry/{form_class}', methods=['GET', 'POST'])\n@login_required\ndef {route_func}():\n    cu_id = current_user.id\n    form = {form_class}""")

def organize_access(access_by):
    if access_by == 'only_admins':
        with open("create_form.py", "a") as file:
            file.write("\n    if cu_id in sys_admins:")

def get_data(): #hay bteshti8il 3al done #the importance of this func was when testing the iteration iver immutablemultidict
    data = request.form
    return data

def write_request(data):
    for i in data:
        with open("create_form.py", "a") as file:
            file.write(f"\n")

def track_fields():
    record = TrackFields("A")
    db.session.add(record)
    db.session.commit() 

def count_fields():
    count = TrackFields.query.count()
    print(count)
    return count       

def clear_track():
    records = TrackFields.query.all()
    db.session.delete(records)
    db.session.commit()