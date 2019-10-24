# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect


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
    print(request.form.get("titre"))
    return redirect("/")

app.run(port=5000, debug=True)