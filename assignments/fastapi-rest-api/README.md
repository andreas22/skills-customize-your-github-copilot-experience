# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build REST API endpoints using FastAPI, including path and query parameters, request validation with Pydantic models, and automatic documentation.

## 📝 Tasks

### 🛠️ Create a Core FastAPI App

#### Description
Set up a FastAPI application with a basic endpoint to retrieve item details by ID.

#### Requirements
Completed program should:

- Create a FastAPI app instance using `FastAPI()`.
- Define a `GET /items/{item_id}` endpoint.
- Return a JSON response with `item_id`, `name`, and `price` fields.
- Use a dictionary or list to store sample item data in the app.

### 🛠️ Add Query Parameters and List Endpoint

#### Description
Add an endpoint that returns a list of items and supports optional filtering through query parameters.

#### Requirements
Completed program should:

- Define a `GET /items` endpoint.
- Accept optional query parameters such as `category` and `max_price`.
- Filter the returned items based on these query parameters.
- Return a JSON list of items matching the criteria.

### 🛠️ Use Pydantic Models and Validate Input

#### Description
Create request and response models using Pydantic to validate API input and output data.

#### Requirements
Completed program should:

- Define a Pydantic model for item creation with fields `name`, `category`, `price`, and `in_stock`.
- Add a `POST /items` endpoint that accepts the request body as the Pydantic model.
- Validate incoming data and return a response model with an assigned `item_id`.
- Ensure FastAPI-generated docs work at `/docs`.

### 🛠️ Example Requests

#### Description
Provide example requests students can use to test their API.

#### Requirements
Completed assignment should include examples such as:

```bash
curl -X GET "http://127.0.0.1:8000/items/1"
```

```bash
curl -X GET "http://127.0.0.1:8000/items?category=books&max_price=20"
```

```bash
curl -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d '{"name":"New Item","category":"books","price":12.99,"in_stock":true}'
```
