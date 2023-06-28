Certainly! Here's a comprehensive tutorial on Flask-JWT-Extended in GitHub-flavored Markdown format:

---

# Flask-JWT-Extended Tutorial

## Introduction

This tutorial will guide you through the basics of using Flask-JWT-Extended, an extension for Flask that adds support for JSON Web Tokens (JWT) to secure your API endpoints. We will cover the following topics:

1. Setup and Installation
2. Configuring Flask-JWT-Extended
3. User Authentication and Token Generation
4. Protecting Endpoints with JWT
5. Customizing JWT Handling
6. Refreshing Tokens
7. Revoking Tokens
8. Token Blacklisting
9. Handling JWT Errors
10. Advanced Topics

## 1. Setup and Installation

In this section, we will cover the setup and installation process for Flask-JWT-Extended.

### Prerequisites

- Python 3.x installed on your system
- pip package manager

### Installation

1. Create a new directory for your Flask project: `mkdir flask-app`
2. Navigate to the project directory: `cd flask-app`
3. Create and activate a virtual environment (recommended):

```shell
python3 -m venv env
source env/bin/activate
```

4. Install Flask-JWT-Extended and its dependencies:

```shell
pip install Flask-JWT-Extended
```

## 2. Configuring Flask-JWT-Extended

In this section, we will configure Flask-JWT-Extended for our application.

### Configuration Options

Flask-JWT-Extended provides several configuration options that can be set in your Flask application. These options include:

- JWT_SECRET_KEY: Secret key used to encode and decode JWTs
- JWT_ACCESS_TOKEN_EXPIRES: Expiration time for access tokens
- JWT_REFRESH_TOKEN_EXPIRES: Expiration time for refresh tokens
- JWT_BLACKLIST_ENABLED: Enable token blacklisting
- JWT_BLACKLIST_TOKEN_CHECKS: Specify which token types to check for revocation

To configure Flask-JWT-Extended, update your Flask application's configuration:

```python
from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app)
```

## 3. User Authentication and Token Generation

In this section, we will cover user authentication and token generation using Flask-JWT-Extended.

### User Login

To authenticate a user and generate a JWT access token, create a login endpoint:

```python
from flask import jsonify, request
from flask_jwt_extended import create_access_token

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if the username and password are valid
    if username == 'admin' and password == 'password':
        # Generate an access token for the user
        access_token = create_access_token(identity=username)

        # Return the access token as a JSON response
        return jsonify({'access_token': access_token}), 200

    # Return an error message if the authentication fails
    return jsonify({'message': 'Invalid username or password'}), 401
```

### Protected Route

To protect a route and require a valid JWT access token for access, use the `@jwt_required` decorator:

```python
from flask_jwt_extended import jwt_required

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Only authenticated users with valid tokens can access this route
    return jsonify({'message': 'Protected Route'})
```

## 4. Protect

ing Endpoints with JWT

In this section, we will explore different ways to protect endpoints using Flask-JWT-Extended.

### Method 1: Decorator

You can protect an endpoint using the `@jwt_required` decorator:

```python
from flask_jwt_extended import jwt_required

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Only authenticated users with valid tokens can access this route
    return jsonify({'message': 'Protected Route'})
```

### Method 2: Decorator with Custom Options

You can also customize the behavior of the `@jwt_required` decorator:

```python
from flask_jwt_extended import jwt_required

@app.route('/protected', methods=['GET'])
@jwt_required(optional=True, fresh=True)
def protected():
    # Only authenticated users with fresh tokens can access this route
    # However, the route is still accessible with expired tokens (optional=True)
    return jsonify({'message': 'Protected Route'})
```

### Method 3: Manual Token Check

You can manually check the JWT token using `jwt_required()` function:

```python
from flask_jwt_extended import jwt_required

@app.route('/protected', methods=['GET'])
def protected():
    # Manually check the JWT token
    jwt_required()

    # Only authenticated users with valid tokens can access this route
    return jsonify({'message': 'Protected Route'})
```

## 5. Customizing JWT Handling

In this section, we will cover customizing JWT handling in Flask-JWT-Extended.

### Custom Claims

You can include custom claims in your JWT tokens:

```python
from flask_jwt_extended import create_access_token

access_token = create_access_token(identity=username, custom_claim='value')
```

### Custom Response

You can customize the response returned when a JWT error occurs:

```python
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({'message': 'Token has expired'}), 401
```

## 6. Refreshing Tokens

In this section, we will cover refreshing JWT access tokens using Flask-JWT-Extended.

### Refresh Endpoint

Create a refresh endpoint to generate a new access token using a valid refresh token:

```python
from flask_jwt_extended import create_access_token, jwt_refresh_token_required

@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    # Generate a new access token using the refresh token
    access_token = create_access_token(identity=get_jwt_identity())

    # Return the new access token as a JSON response
    return jsonify({'access_token': access_token}), 200
```

### Obtaining a Refresh Token

To obtain a refresh token, include the `set_refresh_cookies` parameter when creating an access token:

```python
from flask_jwt_extended import create_access_token

access_token = create_access_token(identity=username, set_refresh_cookies=True)
```

## 7. Revoking Tokens

In this section, we will cover revoking JWT tokens using Flask-JWT-Extended.

### Revoking Access Tokens

To revoke an access token, add it to the token blacklist:

```python
from flask_jwt_extended import get_jwt, get_raw_jwt

blacklist.add(get_raw_jwt()['jti'])
```

### Revoking Refresh Tokens

To revoke a refresh token, add it to the token blacklist:

```python
from flask_jwt_extended import get_raw_jwt

blacklist.add(get_raw_jwt()['jti'])
```

## 8. Token Blacklisting

In this section, we will cover token blacklisting using Flask-JWT-Extended.

### Setting Up Token Blacklist

To enable token blacklisting, configure Flask-JWT-Extended with the `JWT_BLACKLIST_ENABLED` option

:

```python
app.config['JWT_BLACKLIST_ENABLED'] = True
```

### Blacklisting Tokens

To blacklist a token, add its unique identifier (`jti`) to the token blacklist:

```python
from flask_jwt_extended import get_raw_jwt

blacklist.add(get_raw_jwt()['jti'])
```

### Checking Token Blacklist

To check if a token is blacklisted, use the `is_token_revoked` callback:

```python
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

@jwt.token_in_blacklist_loader
def check_token_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return blacklist.is_token_revoked(jti)
```

## 9. Handling JWT Errors

In this section, we will cover handling JWT errors using Flask-JWT-Extended.

### Handling JWT Exceptions

To handle JWT exceptions globally, use the `@jwt.error_handler` decorator:

```python
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

@jwt.error_handler
def handle_jwt_errors(error):
    return jsonify({'message': str(error)}), 401
```

### Handling Invalid Tokens

To handle invalid tokens, use the `@jwt.invalid_token_loader` decorator:

```python
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

@jwt.invalid_token_loader
def handle_invalid_token(error):
    return jsonify({'message': 'Invalid token'}), 401
```

## 10. Advanced Topics

In this section, we will briefly touch upon advanced topics related to Flask-JWT-Extended.

- Token Identity Claims: Customizing the JWT identity claim
- Token Freshness: Checking token freshness for sensitive operations
- Token Location: Configuring token location in requests

