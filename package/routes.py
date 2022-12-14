
from pymysql import IntegrityError
from package import app, login_manager
from flask import after_this_request, render_template, redirect, send_file, url_for, request, flash, make_response, session
from package.dbmodels import *
from package.mywtforms import *
from package.functions import *
from flask_login import login_user, login_required, current_user, logout_user
from flask_mail import Message

#important lists
sys_admins = [1, 3]
"""users_headings = ['id', 'name', 'surname', 'username', 'email', 'password_hash', 'date_added', 'date_edited'] #colummns_names() should replace these
aar_headings = ['id', 'starting_date_time', 'finishing_date_time', 'gps_location', 'governorate',
 'location', 'its_name', 'p_code', 'nb_of_families', 'activity_type', 'if_other_type', 'donor', 'team_leader',
  'targeted_nb_in_camp', 'distributed_items', 'nb_of_itmes_to_be_distributed_in_this_act', 'exists_of_written_scheduled','voucher_distributed',
   'beneficiaries_list_ready_used', 'protect_policies_respect_rate', 'controllcing_workplacce_rate', 'commitment_to_Covid_precautions',
    'existing_of_requirements', 'if_shortcoming_in_requirements', 'randomly_checked_item_rate', 'staff_performance', 'general_notes',
 'added_by', 'date_added', 'date_edited']"""

# routes
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginform()
    if form.validate_on_submit():
        req_username = request.form["username"]
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
    if id in sys_admins:
        form = RegisterForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                name = request.form["name"]
                surname = request.form["surname"]
                username = request.form["username"]
                email = request.form["email"]
                password = request.form["password"]
                date_added = finish_datetime()
                record = Users(name, surname, username, email, password, date_added, date_edited=None)
                db.session.add(record)
                db.session.commit()
                flash("The new user has been added successfully")
                return redirect(url_for('register'))
            else:
                return render_template("register.html", form=form, cu_id=id)
        else:
            return render_template("/data_entry/register.html", form=form, cu_id=id, admins=sys_admins)
    #message = "An error occured try to logout then login again"
    return redirect(url_for("welcome"))


@app.route('/')
@login_required
def welcome():
    cu_id = current_user.id
    return render_template("departmentsnavigation.html", cu_id=cu_id)

@app.route('/Ba3dayn_bsewihoun')
@login_required
def welcome_mo2akkate():
    return "<h1> hello this is under development</h1>"

@app.route('/DataEntry')
@login_required
def de_welcome():
    cu_id = current_user.id
    return render_template("/indexes/de_index.html", cu_id=cu_id, admins=sys_admins)

@app.route('/Graphs_Statistics')
@login_required
def gs_welcome():
    cu_id = current_user.id
    if cu_id in sys_admins:
        return render_template("/indexes/gs_index.html")
    flash("Only for admins")
    return redirect(url_for('welcome'))

@app.route("/A_A_R", methods=['GET', 'POST'])
@login_required
def A_A_R():
    cu_id = current_user.id
    form1 = AdhaActivities()
    if request.method == 'POST':
        if form1.validate_on_submit:
        #gps_location_should_be_taken_auto
            starting_date = request.form["starting_date"] 
            #starting_time = request.form["starting_time"]
            starting_time = "11:11:11.321333"
            starting_datetime = starting_date + " " + starting_time
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
            added_by = cu_id
            date_added = finish_datetime()
            record = AdhaActivitiesRating(starting_datetime, finish_date_time, gps, governorate, location, its_name, p_code, nb_of_families, activity_type, if_other_type, donor, team_leader, targeted_nb_in_camp, distributed_items, nb_of_itmes_to_be_distributed_in_this_act,
        exists_of_written_scheduled, voucher_distributed, beneficiaries_list_ready_used, protect_policies_respect_rate, controlling_workplacce_rate,
        commitment_to_covid_precautions, existing_of_requirements, if_shortcoming_in_requirements, randomly_checked_item_rate,
        staff_performance, general_notes, added_by, date_added, date_edited=None)
            db.session.add(record)
            db.session.commit()
            flash("لقد تمت إضافة المعلومات بنجاح!")
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
    return render_template("/data_entry/adhaactrating.html", status4="active", form=form1, cu_id=cu_id, admins=sys_admins)

@app.route('/data_entry/update', methods=['POST', 'GET'])
@login_required
def select_form_type():
    cu_id = current_user.id
    form = SelectingFormToEdit()
    if request.method == 'POST':
        selected_form = request.form['form']
        if cu_id in sys_admins and (selected_form == 'register'):
            session['table'] = 'Users'
            #session['queried_records'] = table.query.order_by(table.id.desc()).limit(3)
            session['wich_form'] = 'Register'
            return redirect(url_for('select_form'))
        elif selected_form == 'AdhaActivities':
            la_net2akkad = AdhaActivitiesRating.query.filter_by(added_by=cu_id).order_by(AdhaActivitiesRating.id.desc()).limit(3) #la net2akkad 2eno howwe 3emil mn he l form aslan
            if la_net2akkad or cu_id in sys_admins:
                session['table'] = 'AdhaActivitiesRating'
                session['wich_form'] = 'تقييم نشاطات الأضحى'
                return redirect(url_for('select_form'))
        else:
            flash("تأكد من إختيارك")
            return redirect(url_for('select_form_type'))
    else:
        new = "new"
        form = SelectingFormToEdit()
        return render_template('selecting_f_to_e.html', form=form, cu_id=cu_id, admins=sys_admins)

@app.route('/data_entry/select_form', methods=['POST', 'GET'])
@login_required
def select_form(): #tab3an badna n7awwil na3mil functions la nhawwin l sho8l
    cu_id = current_user.id
    table = session.get('table')
    if request.method == 'POST': #ba3d ma ykoun na22a
        record_to_workwith_id = request.form['id']
        what_to_do = request.form['what_to_do']
        if table == 'Users':
            if what_to_do == 'delete(only_for_admins) | حذف' and cu_id in sys_admins:
                user_to_delete = Users.query.filter(Users.id == record_to_workwith_id).first()
                db.session.delete(user_to_delete)
                db.session.commit()
                flash('تم حذف المستخدم بنجاح')
                return redirect(url_for('select_form_type'))
            elif what_to_do == 'delete(only_for_admins) | حذف' and cu_id not in sys_admins:
                flash('Only for admins')
                return redirect(url_for('select_form_type'))
            elif what_to_do == 'edit | تعديل' and cu_id in sys_admins:
                session['passed'] = 'passed'
                session['record_to_edit_id'] = record_to_workwith_id
                return redirect(url_for('edit_users'))
        elif table == 'AdhaActivitiesRating':
            if what_to_do == 'delete(only_for_admins) | حذف' and cu_id in sys_admins:
                record_to_delete = AdhaActivitiesRating.query.filter(AdhaActivitiesRating.id == record_to_workwith_id).first()
                db.session.delete(record_to_delete)
                db.session.commit()
                flash('تم حذف التسجيل بنجاح')
                return redirect(url_for('select_form_type'))
            elif what_to_do == 'edit | تعديل':
                session['record_to_edit_id'] = record_to_workwith_id
                session['passed'] = 'passed'
                return redirect(url_for('edit_a_a_r'))
            else:
                flash('Only for admins')
                return redirect(url_for('select_form_type'))
                #return "Only admins can delete forms"
        return "hello2"
    #queried_records = session.get('queried_records')
    else:
        if table == 'Users':
            query = Users.query.order_by(Users.id.desc()).limit(3)
            return render_template("selecting_record.html", queried_records=query, wich_form=session['wich_form'])
        elif table == 'AdhaActivitiesRating':
            if cu_id in sys_admins:
                query = AdhaActivitiesRating.query.order_by(AdhaActivitiesRating.id.desc()).limit(3)
                return render_template('selecting_record.html', queried_records=query, wich_form=session['wich_form'], cu_id=cu_id, admins=sys_admins)
            else:
                query = AdhaActivitiesRating.query.filter_by(added_by=cu_id).order_by(AdhaActivitiesRating.id.desc()).limit(3)
                return render_template('selecting_record.html', queried_records=query, wich_form=session['wich_form'], cu_id=cu_id, admins=sys_admins)
        else:
            return "You shoyld select a form first"

@app.route('/data_entry/edit/adha_acts_rating', methods=['POST', 'GET'])
@login_required
def edit_a_a_r():
    form = AdhaActivities()
    cu_id = current_user.id #kormel l navbar
    passed = session['passed']
    record_id = session.get('record_to_edit_id')
    record = AdhaActivitiesRating.query.filter(AdhaActivitiesRating.id==record_id).first()
    if request.method == 'POST' and form.validate_on_submit:
        starting_date = request.form["starting_date"]
        #starting_date = "2020-11-22" 
        starting_time = request.form["starting_time"]
        #starting_time = "11:11:11.321333"
        record.starting_datetime = starting_date + " " + starting_time
        record.finishing_date_time = record.finishing_date_time
        record.governorate = request.form['governorate']
        record.location = request.form['location']
        #gps = request.form["gps"] #la 7atta ysir l site taba3e https la tsir tshti8il l gps
        gps = "12.123123,88,312342"
        record.its_name = request.form['its_name']
        record.p_code = request.form['p_code']
        record.nb_of_families = request.form['nb_of_families']
        record.activity_type = request.form['activity_type']
        record.if_other_type = request.form['if_other_type']
        record.donor = request.form['donor']
        record.team_leader = request.form['team_leader']
        record.targeted_nb_in_camp = request.form['targeted_nb_in_camp']
        record.distributed_items = request.form['distributed_items']
        record.nb_of_itmes_to_be_distributed_in_this_act = request.form['nb_of_itmes_to_be_distributed_in_this_act']
        record.exists_of_written_scheduled = request.form['exists_of_written_scheduled']
        record.voucher_distributed = request.form['voucher_distributed']
        record.beneficiaries_list_ready_used = request.form['beneficiaries_list_ready_used']
        record.protect_policies_respect_rate = request.form['pprr']
        record.controlling_workplacce_rate = request.form["controlling_workplacce_rate"]
        record.commitment_to_covid_precautions = request.form["commitment_to_covid_precautions"]
        record.existing_of_requirements = request.form['existing_of_requirements'] #tawejoud l ma3added wl mostalzamet llojistiyye
        record.if_shortcoming_in_requirements = request.form['if_shortcoming_in_requirements'] #iza fi nawa2es bl mostalzamet
        record.randomly_checked_item_rate = request.form["randomly_checked_item_rate"]
        record.staff_performance = request.form["staff_performance"]
        record.general_notes = request.form['general_notes']
        record.added_by = record.added_by
        record.date_added = record.date_added
        record.date_edited = finish_datetime()
        db.session.commit()
        flash("تم التعديل بنجاح")
        return redirect(url_for('de_welcome'))
    elif passed == 'passed':
        return render_template('/edit/aar_to_edit.html', form=form, record=record, cu_id=cu_id, admins=sys_admins) 
    return(redirect(url_for('select_form_type')))

@app.route('/data_entry/edit/users', methods=['POST', 'GET'])
@login_required
def edit_users():
    form = RegisterForm()
    passed = session.get('passed')
    cu_id = current_user.id
    record_id = session.get('record_to_edit_id')
    record = Users.query.filter(Users.id==record_id).first()
    if passed == 'passed' and cu_id == 3:
        if request.method == 'POST' and form.validate_on_submit:
            record.name = request.form["name"]
            record.surname = request.form["surname"]
            record.username = request.form["username"]
            record.email = request.form["email"]
            new_psswd = request.form["password"]
            record.password_hash = generate_password_hash(new_psswd)
            record.date_edited = finish_datetime()
            db.session.commit()
            #print(db.session.commit())
            flash('User updated succefully')
            return redirect(url_for('select_form_type'))
        else:
            return render_template('/edit/to_edit_users.html', form=form, record=record, cu_id=cu_id, admins=sys_admins)
    flash('you can\'t ;)')
    return(redirect(url_for('de_welcome')))

@app.route('/gs/select_query_type', methods=['POST', 'GET'])
@login_required
def querying_downloading():
    cu_id = current_user.id
    form = SelectQueringBase()
    if cu_id in sys_admins:
        if request.method == 'POST' and form.validate_on_submit:
            type = request.form['type']
            session['type'] = type
            if type == 'records':
                return redirect(url_for('querying'))
            elif type == 'columns':
                return redirect(url_for('querying'))
            elif type == 'cells':
                return redirect(url_for('querying'))
            else:
                return "Impossible"
        return render_template('/gs/select_query_type.html', form1=SelectQueringBase())
    flash("Only for admins")
    return redirect(url_for('welcome'))

@app.route('/gs/QueryRecords', methods=['POST', 'GET'])
@login_required
def querying():
    type = session['type'] #3anda 2este5demayn l 2awwal bt2akkid 2eno luser mara2 bl mar7le l 2abl l tene la nshouf shou nsewe
    cu_id = current_user.id
    form = QueryingRecordsTDateTime()
    #form0 = QueryingRecords
    #form1 = QueryingColumns
    #form2 = QueryingCells
    if cu_id in sys_admins:
        if type == 'records':
            if request.method == 'POST' and form.validate_on_submit:# and os.path.isfile("query.xlsx"):
                table = request.form['table']
                first_date = request.form['first_date']
                last_date = request.form['last_date']
                form.last_date.data = ""
                #first_time = request.form['first_time']
                #last_time = request.form['last_time']
                first_time= "05:05:05.111111"
                last_time = "13:33:33.333333"
                how_much = request.form['how_much']
                order = request.form['order']
                query_cmd = f"select * from {table} where date_added between '{first_date} {first_time}' and '{last_date} {last_time}' order by id {order} limit {how_much}"
                query = db.engine.execute(query_cmd)
                query_to_csv_excel(query_cmd)
                file = 'query.xlsx'
                file2 = 'query.csv'
                file_handle = open(file, 'r')
                return send_file(file, as_attachment=True)#, redirect(url_for('querying'))
                #return redirect(url_for('querying'))
            return render_template('/gs/querying.html', type=type, form=form) 
       # elif type == 'columns':

        #elif type == 'cells':
    flash("Only for admins")
    return redirect(url_for('welcome'))

@app.route('/data_entry/new_form/titles', methods=['POST', 'GET'])
@login_required
def new_form_titles():
    form = Titles()
    cu_id = current_user.id
    if cu_id in sys_admins:
        if request.method == 'POST':
            if form.validate_on_submit:
                form_title = request.form["form_title"]
                form_class = request.form["form_class"]
                table = request.form["table"]
                access_by = request.form["access_by"]
                session['form_ttl'] = form_title
                #create_template(form_title, form_class)
                #append_form_nav(form_title, form_class)
                #append_wtf_title(form_class)
                #append_db_class_title(form_class, table)
                #append_route(form_class)
                #organize_access(access_by)
                flash("Titles writed successfully")
                return redirect(url_for('new_form'))
            flash("not valide")
            return render_template('/data_entry/add_titles.html', form=form ,cu_id=cu_id)
        return render_template('/data_entry/add_titles.html', form=form ,cu_id=cu_id)
    flash("Only for admins")
    return redirect(url_for("de_welcome"))

@app.route('/data_entry/new_form', methods=['POST', 'GET'])
@login_required
def new_form():
    cu_id = current_user.id
    if cu_id in sys_admins:
        form1 = MakeForm()
        if request.method == 'POST':
            form_data = request.form['form_data']
            data_dict = json.loads(form_data)
            ttls = data_dict['titles']
            form_title = ttls[0]
            form_class = ttls[1]
            table = ttls[2]
            access_by = ttls[3]
            create_template(form_title, form_class)
            append_form_nav(form_title, form_class)
            append_wtf_title(form_class)
            append_db_class_title(form_class, table)
            append_route(form_class)
            organize_access(access_by)
            fields = data_dict['fields']
            for field in fields: #the field is the list inside the list
                field_name = field[0]
                flabel = field[1]
                field_type = field[2]
                in_req = field[3]
                regex = field[4]
                length = field[5]
                nb_range = field[6]
                min_nb = field[7]
                max_nb = field[8] 
                min_char = field[9]
                max_char = field[10]
                choices = field[11]
                possible_validators = [in_req, regex, length, nb_range, min_nb, max_nb, min_char, max_char]
                prpr_templ_flds(field_name, form_title, form_class)
                try:
                    track_fields(field_name) #ra7 n5alli bas kormel 2oset l duplication
                except IntegrityError:
                    flash("You can't give 2 fields the same name! It should be unique!")
                    return redirect(url_for("new_form"))
                except:
                    flash("You can't give 2 fields the same name! It should be unique!")
                    return redirect(url_for("new_form"))
                code = customize_wtf_fld_code(possible_validators, field_type, field_name, flabel, in_req, regex,
                                length, min_char, max_char, nb_range, min_nb, max_nb, choices)
                append_wtform(code)
                append_column(field_name, field_type)
                add_init_arg(field_name)
                append_init(field_type, field_name)
                set_psswd_func(field_type, field_name)
            #done funcs
            continue_dbmodel()
            write_requests(access_by)
            clear_track()
            write_return(access_by, form_title)
            notify_dev(form_title)
            rm_sended_templ(form_title)
            clear_sended_files()
            flash("The form has been addded successfully, it will take about 24h as max to be activated!")  
            return redirect(url_for("new_form"))
        return render_template('/data_entry/make_form.html', form=form1, cu_id=cu_id)
    flash(f"only for admins {cu_id} user")    
    return redirect(url_for('de_welcome'))
    
#!!!!la tnsa 2eno ba3d kol form vyen3amal badna flask migrate
@app.route('/data_entry/new_form/done', methods=['POST', 'GET'])
@login_required
def form_done():
    #continue_dbmodel()
    #count_fields()
    write_return(access_by, form_title)
    form_title = session['form_ttl']
    notify_dev(form_title)
    return "Done"

@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    flash("تم تسجيل الخروج")
    return redirect(url_for("login"))

@app.route('/admin/cookies')
@login_required
def cookies():
    cu_id = current_user.id
    if cu_id in sys_admins:
        role = ""
        if cu_id in sys_admins:
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
    return "only for admins!"
