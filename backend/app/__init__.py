import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Загрузка переменных окружения
load_dotenv(override=False)

# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(os.environ.get("BACKEND_CONFIG"))
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# инициализирует расширений
from . import views
