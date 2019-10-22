# Installation

1. Install NPM dependencies (Bootstrap, jQuery):

```bash
npm install
```

2. Create Python virtualenv and activate it, install Python requirements:

```bash
virtualenv .env
. .env/bin/activate
pip install -r requirements.txt
```

# Running

Within activated virtualenv run Flask application in development mode:

```
export FLASK_ENV=development
flask run
```
