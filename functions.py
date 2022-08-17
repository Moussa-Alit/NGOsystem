from datetime import datetime
import pandas as pd
from dbmodels import Users, AdhaActivitiesRating
import os

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

def append_wtf_title(form_class):
    with open("mywtforms.py", "a") as file:
        file.write(f"""\nclass {form_class}(FlaskForm):\n    a = 1""")
        file.close()
        return

def db_model(form_class):
    db_class = form_class + "Db"
    return db_class

def route_function(form_class):
    route_func = form_class + "route"
    return route_func

def append_db_class_title(form_class, table):
    db_class = db_model(form_class)
    with open("dbmodels.py", "a") as file:
        file.write(f"""\n\nclass {db_class}(db.Model):\n    __tablename__ = '{table}'\n    id = db.Column(db.Integer, primary_key=True)""")
        file.close()
        return

def append_form_title(form_title):
    with open(get_script_path() + "/templates/navbar.html", "r") as file:
        lines = file.readlines()
    with open(get_script_path() + "/templates/navbar.html", "w") as file:
        lines.insert(30, f"""<li class="nav-item">\n    <a class="nav-link">{form_title}</a>\n</li>""")
        for i in lines:
            file.write(i)

def append_route(form_class):
    route_func = route_function(form_class)
    with open("create_form.py", "a") as file:
        file.write(f"""@app.route('/data_entry/{form_class}', methods=['GET', 'POST'])\n@login_required\ndef {route_func}():\n    cu_id = current_user.id""")

def append_wtform(flaskform):
    with open("mywtforms.py", "a") as cr:
        cr.write(flaskform)
        cr.close()
        return

def check_for_validators(validators):
    for i in validators:
        if i:
            return True


def add_comma_if_validator(validators):
    for validator in validators:
        if validator:
            index = validators.index(validator)
            validator += ","
            validators[index] = validator
    return validators
