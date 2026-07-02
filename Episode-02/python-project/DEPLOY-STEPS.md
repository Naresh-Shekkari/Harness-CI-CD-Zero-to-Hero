# 🚀 Deploy Python App with Local Docker Runner

## What We Built

```
python-project/
├── app.py              ← Flask web app
├── test_app.py         ← Unit tests
├── requirements.txt    ← Dependencies
├── Dockerfile          ← Docker image
├── .gitignore
└── .harness/
    └── pipeline-docker.yaml  ← Harness pipeline (Local Docker)
```

---

## Prerequisites

1. Docker Desktop installed and running
2. Harness Delegate installed (see below)
3. Code pushed to GitHub

---

## Step 1: Install Harness Docker Delegate

1. Go to Harness → Project Settings → Delegates
2. Click + New Delegate
3. Choose Docker
4. Copy the docker-compose command Harness gives you
5. Run it in your terminal
6. Wait 2 minutes
7. Delegate shows "Connected" in Harness UI

---

## Step 2: Push Code to GitHub

```bash
git add .
git commit -m "Episode 2: Python project with Docker pipeline"
git push origin master
```

---

## Step 3: Create Pipeline in Harness

1. Pipelines → Import from Git
2. Connector: your GitHub connector
3. Repo: Harness-CI-CD-Zero-to-Hero
4. Branch: master
5. YAML Path: Episode-02/python-project/.harness/pipeline-docker.yaml
6. Click Import

---

## Step 4: Run Pipeline

1. Click Run
2. Branch: master
3. Click Run Pipeline
4. Watch 3 steps execute:
   - Install Dependencies ✅
   - Run Tests ✅
   - Run App ✅

---

## Expected Output

```
=== Running Unit Tests ===
test_app.py::test_home PASSED
test_app.py::test_health PASSED
test_app.py::test_info PASSED
=== All Tests Passed! ===

=== Starting Python App ===
{'message': 'Hello from Harness CI/CD Course!', 'episode': 2, ...}
{'status': 'healthy'}
=== App Works! Pipeline Success! ===
```

---

## Run Locally (to test before pushing)

```bash
cd Episode-02/python-project
pip install -r requirements.txt
pytest test_app.py -v
python app.py
# Open browser: http://localhost:5000
```
