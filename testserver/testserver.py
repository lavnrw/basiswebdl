#!/usr/bin/python3

# Running:
# $ FLASK_APP=testserver flask run

from flask import Flask, send_file

app = Flask(__name__)


@app.route("/landesarchiv/login", methods=["POST"])
def login():
    return "dummytoken"


@app.route("/landesarchiv/export/<prison>")
def export(prison):
    return send_file("example.zip")


@app.route("/landesarchiv/reexport/<guid>")
def reexport(guid):
    # A reexported rueckgrat.xml has no element "/rueckgrat/Header/Jva", so
    # this file actually does not contain correct example data, but never mind.
    return send_file("example.zip")


@app.route("/landesarchiv/commit/<guid>", methods=["PUT"])
def commit(guid):
    return "", 200
