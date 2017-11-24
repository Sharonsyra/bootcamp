from flask import Flask, request, redirect, render_template, url_for, flash, session
import os
import arrow

from classes.user import User
from classes.bucketlist import Bucketlist
from classes.item import Item

app = Flask(__name__)
app.secret_key = os.urandom(20)

Users = []
Bucketlists = []
Items = []


@app.route('/')
def main():
    """ Takes one to the landing page """
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Enable user to register """
    if request.method == 'GET':
        return render_template('signup.html')

    else:
        username = request.form['inputUsername']
        email = request.form['inputEmail']
        password = request.form['inputPassword']

        if username in [usernameobject.username for usernameobject in Users]:
            flash("Username already exists!")
            return redirect(url_for('register'))
        elif email in [emailobject.email for emailobject in Users]:
            flash("Email already exists!")
            return redirect(url_for('register'))
        elif len(password) < 6:
            flash("Password must be at least six characters!")
            return redirect(url_for('register'))

        new_user = User(username=username, email=email, password=password)

        flash("User registered successfully!")
        Users.append(new_user)
        session['username'] = new_user.username

        return redirect(url_for('bucketlists'))


@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    """ Enable user to sign in """
    if request.method == 'GET':
        return render_template('signin.html')

    elif request.method == 'POST':
        email = request.form['inputEmail']
        password = request.form['inputPassword']
        check_user = [
            userobject for userobject in Users if
            userobject.email == email and userobject.password == password]
        if not check_user:
            flash("Invalid email or password!")
            return render_template("signin.html")
        session['username'] = check_user[0].username
        return redirect(url_for('bucketlists'))


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    """ User's profile details """
    return render_template('profile.html')


@app.route('/create_bucket', methods=['GET', 'POST'])
def create_bucket():
    """Create new bucketlists"""
    if 'username' in session:
        if request.method == 'GET':
            return render_template('create_bucket.html')
        elif request.method == 'POST':
            name = request.form['name']
            if name in Bucketlists:
                flash("Bucketlist name already exists!")
            description = request.form['description']
            time = arrow.utcnow()
            date_created = time.humanize()
            date_modified = time.humanize()
            new_bucket = Bucketlist(name=name, description=description, date_created=date_created,
                                    date_modified=date_modified)
            flash("Bucketlist added successfully!")
            Bucketlists.append(new_bucket)
            return redirect('bucketlists')
    flash('You are not logged in. Please login or register!')
    return redirect('/')


@app.route('/bucketlists', methods=['GET', 'POST'])
def bucketlists():
    """ View all bucketlists and perform CRUD operations """
    if 'username' in session:
        if request.method == 'GET':
            buckets = [bucketlists for bucketlists in Bucketlists]
            return render_template('home.html', buckets=buckets)
    flash('You are not logged in. Please login or register!')
    return redirect('/')


@app.route('/bucketlists/<int:bucket_id>', methods=['GET', 'PUT'])
def edit_bucket(bucket_id):
    if 'username' in session:
        one_bucket = [bucketobject for bucketobject in
                      Bucketlists if bucketobject.id == bucket_id][0]
        if request.method == 'GET':
            return redirect('edit_bucket.html', bucket=one_bucket)
        elif request.method == 'PUT':
            name = request.form['name']
            one_bucket = name
    flash('You are not logged in. Please login or register!')
    return redirect('/')


@app.route('/items', methods=['GET', 'POST', 'PUT', 'DELETE'])
def items():
    """ View all bucketlists and perform CRUD operations """
    if 'username' in session:
        if request.method == 'GET':
            return render_template('items.html')
        elif request.method == 'POST':
            pass
        elif request.method == 'PUT':
            pass
        elif request.method == 'DELETE':
            pass
    flash('You are not logged in. Please login or register!')
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    app.run()
