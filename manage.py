import os
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.config import configure_app
from app import app, db
from app.models.models import Items, Catalog, User
import logging

logging.basicConfig()


l = [1, 2, 3]

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()
