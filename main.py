from App import create_note_app
from flask import Flask


app : Flask = create_note_app()

if __name__ == "__main__":
    # Development Environment
    # app.run(debug=True, host="0.0.0.0")
    
    # Production Environment
    app.run()