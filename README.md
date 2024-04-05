# Flask Grammar Correction App

This Flask application provides a simple but powerful grammar correction service, integrating an external AI-powered grammar correction API. It supports user management functionalities including signup, login, and user profile updates, leveraging JWT for secure authentication.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask
- Flask-JWT-Extended
- SQLAlchemy (if interacting with a database)
- Any additional packages can be installed via `requirements.txt`.

### Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/flask-grammar-correction-service.git
cd flask-grammar-correction-service
```

2. Install the required Python packages.

```bash
pip install -r requirements.txt
```

3. Configure your application settings by editing the `config/db_config.py` and `config/ai_config.py` files to match your database and AI service credentials.

4. Set up your database schema as required by the `models/user.py` (assuming you have a `UserDBHandler` managing database interactions).

5. Start the Flask application.

```bash
export FLASK_APP=run.py
export FLASK_ENV=development # Use 'production' for production environments
flask run
```

### API Documentation

For API documentation and interaction, it's recommended to use tools like Swagger or Postman. Import the API collection and environment settings provided in the repository to get started.

- **Login**: `POST /login` - Authenticate users and receive a JWT token.
- **Signup**: `POST /signup` - Register a new user.
- **Delete User**: `DELETE /deleteUser` - Remove an existing user account. Requires JWT authentication.
- **Update User**: `PATCH /updateUser` - Update user information. Requires JWT authentication.
- **Grammar Check**: `POST /grammar` - Submit text for grammar correction. Requires JWT authentication.

### AI Integration

This service utilizes an external AI-powered grammar correction API. Configure the `API_URL` and `API_TOKEN` in `config/ai_config.py` to integrate with the grammar correction service. The `/grammar` endpoint facilitates interaction with this AI service, offering real-time grammar suggestions.

## Contribution

Contributions to the Flask Grammar Correction Service are welcome. Please ensure to follow the code of conduct and submit pull requests for any enhancements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
