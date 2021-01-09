from flask_frozen import Freezer
from run import app

if __name__ == '__main__':

    # settings
    app.config['FREEZER_RELATIVE_URLS'] = True

    # freeze
    freezer = Freezer(app)
    freezer.freeze()