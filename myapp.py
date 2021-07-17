from flask import Flask,render_template,redirect,flash,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.secret_key="gourav"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqllite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)


class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    message=db.Column(db.String(50))


@app.route("/")
def home():
    
    profiles={"name":"gourav","last":"agarwal"}
    return render_template ("home.html",profile=profiles)

@app.route("/about/")
def about():
    return render_template ("about.html")

@app.route("/acheivement/")
def acheivement():
    return render_template ("acheivement.html")
@app.route("/contact/",methods=["GET","POST"])
def contact():
    if request.method=="POST":
        email=request.form["email"]
        message=request.form["message"]
        contact=Contact(email=email,message=message)
        db.session.add(contact)
        db.session.commit()
        flash("added")
        return redirect("/")
    return render_template ("contact.html")


if __name__=="__main__":
    app.run(debug=True)
