# NoteApp API

This repository contains a simple NoteApp API developed using Python and the Flask framework. It provides basic CRUD (Create, Read, Update, Delete) operations for managing notes. The API is built with the following Python libraries: Flask, Flask-Restful, Flask-SQLAlchemy, Flask-JWT-Extended, Flask-Marshmallow, Flask-Cors, Flask-Bcrypt, and MySQLclient.

## Features

- User authentication and authorization
- User management (update password, get user information, update user information, delete user account)
- Note management (create note, get all notes of a user, get specific note information, update note, delete note)
- Unit testing

## Prerequisites

To run this API locally, you need to have the following dependencies installed:

- Python (version >= 3.6)
- Flask (version >= 2.0.0)
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flask-Marshmallow
- Flask-Cors
- Flask-Bcrypt
- MySQLclient

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/TheDayDreamer01/NoteApp-Flask-API.git
   ```
2. Change into the project's directory.
   ```bash
   cd noteapp-flask-api
   ```
3. (Optional) Create a virtual environment.
   ```bash
   virtualenv env
   source venv/bin/activate
   ```
4. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```
5. Start the API server.
   ```bash
   python server.py
   ```

By default, the API will use SQLite3 as the database for the development and testing environment. If you want to use MySQL for the production environment, please update the database configuration accordingly in the `./App/config.py`.

## API Routes

The following routes are available in the NoteApp API:

### Authentication

- `POST /api/auth/signin`: Login a user
- `POST /api/auth/signup`: Sign up a user
- `POST /api/auth/signout`: Sign out the current user
- `POST /api/auth/refresh`: Refresh access token using refresh token
- `POST /api/auth/refresh/signout`: Sign out using the refresh token

### User Management

- `POST /api/user/<user_id>`: Update user password
- `GET /api/user/<user_id>`: Get current user information
- `PUT /api/user/<user_id>`: Update basic information of the user
- `DELETE /api/user/<user_id>`: Delete the user account

### Note Management

- `GET /api/note/<user_id>`: Get all notes of the current user
- `POST /api/note/<user_id>`: Create a new note
- `GET /api/note/<note_id>/<note_title>/<user_id>`: Get specific information of a note
- `PUT /api/note/<note_id>/<note_title>/<user_id>`: Update a note
- `DELETE /api/note/<note_id>/<note_title>/<user_id>`: Delete a note

## Unit Testing

Unit tests for the NoteApp API are located in the `Test` directory. To run the tests, execute the following command:

```shell
python -m unittest discover -s Test
```

## Contributing

Contributions to this NoteApp API are welcome! If you find any issues or want to suggest improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per your needs.
