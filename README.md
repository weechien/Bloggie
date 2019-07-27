# MyFlaskJournal 📖

A blog-publishing website to share your tech-related opinions and findings:

https://myapplicationfinal.herokuapp.com/

## Project Description
MyFlaskJournal is a web app for people to post their thoughts and research on matters related to technology. Our goal is to enable like-minded people to share ideas and the latest news in technology with each other in an easy way. Topics include Programming, Science, Machine Learning and Other Tech. MyFlaskJournal is designed with ease of use in mind ⁠— register and login easily, view posts from a specific user or category, publish, update or delete posts with a click of a button. These conveniences are possible thanks to the integrated Flask framework.

## Features
* Publish, update and delete posts.
  * Registered users may publish new posts which will appear on the home page.
  * Users may only edit and delete their own posts by clicking on the post title.
* View paginated posts.
  * Only the links for the current, left, right, first and last pages are shown.
* Filter posts by author and category.
  * View posts published by a specific user by clicking on the author's name in a post.
  * View posts filtered by category by clicking on the side bar to the right.
* Register and login user.
  * The password must contain at least:
    * 8 characters
    * 1 numeric character
    * 1 uppercase letter
    * 1 lowercase letter
    * 1 special character
  * Users are required to login after registration.
* Update user's email, username and profile picture.
  * The selected picture will be resize and the old picture will be removed from the server.
* Reset password via email.
  * An email with a timed token will be sent to the user's email address.
  * The user will be redirected to reset their password upon clicking on the link in the email.

## Built With

* [Flask](https://palletsprojects.com/p/flask/) - Web framework used
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - User session management
* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) - Hashing utilities
* [Flask-Mail](https://pythonhosted.org/Flask-Mail/) - SMTP setup for email transmission
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - Database utilities
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) - Form input handling and validation
* [Jinja2](http://jinja.pocoo.org/docs/2.10/) - Templating language for Python
* [Pillow](https://pillow.readthedocs.io/en/stable/) - Image processing and manipulation
* [itsdangerous](https://pythonhosted.org/itsdangerous/) - Data handling in untrusted environments

## Acknowledgments

* Corey Schafer on YouTube
* Authors of the libraries used in this app
* CS50 staff on edX and Reddit
