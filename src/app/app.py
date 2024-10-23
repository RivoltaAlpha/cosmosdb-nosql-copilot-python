from flask import Flask
from azure.cosmos import CosmosClient
from routes import app as routes_blueprint
from config import Config


app = Flask(__name__)

# Register the blueprint from routes.py
app.register_blueprint(routes_blueprint)

# Initialize Cosmos DB Client
client = CosmosClient(Config.COSMOS_ENDPOINT, credential=Config.COSMOS_KEY)
database = client.get_database_client(Config.COSMOS_DATABASE)

if __name__ == '__main__':
    app.run(debug=True)