# Necessário adicionar os importes das models nesse __init__ para que seja possivel gerar as migrations.
# Sem isso não é possível o Alembic encontrar as models que será migrations para adiconar tabelas no banco.
from app.models.Example import Example
from app.models.Example2 import Example2
