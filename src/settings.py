import os

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", 'commutations')

SERVICE_NAME = os.getenv("SERVICE_NAME", "Commutation Service"),
SERVER_URL = os.getenv("APM_SERVER_URL", "http://arm-elk-01:8200"),
SECRET_TOKEN = os.getenv("SECRET_TOKEN", 'my_secret_token'),
ENVIRONMENT = os.getenv("SERVICE_ENVIRONMENT", 'local')
