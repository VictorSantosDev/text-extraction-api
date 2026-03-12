from flask import Flask
from app.routes.ExampleRoutes import example_routes

app = Flask(__name__)

# Registrem as rotas aqui, igual no exemplo abaixo.
app.register_blueprint(example_routes)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8081,
        debug=True
    )
