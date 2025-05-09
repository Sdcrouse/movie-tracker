import re

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

        if error is None:
            valid_email_pattern = re.compile("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

            if not valid_email_pattern.fullmatch(email):
                error = 'Invalid email address.'

        # TODO: Ensure that passwords are valid
        # TODO: Ensure that the email doesn't already exist

        if error is None:
            # TODO: Change this to redirect to the login page
            flash('Registration is successful!')

        flash(error)
    
    return render_template('auth/register.html')