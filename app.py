from flask import Flask, request, redirect, render_template, url_for, flash

from classes.user import User
from classes.bucketlist import bucketlist
from classes.item import Item

app = Flask(__name__)

Users = []


@app.route('/')
def main():
    """ Takes one to the landing page """
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register(sels, users):
    """ Enable user to register """
    if request.method == 'GET':
        return render_template('signup.html')

    elif request.method == 'POST':
        username = request.form['Username']
        email = request.form['Email']
        password = request.form['Password']
        newUser = User(username=username, email=email, password=password)

        Users.append(newUser)

        return redirect(url_for('sign_in'))


@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    """ Enable user to sign in """
    if request.method == 'GET':
        return render_template('signin.html')

    elif request.method == 'POST':
        email = request.form['Email']
        password = request.form['Password']
        checkUser = [
            emailobject for emailobject in Users if
            emailobject.email == email][0]
        if not checkUser:
            flash("Invalid email!")
            return render_template("signin.html")
        
        return redirect(url_for('view_bucketlists'))


@app.route('/bucketlists')
def view_bucketlists():
    """ View all bucketlists and perform CRUD operations """
    if session.get('user'):
        ideas = dbsession.query(Ideas).all()
        return render_template('userHome.html', ideas=ideas)
    else:
        return render_template('error.html', error='Unauthorized Access')


if __name__ == '__main__':
    app.run()
