# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from uuid import uuid4


app = Flask(__name__, static_url_path="/public", static_folder="public")

liste_articles = [
    {"title": "Cartes graphique", "prix": "700", "description": "Une carte graphique...", "img": "gpu.png"},
    {"title": "Disque dur", "prix": "300", "description": "Un disque dur...", "img": "hdd.jpg"},
    {"title": "Clavier", "prix": "7", "description": "Un clavier...", "img": "clavier.jpg"},
    {"title": "Souris", "prix": "6", "description": "Une souris...", "img": "souris.jpg"},
    {"title": "Pomme", "prix": "1200", "description": "Une pomme...", "img": "apple.jpg"},
]

@app.route("/")
def home():
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
    liste_articles.append({
        "title": request.form.get("titre"),
        "prix": request.form.get("prix"),
        "description": request.form.get("desc"),
        "img": filename
    })
    return redirect("/")

app.run(port=5000, debug=True)