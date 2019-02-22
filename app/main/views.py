from flask import Flask, render_template, Response
from . import main
from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from flask.views import View, MethodView
from .. import db
from datetime import datetime
from ..request import get_books


@main.route('/')
def index():

    return render_template('index.html')


@main.route('/goodbooks')
def goodbooks():

    result = get_books()

    return render_template('goodbooks.html', books = result)

