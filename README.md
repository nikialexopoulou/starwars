
# Star Wars API Importer

This Django project imports Star Wars data from the SWAPI API into a local SQLite database.

---

## Features

- Imports planets, species, films, characters, vehicles, and starships
- Uses SQLite as the database backend
- Managed dependencies with Pipenv
- Supports running locally or via Docker
- API documentation available at `/swagger`

---

## Requirements

- Python 3.12+
- Pipenv (if running locally)
- Docker & Docker Compose (if using container)

---

## Setup & Run Locally

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. Install dependencies:

   ```bash
   pipenv install
   ```

3. Apply database migrations:

   ```bash
   pipenv run python manage.py migrate
   ```

4. Start the development server:

   ```bash
   pipenv run python manage.py runserver
   ```

5. Access API documentation at:  
   [http://localhost:8000/swagger](http://localhost:8000/swagger)

6. Run the import command:

   ```bash
   pipenv run python manage.py fetch_swapi_data
   ```

---

## Setup & Run with Docker

1. Build and start the Docker container:

   ```bash
   docker-compose up --build
   ```

2. The server will be available at:  
   [http://localhost:8000](http://localhost:8000)

3. Access the Swagger UI at:  
   [http://localhost:8000/swagger](http://localhost:8000/swagger)

4. Run the import command inside the container:

   ```bash
   docker-compose run web python manage.py fetch_swapi_data
   ```

---

## Sending API Requests

- Use the Swagger UI at `/swagger` for an interactive API interface.
- Or use any REST client (e.g., Postman, curl) to send requests to the endpoints.
- Example with curl:

  ```bash
  curl http://localhost:8000/api/planets/
  ```
