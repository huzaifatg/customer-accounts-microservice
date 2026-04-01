from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

# Apply security headers
talisman = Talisman(app)