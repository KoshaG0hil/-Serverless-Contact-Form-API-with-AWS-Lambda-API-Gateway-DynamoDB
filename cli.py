#!/usr/bin/env python3
"""
Serverless Contact Form API - Interactive CLI Demonstration
Simulates submitting and retrieving messages via Lambda & DynamoDB logic.
"""

import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# In-memory storage simulating DynamoDB
MOCK_DYNAMODB = []


def simulate_submit(name: str, email: str, message: str):
    """Simulates lambda_submit.py handler execution."""
    if not name or not email or not message:
        return {"statusCode": 400, "body": json.dumps({"error": "Missing required fields"})}

    item = {"name": name, "email": email, "message": message}
    MOCK_DYNAMODB.append(item)
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Hi {name}, your message has been saved!"})
    }


def simulate_get():
    """Simulates lambda_get.py handler execution."""
    return {
        "statusCode": 200,
        "body": json.dumps({"messages": MOCK_DYNAMODB})
    }


def run_cli():
    console.print(Panel.fit(
        "[bold cyan]AWS SERVERLESS CONTACT FORM API SIMULATOR[/bold cyan]\n"
        "[dim]AWS Lambda · Amazon API Gateway · Amazon DynamoDB (NoSQL)[/dim]",
        border_style="cyan"
    ))

    # Test Submissions
    test_entries = [
        ("Kosha Gohil", "kosha@example.com", "Testing serverless contact form backend pipeline!"),
        ("DevOps Recruiter", "recruiter@cloudcorp.com", "Impressive AWS cloud engineering architecture."),
        ("Security Lead", "secops@enterprise.org", "Great zero-trust DynamoDB encryption configurations.")
    ]

    console.print("\n[bold green]=== SIMULATING POST /submit REQUESTS ===[/bold green]")
    for name, email, msg in test_entries:
        res = simulate_submit(name, email, msg)
        console.print(f"[+] POST /submit: [white]{name} ({email})[/white] -> [bold green]Status {res['statusCode']} OK[/bold green]")

    # Retrieve Messages
    console.print("\n[bold yellow]=== SIMULATING GET /messages (DYNAMODB SCAN) ===[/bold yellow]")
    get_res = simulate_get()
    records = json.loads(get_res["body"])["messages"]

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Sender Name", width=20)
    table.add_column("Email (Partition Key)", width=28)
    table.add_column("Message Payload", width=42)

    for r in records:
        table.add_row(r["name"], r["email"], r["message"])

    console.print(table)
    console.print("\n[bold green][OK] Serverless API execution completed cleanly with 0 errors.[/bold green]\n")


if __name__ == "__main__":
    run_cli()
