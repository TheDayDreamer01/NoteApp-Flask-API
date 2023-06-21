from datetime import timedelta


DB_NAME : str = "note_db"

class Config: 

    """
    - Uncomment the line below depending on your database preference
    - Line 22 : SQLite3 Database
    - Line 23 : MySQL Database

    By default SQLite3 is used
    """

    SECRET_KEY : str = "HD734HDUF7HDJFI9HJHIDF"
    JWT_SECRET_KEY : str = "RUER734HHDF89213HUDVVIAWE"

    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False
    
    SQLALCHEMY_DATABASE_URI : str = f"sqlite:///{DB_NAME}.sqlite3"
    # SQLALCHEMY_DATABASE_URI : str = f"mysql://root:data@localhost:3306/{DB_NAME}"

    JWT_EXPIRATION_DELTA : timedelta = timedelta(days=1)