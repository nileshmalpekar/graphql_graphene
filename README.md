# Introduction

## Setup

1. Setup virtual environment

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt 
```

2. Run tests

```
./scripts/app_test.sh 
```

3. Run flask app

    3.1 Directly
```
./scripts/flask_run.sh
```

    3.2 With `gunicorn`
```
./scripts/app_run.sh 
```

4. Access application GUI

Application Web GUI could be accessed at location http://127.0.0.1:5000/graphql