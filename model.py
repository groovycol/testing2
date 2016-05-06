from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    #FIXME: write a function that creates a game and adds it to the database.
    n1 = Game(name="Twister", description="ties you up in knots")  
    n2 = Game(name="Battleship", description="you sunk my Battleship!")  
    n3 = Game(name="Connect-four", description="pretty sneaky sis")  
    n4 = Game(name="Pente", description="how to lose tiny marbles in your house")  

    db.session.add_all([n1, n2, n3, n4])
    db.session.commit()

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
 