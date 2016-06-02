from src.resources import *
from urls import *

if __name__ == '__main__':
    app.secret_key = '123'
    app.run(debug=True)
