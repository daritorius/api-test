For complete setup of virtualenv:
    ubuntu/debian: sudo apt-get install libsqlite3-dev sqlite3
    macos: brew install sqlite3

Technologies:
    - flask-restful
    - SQLAlchemy
    - fabric
    - sqlite3

Init project with fabric command: "fab init_virtualenv".

Activate virtualenv: "source .env/api/bin/active" from parent directory.

Start project: "python start.py" from parent directory.

Run tests: "python tests.py" from parent directory.

Thank you.