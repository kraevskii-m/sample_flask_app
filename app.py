from random import randint

from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('store', None)
    return redirect(url_for('index'))


@app.route('/random')
def random():
    if 'username' in session:
        temp = str(randint(0, 1000))
        if 'store' in session:
            session['username' + 'store'].append(temp)
            session.modified = True
        else:
            session['store'] = [temp]
        return temp
    return 'You are not logged in'


@app.route('/history')
def history():
    if 'username' in session:
        out = session['store']
        return "\n".join(out)
    return 'You are not logged in'


if __name__ == '__main__':
    app.run()
