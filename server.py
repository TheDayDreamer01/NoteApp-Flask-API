from App import create_note_app
from flask import Flask
from App.config import (
    ProductionEnvironment,
    DevelopmentEnvironment,
    TestEnvironment
)


config : object = None
environment : str = "DEVELOPMENT"

match environment:
    case "DEVELOPMENT":
        config = DevelopmentEnvironment()

    case "PRODUCTION":
        config = ProductionEnvironment()

    case "TESTING":
        config =  TestEnvironment()


app : Flask = create_note_app(config)

if __name__ == "__main__":
    app.run(debug=True)