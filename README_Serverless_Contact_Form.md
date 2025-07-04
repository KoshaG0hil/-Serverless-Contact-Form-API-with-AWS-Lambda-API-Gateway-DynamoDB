# 🛠️ Serverless Contact Form with AWS Lambda, API Gateway, and DynamoDB

A complete, serverless contact form backend built with AWS services and tested via Postman. This project demonstrates how to use Amazon API Gateway, AWS Lambda, and Amazon DynamoDB to build a scalable and cost-effective solution.

---

## 📌 Project Overview

**Goal:** Accept contact form data via API, save it to DynamoDB, and allow fetching stored messages via GET endpoint.

---

## 🔧 Technologies Used

- **AWS Lambda** – Serverless compute to handle logic (Python)
- **API Gateway** – RESTful API to expose POST and GET endpoints
- **Amazon DynamoDB** – NoSQL database to store submissions
- **IAM** – Secure roles and permissions for Lambda access
- **Postman** – Testing tool for API requests

---

## 📂 Architecture

```
Postman ➝ API Gateway ➝ Lambda ➝ DynamoDB
                     ↓
               Lambda (GET) ➝ DynamoDB
```

---

## 🔨 Features

- Accepts `POST` request to `/submit` with JSON payload:
  ```json
  {
    "name": "Kosha",
    "email": "kosha@example.com",
    "message": "Testing from Postman!"
  }
  ```

- Stores each message in `ContactSubmissions` DynamoDB table.
- Provides a `GET /messages` endpoint to return all messages.

---

## 🚀 How to Deploy

### Step 1: DynamoDB Table

- Create table: `ContactSubmissions`
- Partition key: `email` (String)

### Step 2: Lambda – `submitContactForm`

- Handles POST requests
- Parses JSON and writes to DynamoDB

### Step 3: Lambda – `getContactMessages`

- Handles GET requests
- Uses `table.scan()` to return all entries

### Step 4: API Gateway

- Create HTTP API
- Route: `POST /submit` ➝ Integration: `submitContactForm`
- Route: `GET /messages` ➝ Integration: `getContactMessages`
- Deploy to a stage (e.g., `prod` or `koshaform`)

### Step 5: IAM Permissions

Both Lambda roles should include:

```json
{
  "Effect": "Allow",
  "Action": ["dynamodb:PutItem", "dynamodb:Scan"],
  "Resource": "arn:aws:dynamodb:<REGION>:<ACCOUNT_ID>:table/ContactSubmissions"
}
```

---

## ✅ Example Usage (Postman)

### POST /submit

- Method: `POST`
- Body → raw → JSON:

```json
{
  "name": "Kosha",
  "email": "kosha@example.com",
  "message": "Hello from Postman!"
}
```

### GET /messages

- Method: `GET`
- No body needed

Returns:

```json
[
  {
    "name": "Kosha",
    "email": "kosha@example.com",
    "message": "Hello from Postman!"
  }
]
```

---

## 👩‍💻 Built by

**Kosha Gohil** – AWS Solutions Architect Associate | Cybersecurity & Cloud Enthusiast  
🗓️ Project Completion: July 2025

---

## 📌 Next Steps

- Add S3-hosted frontend form
- Integrate authentication (Cognito or API Keys)
- Add CORS headers for web integration
- Implement logging via CloudWatch

