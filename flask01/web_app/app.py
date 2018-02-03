from flask import Flask, render_template
from flask_admin import Admin
from web_app.models import db, Page, Menu
from flask_admin.contrib.sqla import ModelView

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    db.init_app(app)

    admin = Admin(app, name='beginflask', template_mode='bootstrap3')
    admin.add_view(ModelView(Page, db.session))
    admin.add_view(ModelView(Menu, db.session))

    @app.route('/')
    def index():
        page = Page.query.filter_by(id=1).first()
        content = 'empty'
        if page is not None:
            content = page.content

        return render_template('index.html', TITLE='Begin Flask', CONTENT=content)

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Begin Flask')

    return app


