from flask import render_template, redirect, flash, url_for
from werkzeug.utils import secure_filename

from app.models import Sploit

from app import db
from app.main import bp
from app.main.forms import LoginForm, SploitForm
from app.auth import login_required


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@login_required
@bp.route('/sploits', methods=['GET', 'POST'])
def sploits():
    form = SploitForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads/' + filename)
        sploit = Sploit(path=('uploads/' + filename), name=form.name.data)
        db.session.add(sploit)
        db.session.commit()
        flash('Sploit uploaded!')

    sploits = Sploit.query.all()

    return render_template('sploits.html', title='Sploits', 
            form=form, sploits=sploits)


@login_required
@bp.route('/remove_sploit/<int:id>')
def remove_sploit(id):
    Sploit.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Sploit removed!')
    return redirect(url_for('main.sploits'))


@bp.route('/teams')
def teams():
    return render_template('teams.html')
