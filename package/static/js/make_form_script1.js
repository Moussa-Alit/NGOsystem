var ttls_arr = [];
function get_pass() {
    confirm("Are you sure?!\nYou will not be able to edit anything later!");
    let form_title = document.getElementById("form_title").value;
    let form_class = document.getElementById("form_class").value;
    let table = document.getElementById("table").value;
    let access_by = document.getElementById("access_by").value;
    ttls_arr = [form_title, form_class, table, access_by];
    document.getElementById("titles_div").style.display = "none";
    document.getElementById("fields_div").style.display = "block";
    console.log(ttls_arr)
};

function show_div() {
    if (document.getElementById("field_type").value == "StringField") { 
        document.getElementById("str_vali").style.display = "block" 
        if (document.getElementById("for_nb_range").style.display = "block" || document.getElementById("input-group-hm").style.display == "block" || document.getElementById("nb_range").style.display == "block") {
        document.getElementById("for_nb_range").style.display = "none"
        document.getElementById("nb_range").style.display = "none"
        document.getElementById("input-group-hm").style.display = "none"
        document.getElementById("input-group-nb-rg").style.display = "none"
    }
    } else if (document.getElementById("field_type").value == "IntegerField") {
        document.getElementById("nb_range").style.display = "block"
        document.getElementById("for_nb_range").style.display = "block"
        if (document.getElementById("str_vali").style.display = "block" || document.getElementById("input-group-hm").style.display == "block") {
            document.getElementById("str_vali").style.display = "none"
            document.getElementById("input-group-hm").style.display = "none"
    }
    } else if (document.getElementById("field_type").value == "SelectField" || document.getElementById("field_type").value == "RadioField") {
        document.getElementById("input-group-hm").style.display = "block"
        document.getElementById("hm_choices_id").required = true;
        if (document.getElementById("str_vali").style.display = "block" ||  document.getElementById("nb_range").style.display == "block") {
            document.getElementById("str_vali").style.display = "none"
            document.getElementById("input-group-nb-rg").style.display = "none"
            document.getElementById("for_nb_range").style.display = "none"
            document.getElementById("nb_range").style.display = "none" 
       }
    } else if (document.getElementById("field_type").value == "PasswordField") {
        document.getElementById("in_req").setAttribute('required', '')
        document.getElementById("str_vali").style.display = "none"
        document.getElementById("input-group-nb-rg").style.display = "none"
        document.getElementById("for_nb_range").style.display = "none"
        document.getElementById("nb_range").style.display = "none"
        document.getElementById("input-group-hm").style.display = "none"
    }
    else {
        document.getElementById("str_vali").style.display = "none"        
        document.getElementById("input-group-str-len").style.display = "none"
        document.getElementById("input-group-nb-rg").style.display = "none"
        document.getElementById("for_nb_range").style.display = "none"
        document.getElementById("nb_range").style.display = "none"
        document.getElementById("input-group-hm").style.display = "none" 
    }
};
function set_length() {
    if (document.getElementById("length").value == "yes") {
        document.getElementById("input-group-str-len").style.display = "block"
    } else {
        document.getElementById("input-group-str-len").style.display = "none"
    }
};
function set_nb_range() {
    if (document.getElementById("nb_range").value == "yes") {
        document.getElementById("input-group-nb-rg").style.display = "block"
    } else {
        document.getElementById("input-group-nb-rg").style.display = "none"
    } 
};
function generate_choices() {
    if (document.getElementById("choice1")) {
        //removechilds()
        const parent_div = document.getElementById("choices_div");
        parent_div.innerHTML = ''
        /*while (parent_div.firstChild) {
            parent.removeChild(parent.lastChild);
        }*/
    }
    //alert("Don't make the field before seting the choices and values!!!!") //these fields are already required
    let x = document.getElementById("hm_choices_id").value;
    var choices = document.getElementById("choices_div");
    var btn = document.createElement('button');
        btn.setAttribute('type', 'button');
        btn.setAttribute('onclick', 'make_dict(); ');
        btn.setAttribute('class', 'btn btn-info')
        btn.innerHTML = '   SET   ';
    for (let i=0; i < x; i++) {
        var choice_label = document.createElement('label');
        choice_label.innerHTML = `Choice ${i+1}`;
        choice_label.setAttribute('class', 'form-label');
        var choice = document.createElement('input');
        choice.setAttribute('type', 'text');
        choice.setAttribute('name', `choice ${i+1}`);
        choice.setAttribute('id', `choice${i+1}`);
        choice.setAttribute('class', 'form-control');
        choice.setAttribute('required', '');
        var value_label = document.createElement('label');
        value_label.setAttribute('class', 'form-label');
        value_label.innerHTML = `Value ${i+1}`;
        var ch_value = document.createElement('input');
        ch_value.setAttribute('type', 'text');
        ch_value.setAttribute('name', `ch_value${i+1}`);
        ch_value.setAttribute('id', `ch_value${i+1}`);
        ch_value.setAttribute('class', 'form-control');
        ch_value.setAttribute('required', '');
        
        choices.appendChild(choice_label);
        choices.appendChild(choice);
        choices.appendChild(value_label);
        choices.appendChild(ch_value);
        
        
    }
    choices.appendChild(btn)
};

var choices_dict = {};
function make_dict() { 
    //var choices_dict = {};
    if (choices_dict) {
        choices_dict = {};
        var parent = document.getElementById("choices_div");
        var ch_val_list = parent.children;
        for (let i=0; i < ch_val_list.length; i++) {
            if (i % 4 == 1) {
                let c = i + 2;
                var choice = ch_val_list[i].value;
                var value = ch_val_list[c].value;
                choices_dict[choice] = value;
            } else {
                continue;
            } 
        }
        Object.keys(choices_dict).every ( value => {
            if (!value) {
                confirm("Be carefull you should fill the choices and values")
            } else {
                alert("Choices setted successfully")
            }
        })
    } else {  
        var parent = document.getElementById("choices_div");
        var ch_val_list = parent.children;
        for (let i=0; i < ch_val_list.length; i++) {
            if (i % 4 == 1) {
                let c = i + 2;
                var choice = ch_val_list[i].value;
                var value = ch_val_list[c].value;
                choices_dict[choice] = value;
            } else {
                continue;
            } 
        }
        Object.keys(choices_dict).every ( value => {
            if (!value) {
                confirm("Be carefull you should fill the choices and values")
            } else {
                alert("Choices setted successfully")
            }
        })
    }
    console.log(choices_dict);
    /*let choices = JSON.stringify(choices_dict);
    var hidden_choices = document.getElementById("hidden_choices");
    hidden_choices.value = choices;*/
    const parent_div = document.getElementById("choices_div");
    while (parent_div.firstChild) {
        parent.removeChild(parent.lastChild);
    }
};
var flds_arr = [];

function push_field() {
    document.getElementById("input-group-nb-rg").style.display = "none";
    document.getElementById("input-group-str-len").style.display = "none";
    document.getElementById("input-group-hm").style.display = "none";
    document.getElementById("is_nb_rg").style.display = "none";
    document.getElementById("str_vali").style.display = "none";
    let field_name = document.getElementById("field_name").value;
    let flabel = document.getElementById("flabel").value;
    let field_type = document.getElementById("field_type").value;
    let in_req = document.getElementById("in_req").value;
    let regex = document.getElementById("regex").value;
    let length = document.getElementById("length").value;
    let nb_range = document.getElementById("nb_range").value;
    let min_nb = document.getElementById("min_nb").value;
    let max_nb = document.getElementById("max_nb").value;
    let min_char = document.getElementById("min_char").value;
    let max_char  = document.getElementById("max_char").value;
    var fld_arr = [field_name, flabel, field_type, in_req, regex, length, nb_range, min_nb, max_nb, min_char, max_char, choices_dict];
    flds_arr.push(fld_arr)
    console.log(flds_arr)
    console.log(fld_arr)
    document.getElementById("field_name").value = ""
    document.getElementById("flabel").value = ""
    document.getElementById("field_type").value = ""
    document.getElementById("in_req").value = ""
    document.getElementById("regex").value = ""
    document.getElementById("length").value = ""
    document.getElementById("nb_range").value = ""
    document.getElementById("min_nb").value = ""
    document.getElementById("max_nb").value = ""
    document.getElementById("min_char").value = ""
    document.getElementById("max_char").value = ""
};

function confirm_send() {
    const form_objct = {"titles": ttls_arr, "fields": flds_arr};
    confirm("You will not be able to add more fields!!!\n Are you sure that you have finished making this form?")   
    let data = JSON.stringify(form_objct);
    document.getElementById("form_data").value = data;
    /*fetch('/data_entry/new_form', {
        method:'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8'
        },
        body: JSON.stringify(form_objct)

    }).then( res => res.json())
      .then(data => console.log(data))
      .catch(error => console.log(error));*/
    /*var form_data_tag = document.getElementById("form_data");
    form_data_tag.value = data;**/
    // Creating a XHR object
    /*let xhr = new XMLHttpRequest();
    let url = '{{ url_for("new_form") }}';

    // open a connection
    xhr.open("POST", url, true);

    xhr.setRequestHeader("Content-Type", 'application/json; charset=utf-8');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert("w 2ayr")
        }
    let form_objct = {"titles": ttls_arr, "fields": flds_arr};
    let data = JSON.stringify(form_objct);

    xhr.send(data);
    }*/
};

function removechilds() {
    const parent_div = document.getElementById("choices_div");
    while (parent_div.firstChild) {
        parent.removeChild(parent.lastChild);
    }
};
