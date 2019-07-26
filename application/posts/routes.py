from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from application import db
from application.models import Post, User
from application.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    category=dict(form.category.choices).get(form.category.data),
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('posts/post_form.html', title='New Post', form=form)


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    form.submit.label.text = 'Update'
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.category = dict(form.category.choices).get(form.category.data)
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.category.data = post.category[0]
    return render_template('posts/post_form.html', title='Update Post', form=form)


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.index'))


@posts.route('/post/<string:category>')
def category_posts(category):
    page = request.args.get('page', 1, type=int)
    posts = Post.query\
        .filter_by(category=category)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    print('posts', posts.items)
    if not posts.items:
        return render_template('posts/no_post.html', category=category)
    users = [User.query\
        .filter(User.posts.contains(post))
        .all() for post in posts.items]
    print('users', users)
    return render_template('posts/category_posts.html', posts=posts, users=users)
