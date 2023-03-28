# Django Product Service

This Django service provides API endpoints for managing products, including a built-in API documentation with Swagger, ReDoc, and OpenAPI schema download capabilities. Below you'll find the details of the available endpoints and their usage, as well as instructions on how to set up and run the project.

## Table of Contents

- [API Documentation Endpoints](#api-documentation-endpoints)
- [Product Endpoints](#product-endpoints)
- [Celery Beat Task](#celery-beat-task)
- [Installation and Configuration](#installation-and-configuration)
- [Running the Project with Docker](#running-the-project-with-docker)
- [Running Tests](#running-tests)

## API Documentation Endpoints

1. **GET /api/schema**: Download the OpenAPI schema.
2. **GET /api/schema/swagger-ui/**: Access the Swagger UI documentation.
3. **GET /api/schema/redoc/**: Access the ReDoc documentation.

## Product Endpoints

1. **GET /api/products**: Retrieve the list of products.
2. **GET /api/products/{code}**: Retrieve a specific product by its code.

For the list of products, the default paginator of Django Rest Framework is used. You can refer to the [official pagination documentation](https://www.django-rest-framework.org/api-guide/pagination/) for more information.

Filters can be applied based on the Django Rest Framework and django-filter documentation for the fields `name`, `buying_price`, and `selling_price` of the product model.

## Celery Beat Task

This service runs a Celery Beat task that updates the selling prices of the products by 10% every 6 minutes.

## Installation and Configuration

1. Create two files in the project root directory: `rabbit.env` and `.env`. Use the provided example `.env` files as a reference for setting the appropriate values.
2. Install the required dependencies (if not using Docker).

## Running the Project with Docker

1. Make sure you have Docker and Docker Compose installed.
2. In the `.env` file, set the `MAP_PORT` and `EXPOSE_PORT` variables to map the ports correctly for Docker Compose.
3. Run the project using the following command:

```bash
docker-compose up
