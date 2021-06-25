from flask import Flask, request, render_template
from Config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app import routes
