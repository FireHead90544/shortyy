from flask import Flask, request, render_template, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import base64
import json


with open('config.json', 'r') as c:
    params = json.load(c)["params"]
local_server = False

# DB_NAME = urlshortner, TABLE_NAME = links, COLUMNS = url_slug, original_url

app = Flask(__name__)

app.secret_key = "application-secret-key"
app.config['SQLALCHEMY_DATABASE_URI'] = params['db_uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Links(db.Model):
    url_slug = db.Column(db.String(100), primary_key=True, nullable=False)
    original_url = db.Column(db.String(1000), nullable=False)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(503)
def page_not_found(e):
    return "503 | Database Server Error | Please Try Again Later", 503

@app.errorhandler(500)
def page_not_found(e):
    return "500 | Internal Server Error | Please Try Again Later", 503       


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/static")
@app.route("/static/")
def block_static():
    return render_template("404.html")    

@app.route("/login", methods=["GET", "POST"])
def login():
    if ('user' in session and session["user"] == params["admin_user"]):
        links = Links.query.all()
        return redirect("/dashboard")

    if request.method == "GET":
        return render_template("login.html")    
    elif request.method == "POST":
        return redirect("/dashboard")
    else:
        return "Method Not Supported!"
        


@app.route("/<string:slug>")
def shortened(slug):
    slug = slug.lower()
    link = Links.query.filter_by(url_slug=slug).first()
    if link == None:
        return render_template("404.html")
    redirect_url = link.original_url
    return redirect(f"{redirect_url}")



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return redirect("/")

    elif request.method == "POST":
        url = request.form.get('url')
        slug = request.form.get('slug').lower()
        slug = ''.join(e for e in slug if e.isalnum())
        slug = slug.replace(" ", "")

        if slug.lower() in ['login', 'add', 'logout', 'delete', 'dashboard']:
            flash("red")
            flash("Error")
            flash("Cannot Add A System Used Slug! Try Another Slug!")
            return redirect(url_for("home"))

        if len(slug) == 0:
            flash("red")
            flash("Error")
            flash("Enter A Valid Slug!")
            return redirect(url_for("home"))

        links = Links.query.filter_by(url_slug=slug).all()
        if len(links) == 0:
            link = Links(url_slug=slug, original_url=url)
            db.session.add(link)
            db.session.commit()
            flash("green")
            flash("Success")
            flash("Shortened your url as:")
            flash(f"shortyy.ml/{slug}")
            return redirect(url_for("home"))
        else:
            flash("red")
            flash("Error")
            flash("That Slug Is Already Used! Try Another Slug!")
            return redirect(url_for("home"))
   
    else:
        return "Method Not Supported!"  


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route("/delete/<string:slug>", methods=["GET", "POST"])
def delete(slug):
    if ('user' in session and session['user'] == params['admin_user']):
        link = Links.query.filter_by(url_slug=slug).first()
        db.session.delete(link)
        db.session.commit()
    return redirect('/dashboard')    



@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if ('user' in session and session["user"] == params["admin_user"]):
        links = Links.query.all()
        return render_template("dashboard.html", params=params, links=links)

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username == params['admin_user'] and password == params['admin_password']):
            session['user'] = username
            links = Links.query.all()
            return render_template('dashboard.html', params=params, links=links)

    return render_template('login.html', params=params)        

if __name__ == "__main__":
    app.run(debug=True)
