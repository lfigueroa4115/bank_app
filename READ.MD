# Bank Web Application
This is a web application built with Flask for managing bank account. It uses PostgreSQL as the database. Users are able to view, update and delete account. 
## Prerequisites
- Docker
- Docker Compose
## Installation
1. Clone this repository:
    git clone <repository-url>
    Replace <repository-url> with the actual URL of your GitHub repository.

2. Create a `requirements.txt` file:
- Activate your project's virtual environment (if you are using one).
- Open a terminal or command prompt and navigate to the root directory of your project.
- Run the following command to generate the `requirements.txt` file based on the installed packages in your environment:
  pip freeze > requirements.txt

3. Build and run the Docker containers:
    docker-compose up --build


This command will build the Docker image and run the application along with the PostgreSQL database.

4. Access the web application:
- Open a web browser and go to [http://localhost:5000](http://localhost:5000).
- You should be able to interact with the bank web application.

## Usage

- The bank web application provides the following endpoints:
- `GET /account/<int:id>`: Retrieves the account details for the specified account ID.
- `PUT /account/<int:id>`: Updates the balance of the account with the specified account ID.
- `DELETE /users/<int:id>`: Deletes the user account with the specified ID.
- Replace `<int:id>` with the actual account or user ID to interact with the respective endpoints.
- The PostgreSQL database connection details are set in the `connection()` function in the code. Update the connection parameters (`dbname`, `user`, `host`, and `port`) as per your PostgreSQL setup.


