# NoteApp Flask API

The NoteApp API is a backend API developed in Flask, offering user authentication, user manipulation, and CRUD operations for notes. It is designed to be versatile and can be integrated into mobile, GUI, and web applications.

## Features

- User authentication with JWT (JSON Web Tokens) for secure access.
- User manipulation functionalities, including:
  - Retrieving user information.
  - Deleting user accounts.
  - Updating user profiles.
  - Updating user passwords.
- CRUD operations for notes, including:
  - Retrieving notes.
  - Creating new notes.
  - Updating existing notes.
  - Deleting notes.

## Technologies Used

- Flask: A micro web framework for Python.
- JWT (JSON Web Tokens): Used for user authentication and authorization.
- SQLAlchemy: A powerful SQL toolkit and Object-Relational Mapping (ORM) library.
- Bcrypt: A password-hashing library for secure password storage.
- CORS (Cross-Origin Resource Sharing): Enables cross-origin resource sharing in the API.
- SQLite3 or MySQL: Choose the database backend based on user preference (by default SQLite3 is used).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TheDayDreamer01/NoteApp-Flask-API.git
   ```

2. Navigate to the project directory:

   ```bash
   cd NoteApp
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database backend:

   - Open the `App/config.py` file.
   - Choose between SQLite3 or MySQL based on your preference.
   - Update the necessary configuration details (e.g., database credentials).

5. Run the application:

   ```bash
   python main.py
   ```

   The API should now be accessible at `http://localhost:5000`.

## API Usage

To interact with the NoteApp API, you can use various HTTP methods (GET, POST, PUT, DELETE) and the provided endpoints. Here are some example endpoints:

- User Authentication:
  - `POST /api/auth/signin/`: Sign in with email and password.
  - `POST /api/auth/signup/`: Sign up with username, email and password.
  - `GET /api/auth/signout/`: Sign out the current user.

- User Manipulation:
  - `GET /api/user/{user_id}/`: Retrieve user information.
  - `PUT /api/user/{user_id}/`: Update user profile.
  - `PUT /api/user/{user_id}/`: Update user password.
  - `DELETE /api/user/{user_id}/`: Delete user account.

- Note Operations:
  - `GET /api/note/`: Retrieve all notes.
  - `POST /api/note/`: Create a new note.
  - `GET /api/note/{note_id}/{title}/`: Retrieve a specific note.
  - `PUT /api/note/{note_id}/{title}/`: Update a specific note.
  - `DELETE /api/note/{note_id}/{title}/`: Delete a specific note.

Please refer to the API documentation or explore the codebase for more detailed information on the available endpoints and their usage.

## Contribution

Contributions to the NoteApp API are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.
