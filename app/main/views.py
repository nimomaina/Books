from flask import Flask, render_template
from . import main
from .forms import BookForm, CommentForm,UpdateProfile, UpdateForm

from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Book, User, Review
from flask.views import View, MethodView
from .. import db, photos
from datetime import datetime



@main.route("/")
def index():
    return render_template('index.html')


@main.route('/all_books')
def book():
    books = Book.query.order_by(Book.id.desc())
    return render_template('all_books.html', books=books)



@main.route('/primary', methods=['GET', 'POST'])
def primary():
    book = Book.query.filter_by().first()
    ptextbook = Book.query.filter_by(category="ptextbook")
    return render_template('categories/primary.html', book=book, ptextbook=ptextbook)

@main.route('/secondary', methods=['GET', 'POST'])
def secondary():
    book = Book.query.filter_by().first()
    stextbook= Book.query.filter_by(category="stextbook")

    return render_template('categories/secondary.html', stextbook=stextbook, book=book)

@main.route('/novel', methods=['GET', 'POST'])
def novels():
    book = Book.query.filter_by().first()
    novel = Book.query.filter_by(category="novels")

    return render_template('categories/novel.html', book=book, novel=novel)

@main.route('/other', methods=['GET', 'POST'])
def other():
    other= Book.query.filter_by(category="other")
    book = Book.query.filter_by().first()
    return render_template('categories/other.html', book=book, other=other)

@main.route('/books/new/', methods=['GET', 'POST'])
@login_required
def new_book():
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        publisher = form.publisher.data

        print(current_user._get_current_object().id)
        if "photo" in request.files:
            pic = photos.save(request.files["photo"])
            file_path = f"photos/{pic}"
            book_pic = file_path

        new_book= Book(owner_id=current_user._get_current_object().id, category=category,title=title,publisher=publisher
                        ,book_pic=book_pic )
        db.session.add(new_book)
        db.session.commit()
        flash('New book uploaded','success')

        return redirect(url_for('main.book'))
    return render_template('new_book.html', form=form)


@main.route('/books/<int:book_id>',methods = ["GET","POST"])
def view_book(book_id):
    book = Book.query.filter_by(id=book_id).first()

    return render_template("books.html",book=book)


@main.route('/getbooks/<int:book_id>',methods = ["GET","POST"])
def get_book(book_id):
    book = Book.query.filter_by(id=book_id).first()

    return render_template("profile/profile.html",book=book)



@main.route("/update/<book_id>", methods= ['GET', 'POST'])
@login_required
def update_book(book_id):
    book = Book.query.filter_by(id = book_id).first()
    form = UpdateForm()
    if form.validate_on_submit():
        book.title = form.title.data

        db.session.commit()
        flash('Changes saved', 'success')
        return redirect(url_for('main.book'))
    elif request.method == 'GET':
        form.title.data = book.title



    return render_template('new_book.html', form=form)

# @main.route("/delete/<book_id>",methods = ['GET','POST'])
# def delete(book_id):
#     book = Book.query.filter_by(id=book_id).first()
#     db.session.delete(book)
#     db.session.commit()
#
#     return redirect(url_for('main.book'))




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


