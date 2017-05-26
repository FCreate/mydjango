from django.apps import AppConfig
from django.db import connection

class MyappConfig(AppConfig):
    name = 'myapp'
    connection.queries

