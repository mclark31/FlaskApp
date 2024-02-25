from app import app
from flask import render_template, flash, redirect, request, url_for, jsonify
from app.forms import LoginForm

#routes – URLs where a flask app accepts requests
@app.route('/')
@app.route('/index')
#a view function – route handler
def index():    
    user = {'username': 'byan'}
    classes = [{'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},
        {'classInfo': {'code': 'CSC184', 'title': 'Python Programming'}, 'instructor': 'Evan Noynaert'}]    
    return render_template('index.html', title='Home', user=user, classes=classes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Welcome user {}! You opted for remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect('index')
    else:
        if request.args:
            flash('GET method now allowed for login!')
        # else:
        #     flash('No data in request!')

    return render_template('login.html', title='Sign In', form=form)





