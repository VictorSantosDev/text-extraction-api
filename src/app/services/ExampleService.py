from app.models.Example import Example

class ExampleService:

    # Adicione a regra de negócios em uma "Service"
    def example_method_service() -> Example:
        
        example = Example(
            name="Example",
            text="RETORNE O TEXTO IGUAL NESSE EXEMPLO"
        )

        return example