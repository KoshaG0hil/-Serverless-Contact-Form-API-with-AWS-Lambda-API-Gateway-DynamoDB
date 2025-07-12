
# 🛠️ Serverless Contact Form Project using AWS Lambda, API Gateway, DynamoDB & EC2 (Flask)

This project is a beginner-to-intermediate friendly walkthrough of how to build and deploy a **fully serverless contact form backend** using AWS. It's designed to teach you how to build RESTful APIs, integrate services like **Lambda**, **API Gateway**, **DynamoDB**, and deploy a **Flask frontend on EC2**, all step-by-step.

---

## 📚 What You Will Learn

- How to build a serverless API using AWS Lambda & API Gateway
- How to parse JSON requests and store data in DynamoDB
- How to host a frontend on EC2 with Flask and connect it to your API
- How to test your backend using Postman
- How to use ALB (Application Load Balancer) to distribute traffic
- IAM permissions and CORS configuration for Lambda/APIs
- Real-world best practices for error handling and security

---

## 📐 Architecture Overview

```
User → [API Gateway] → [Lambda Function] → [DynamoDB Table]
    → [EC2 + Flask App] ← [Application Load Balancer]
```

---

## 🧰 Tech Stack

- **AWS Lambda** – runs the backend code (no servers to manage)
- **API Gateway** – exposes RESTful API endpoints
- **Amazon DynamoDB** – stores form submissions (NoSQL)
- **EC2 + Flask** – frontend form hosted on virtual machines
- **ALB (Load Balancer)** – distributes traffic across EC2s
- **IAM** – for permissions and access control
- **Postman** – for API testing

---

## ✨ Project Features

- Submit contact forms via `/submit` POST route
- Store form data in DynamoDB
- Retrieve submissions via `/messages` GET route
- Test everything using Postman
- Optional: Use Flask-based frontend on EC2 instances and route traffic through an ALB

---

## 🔧 Setup Instructions (Step-by-Step)

### Step 1: DynamoDB
- Go to AWS Console → DynamoDB → Create Table
- Table Name: `ContactSubmissions`
- Partition Key: `email` (String)

---

### Step 2: Lambda Function – Submit Handler
- Create a Lambda function in Python 3.9 or 3.10
- Add this code:
```python
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactSubmissions')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        name = body.get('name')
        email = body.get('email')
        message = body.get('message')

        if not name or not email or not message:
            return {'statusCode': 400, 'body': json.dumps({'error': 'Missing required fields'})}

        table.put_item(Item={'email': email, 'name': name, 'message': message})

        return {'statusCode': 200, 'body': json.dumps({'message': f'Hi {name}, your message has been saved!'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
```

- Attach IAM Role with `AmazonDynamoDBFullAccess` permissions

---

### Step 3: API Gateway
- Create a new REST API
- Create a POST method for `/submit` resource
- Integrate with the Lambda function
- Enable CORS
- Deploy to a new stage (e.g., `prod`)

---

### Step 4: Optional - Lambda for GET `/messages`
- Similar setup, but use `Scan()` on DynamoDB to retrieve all items

---

### Step 5: Flask Frontend on EC2 (Optional)
- Launch 2 EC2 instances (Amazon Linux 2)
- SSH into both, run:
```bash
sudo yum update -y
sudo yum install python3 -y
pip3 install flask
```

- Create a `app.py`:
```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Kosha's Flask App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

- Run it with: `sudo python3 app.py`

- Configure Security Groups to allow port 80

---

### Step 6: Load Balancer (ALB)
- Go to EC2 → Load Balancers → Create Application Load Balancer
- Register both EC2s as targets
- Set health check path (e.g., `/`)
- Attach listener rule to forward traffic to targets

---

### Step 7: Testing with Postman

📤 **POST** to `/submit` endpoint:
```json
{
  "name": "Kosha",
  "email": "kosha@example.com",
  "message": "Testing serverless project!"
}
```

📥 **GET** from `/messages` endpoint:
- Returns all saved entries

---

## ✅ HTTP Status Codes Used

| Code | Description |
|------|-------------|
| 200  | OK – successful operation |
| 201  | Created – (optional for POST) |
| 400  | Bad Request – missing or malformed input |
| 500  | Server Error – unexpected issues |

---

## 📂 Files Included

- `lambda_submit.py`
- `lambda_get.py`
- `postman_collection_serverless_form.json`
- `README.md`

---

## 📈 Impact & Benefits

- Demonstrates integration of serverless backend with managed NoSQL database for scalable form processing  
- Shows hands-on experience with AWS API Gateway, Lambda, and secure IAM roles  
- Includes deploying a Python Flask app on EC2 behind an Application Load Balancer for high availability  
- Enables building real-world REST APIs with best practices in security, error handling, and scalability  


## 🙋‍♀️ Author

**Kosha Gohil**  
AWS Certified Solutions Architect – Associate  

---
