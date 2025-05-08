from flask import (
    Blueprint, request, flash, render_template
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        # TODO: Ensure that usernames and passwords are valid
        # TODO: Ensure that the username doesn't already exist

        if error is None:
            # TODO: Change this to redirect to the login page
            flash('Registration is successful!')

        flash(error)
    
    return render_template('auth/register.html')