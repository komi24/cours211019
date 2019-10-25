# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from uuid import uuid4
from models import db
from models.Article import Article
import os



app = Flask(__name__, static_url_path="/public", static_folder="public")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courspython.sqlite3"

with app.app_context():
    db.init_app(app)
    db.create_all()


@app.route("/")
def home():
    liste_articles = Article.query.all()
    return render_template("index.html", articles=liste_articles)

@app.route("/contacts/<name>")
def contact(name):
    return f"Les contacts de {name}"

@app.route("/form", methods=["POST"])
def form():
    """
        Rajouter dans votre lsite_articles
        un article du formulaire (titre, prix...)
    """
    file_img = request.files["img"]
    filename = str(uuid4()) + file_img.filename
    file_img.save(f"public/images/{filename}")
    article = Article(
        titre=request.form.get("titre"),
        prix=request.form.get("prix"),
        description=request.form.get("desc"),
        location=request.form.get("location"),
        image=filename
    )
    db.session.add(article)
    db.session.commit()
    return redirect("/")

@app.route("/delete/<idx>")
def delete(idx):
    # article = Article.query.filter_by(id = id).first()
    article = Article.query.filter(Article.id == idx).first()
    db.session.delete(article)
    db.session.commit()
    os.remove("./public/images/" + article.image)
    return redirect("/")

@app.route("/article/<idx>")
def page_article(idx):
    article = Article.query.filter(Article.id == idx).first()
    return render_template("article.html", article=article)


app.run(port=5000, debug=True)