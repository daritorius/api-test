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

Http methods & urls & params:

    ASSETS:
        - [GET] /assets/
            params: sort_by -> string: choices ('asc', 'desc') -> not required
            params: limit -> positive integer -> not required
            params: credits_filter -> string -> not required
        - [POST] /assets/
            params: title -> string -> required
            params: description -> string -> not required
            params: created_at -> datetime string -> format 'rfc822' ('Mon, 01 Jun 2015 00:00:00') -> not required
            params: credits_names -> list of names (strings) -> ['John Doe', 'Adam Smith'] -> not required
            params: thumbnails -> list of image urls -> ['http://google.com/image.png', 'http://yahoo.com/image.png'] -> not required

        - [GET] /assets/<asset_id>/
        - [DELETE] /assets/<asset_id>/
        - [PUT] /assets/<asset_id>/
            params: title -> string -> required
            params: description -> string -> not required
            params: created_at -> datetime string -> format 'rfc822' ('Mon, 01 Jun 2015 00:00:00') -> not required

        - [GET] /assets/<asset_id>/credits/

    CREDITS:

        - [GET] /credits/
            params: sort_by -> string: choices ('asc', 'desc') -> not required
            params: limit -> positive integer -> not required
        - [POST] /credits/
            params: name -> string -> required

        - [GET] /credits/<credits_id>/
        - [DELETE] /credits/<credits_id>/
        - [PUT] /credits/<credits_id>/
            params: name -> string -> required

        - [GET] /credits/<credits_id>/assets/

Thank you.