from flask import Flask
from apps.front import front_bp
from apps.cms import cms_bp
from apps.ueditor import ueditor_bp
from exts import db
import config



def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(front_bp)
    app.register_blueprint(cms_bp)
    app.register_blueprint(ueditor_bp)

    db.init_app(app)

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,port=6000)
