# Python CI/CD Pipeline with GitHub Actions

This project demonstrates how to implement a Continuous Integration (CI) and Continuous Deployment (CD) pipeline using GitHub Actions for a simple Python application.

---

## Project Structure

```text
project/
│
├── src/
│   ├── __init__.py
│   └── math_operations.py
│
├── tests/
│   └── test_operation.py
│
├── requirements.txt
│
└── .github/
    └── workflows/
        ├── ci.yml
        └── cd.yml
```

---

## Application Code

### src/math_operations.py

```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```

---

## Unit Tests

### tests/test_operation.py

```python
from src.math_operations import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(4, 3) == 1
    assert sub(3, 3) == 0
    assert sub(2, 3) == -1
```

---

## Dependencies

### requirements.txt

```text
pytest
```

Install dependencies locally:

```bash
pip install -r requirements.txt
```

---

# Continuous Integration (CI)

The CI pipeline automatically validates code changes whenever code is pushed or a Pull Request is created.

### CI Workflow Objectives

- Checkout source code
- Set up Python environment
- Install dependencies
- Execute unit tests
- Validate application quality before merge

### Trigger Conditions

```yaml
on:
  push:
    branches:
      - "**"

  pull_request:
    branches:
      - main
      - master
```

### CI Process Flow

```text
Developer Pushes Code
         │
         ▼
GitHub Actions Triggered
         │
         ▼
Checkout Repository
         │
         ▼
Setup Python Environment
         │
         ▼
Install Dependencies
         │
         ▼
Run Pytest Test Cases
         │
         ▼
Tests Passed?
    ┌────┴────┐
    │         │
   No        Yes
    │         │
    ▼         ▼
Pipeline    Success
Failed
```

---

# Continuous Deployment (CD)

The CD pipeline executes after successful code integration into the main branch.

### CD Workflow Objectives

- Re-run tests
- Build deployment package
- Upload deployment artifacts
- Deploy application
- Perform health checks

### Trigger Conditions

```yaml
on:
  push:
    branches:
      - main
```

### CD Process Flow

```text
Merge Pull Request
         │
         ▼
Push to Main Branch
         │
         ▼
CD Workflow Triggered
         │
         ▼
Run Tests
         │
         ▼
Package Application
         │
         ▼
Upload Artifact
         │
         ▼
Deploy Application
         │
         ▼
Health Check
         │
         ▼
Deployment Successful
```

---

# Setting Up GitHub Actions

## Step 1: Create Workflow Directory

Create the following folder structure:

```text
.github/
└── workflows/
```

---

## Step 2: Add CI Workflow

Create:

```text
.github/workflows/ci.yml
```

This workflow:

- Runs on every push
- Runs on every pull request
- Executes automated tests

---

## Step 3: Add CD Workflow

Create:

```text
.github/workflows/cd.yml
```

This workflow:

- Runs after code reaches the main branch
- Packages application files
- Performs deployment steps

---

## Step 4: Push Repository to GitHub

Initialize Git repository:

```bash
git init
git add .
git commit -m "Initial commit"
```

Add GitHub remote repository:

```bash
git remote add origin <repository-url>
git branch -M main
git push -u origin main
```

---

## Step 5: Verify Workflow Execution

Navigate to:

```text
GitHub Repository
→ Actions Tab
```

Expected CI execution:

```text
✓ Checkout Repository
✓ Setup Python
✓ Install Dependencies
✓ Run Unit Tests
✓ Pipeline Success
```

---

## Testing CI Failure

Modify application code intentionally:

```python
def add(a, b):
    return a - b
```

Commit and push changes:

```bash
git add .
git commit -m "Testing CI failure"
git push
```

Expected result:

```text
 Unit Test Failure
 CI Pipeline Failed
```

This confirms that automated testing is working correctly.

---

# Branch Protection (Recommended)

Protect the main branch by enforcing successful CI execution before merge.

Navigate to:

```text
Repository Settings
→ Branches
→ Add Rule
```

Configure:

- Require Pull Request before merge
- Require status checks to pass
- Select CI workflow

Benefits:

- Prevents broken code from reaching production
- Enforces automated validation

---

# GitHub Secrets for Deployment

For real deployments, store credentials securely.

Navigate to:

```text
Repository Settings
→ Secrets and Variables
→ Actions
```

Example secrets:

| Secret Name | Purpose |
|------------|---------|
| SERVER_HOST | Deployment server address |
| SERVER_USER | Server username |
| SERVER_SSH_KEY | SSH private key |
| API_TOKEN | Authentication token |

Usage example:

```yaml
${{ secrets.SERVER_HOST }}
```

---

# Example Deployment Workflow

Example deployment to a Linux server:

```yaml
- name: Deploy via SSH
  uses: appleboy/ssh-action@v1

  with:
    host: ${{ secrets.SERVER_HOST }}
    username: ${{ secrets.SERVER_USER }}
    key: ${{ secrets.SERVER_SSH_KEY }}

    script: |
      cd /app
      git pull
      systemctl restart myapp
```

---

# Expected Outcome

After implementation:

### On Every Push

```text
Push Code
   │
   ▼
CI Pipeline Runs
   │
   ▼
Tests Executed
   │
   ▼
Pass / Fail Result
```

### On Merge to Main

```text
Merge Pull Request
   │
   ▼
CD Pipeline Runs
   │
   ▼
Build Package
   │
   ▼
Deploy Application
   │
   ▼
Production Ready
```

---

# Future Enhancements

- Code coverage reporting
- Static code analysis
- Security scanning
- Docker image creation
- Kubernetes deployment
- AWS/Azure/GCP deployment
- Slack or Email notifications
- Automated versioning and releases

---

# Summary

This project demonstrates:

- Python application development
- Unit testing using pytest
- Continuous Integration with GitHub Actions
- Continuous Deployment with GitHub Actions
- Automated validation before merge
- Deployment-ready workflow structure

The CI/CD pipeline ensures that every code change is automatically tested, validated, and prepared for deployment, reducing manual effort and improving software quality.