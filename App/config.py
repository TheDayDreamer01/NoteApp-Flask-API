from datetime import timedelta
from App.utils import secretKeyGenerator


DB_NAME : str = "note_db"


class ProductionEnvironment:

    DEBUG : bool = False
    JWT_BLACKLIST_ENABLED : bool = True

    SECRET_KEY : str = secretKeyGenerator(20)
    JWT_SECRET_KEY : str = secretKeyGenerator(20)

    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False
    SQLALCHEMY_DATABASE_URI : str = f"mysql://<user>:<password>@localhost:3306/{DB_NAME}"

    JWT_ACCESS_TOKEN_EXPIRES : timedelta = timedelta(days = 1)



class DevelopmentEnvironment:

    DEBUG : bool = True
    JWT_BLACKLIST_ENABLED : bool = True

    SECRET_KEY : str = secretKeyGenerator(10)   
    JWT_SECRET_KEY : str = secretKeyGenerator(10)

    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False
    SQLALCHEMY_DATABASE_URI : str = f"sqlite:///{DB_NAME}.sqlite3"

    JWT_ACCESS_TOKEN_EXPIRES : timedelta = timedelta(days = 1)


class TestEnvironment:
    pass