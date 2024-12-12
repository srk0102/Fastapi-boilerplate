Here's a README template for your project setup and structure, tailored to the details you've shared:

---

# craft-be

## Overview
`craft-be` is a backend project built with FastAPI designed to provide a centralized video editing platform with a marketplace for AI-powered video editing tools. This project includes features like user role management, organization support, integration with Adobe Premiere Pro, and more.

## Project Structure
Here's an outline of the main directories and their purposes:

```
craft-be/
├── app/
│   ├── __init__.py             # Initialization of the app module
│   └── server.py               # Server initialization functions
├── src/
│   ├── config/
│   │   └── global.py           # Contains global variables and configurations
│   ├── controllers/
│   │   └── __init__.py         # Initialization of the controllers module
│   │   └── test.py             # Example controller functions
│   ├── models/                 # Database models and schemas
│   ├── routes/
│   │   └── __init__.py         # Initialization of routes module
│   │   └── test.py             # Example API route
│   ├── services/               # Business logic and service functions
│   └── main.py                 # Main entry point to start the FastAPI server
├── tests/
│   └── __init__.py             # Test package initialization
├── .env                        # Environment variables file
├── poetry.lock                 # Lock file for dependencies
├── pyproject.toml              # Poetry configuration for project dependencies
├── Dockerfile                  # Docker configuration
├── README.md                   # Project documentation
└── requirements.txt            # Package requirements
```

### Key Folders and Files
- **`app/`**: Contains initialization files and server configurations.
- **`src/`**: The core backend logic:
  - `config/`: Holds global configurations like HTTP statuses and constants.
  - `controllers/`: Houses controllers that manage the main logic for routes.
  - `models/`: Holds database models and data schemas.
  - `routes/`: Defines the API endpoints.
  - `services/`: Contains service logic and business rules.
  - `main.py`: The primary entry point for starting the FastAPI server.
- **`tests/`**: Testing suite for unit and integration tests.
- **`.env`**: File to store environment variables.
- **`Dockerfile`**: Configuration file for Docker to containerize the application.

## Setup Instructions

### Prerequisites
- **Python 3.11**
- **Poetry** for dependency management
- **Docker** (optional, for containerization)
- **RabbitMQ** and **PostgreSQL** if using them locally

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/craft-be.git
   cd craft-be
   ```

2. **Install dependencies:**
   Use Poetry to install all project dependencies.
   ```bash
   poetry install
   ```

3. **Set up environment variables:**
   Copy the `.env.example` file to `.env` and update the values according to your setup.
   ```bash
   cp .env.example .env
   ```

4. **Run RabbitMQ and PostgreSQL**:
   Make sure RabbitMQ and PostgreSQL are running (you can use Docker for local development).

5. **Run the server:**
   ```bash
   poetry run uvicorn main:app --reload
   ```
   The application should now be running on `http://127.0.0.1:8000`.

### Running with Docker

1. **Build the Docker image:**
   ```bash
   docker build -t craft-be .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 8000:8000 --env-file .env craft-be
   ```

The application will be available at `http://localhost:8000`.

### Usage

- **API Documentation**: Access the FastAPI interactive documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
- **Test Endpoints**: Use the `/test` route to confirm that endpoints are working.

### Running Tests

To run tests, you can use `pytest`:
```bash
poetry run pytest tests/
```

## Troubleshooting

If you encounter issues, check:
- **Poetry setup**: Make sure Poetry is correctly set up and virtual environment is activated.
- **Dependencies**: Ensure all dependencies are correctly installed.
- **Environment variables**: Verify that `.env` file values are correct.

## Additional Information
- **Middleware**: Includes middleware to capture client request details like IP and user-agent.
- **Client IP Handling**: Note that if running behind a proxy, configure headers correctly for capturing real client IP.

---

This README template provides the setup, project structure, and basic usage information for the `craft-be` backend project. Adjust the content as per specific project details or updates.