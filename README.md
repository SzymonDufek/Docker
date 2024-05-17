# Project-Docker


This repository contains a project that demonstrates the use of FastAPI and Docker to create a microservices architecture. The project consists of two microservices: a frontend service that handles user interface and form submissions, and a backend service that processes images and interacts with a database

## Functionality
### Frontend Service
The frontend service is responsible for:

- Serving the main HTML page located in the static directory.
- Handling form submissions which include text and image files.
- Sending the submitted data to the backend service for processing.

## Backend Service
### The backend service handles:

- Receiving data from the frontend service.
- Processing images using the model_pipeline function.
- Storing the processed data (question and response) in a SQLite database.
- Logging each request received from the frontend service.
- Providing an endpoint to fetch and view the logs.
- Backend is running on fine-tuned model from huggingface https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

## Installation

To run the project, ensure you have Docker and Docker Compose installed. Then, follow these steps:

- Clone the repository:

```sh
  git clone https://github.com/SzymonDufek/Project-Docker.git
```

- Navigate to the project directory:

```sh
  cd Project-Docker
```

- Build and start the project

```sh
  docker-compose up --build
```

- Access to the frontend service

Open your browser and navigate to `http://localhost:8000`.

- Submit a form

Submit image and ask a question.

