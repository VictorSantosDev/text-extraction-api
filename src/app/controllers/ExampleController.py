from flask import request, jsonify
from app.services.ExampleService import ExampleService

class ExampleController:

    def __init__(self):
        self.exampleService = ExampleService

    # Crie um controlador onde define a chamada para service e retorno da resposta.
    def example_method(self):
        example = self.exampleService.example_method_service()

        return jsonify(
            {
                "data": {
                    "name": example.name,
                    "text_file": example.text
                }
            }
        )
