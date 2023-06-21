from datetime import timedelta


DB_NAME : str = "note_db.sqlite3"

class Config: 
    SECRET_KEY : str = "HD734HDUF7HDJFI9HJHIDF"
    JWT_SECRET_KEY : str = "RUER734HHDF89213HUDVVIAWE"

    SQLALCHEMY_DATABASE_URI : str = f"sqlite:///{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False

    JWT_EXPIRATION_DELTA : timedelta = timedelta(days=1)