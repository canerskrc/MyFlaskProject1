from flask import Flask,render_template,redirect,url_for,request, make_response, session,abort
from .session_interface import MySessionInterface
from itsdangerous import Signer, BadSignature
app = Flask(__name__)
app.secret_key = b"?051kjasd__"
app.session_interface = MySessionInterface()
# app.run() Çalıştırma seçeneği

def get_current_username():
      email = ""
      login_auth = False
      if 'email' in session:
            email = session['email']
            login_auth = True
      return email, login_auth

@app.route("/")
def Index():
      email, login_auth = get_current_username()
      return render_template("index.html", email=email, login_auth=login_auth)

@app.route("/contact")
def Contact():
      email, login_auth = get_current_username()
      return render_template("contact.html", email=email, login_auth=login_auth)


@app.route("/contactlist")
def ContactList():
      email, login_auth = get_current_username()
      return render_template("contact_list.html",email=email, login_auth=login_auth)

# kullanıcıyı login işleminden sonra sayfalara yönlendiren fonksiyonlar...
@app.route("/login", methods=['GET','POST'])
def Login():
      if request.method == 'POST':
            if request.form:
                  if 'email' in request.form and 'password' == request.form:
                        email = request.form['email']
                        password = request.form['password']
                        if email == 'admin' and password == 'admin':
                              session['email']=email
                              return redirect(url_for('Index'))
                        else:
                              return redirect(url_for('Login'))
            abort(400)
#abort parametresini sayfanın en üst kısmından dahil etmemiz gerekiyor.
      email, login_auth = get_current_username()
      return render_template("login.html", email = email, login_auth=login_auth)

