from flask import (
    Blueprint, request, flash, render_template
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        # TODO: Ensure that emails and passwords are valid
        # TODO: Ensure that the email doesn't already exist

        if error is None:
            # TODO: Change this to redirect to the login page
            flash('Registration is successful!')

        flash(error)
    
    return render_template('auth/register.html')