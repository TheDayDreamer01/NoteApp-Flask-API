from App import create_note_app
from flask import Flask
from Config import (
    ProductionEnvironment,
    DevelopmentEnvironment,
    TestEnvironment
)


ENVIRONMENT : str = "DEVELOPMENT"
config : object = DevelopmentEnvironment()

match ENVIRONMENT:
    case "PRODUCTION":
        config = ProductionEnvironment()

    case "TESTING":
        config =  TestEnvironment()

    case _:
        config = DevelopmentEnvironment()


app : Flask = create_note_app(config)

if __name__ == "__main__":
    
    match ENVIRONMENT:
        case "PRODUCTION": 
            app.run()

        case _:
            app.run(debug=True, host="0.0.0.0")