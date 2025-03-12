# Cliente gRPC
Esse é um cliente gRPC simples que se comunica com o servidor disponível no repositório https://github.com/pepeu120/UserServiceRpc.
O cliente foi desenvolvido para fins de aprendizado na disciplina de Sistemas Distribuídos.

## Como usar
Para usar este cliente, siga estes passos:

Entre no ambiente virtual (opcional):
``` bash
source env/bin/activate
```

Instale as dependências necessárias (caso não tenha instalado anteriormente ou esteja fora do ambiente virtual):
``` bash
pip install grpcio grpcio-tools googleapis-common-protos
```

Gere os arquivos Python a partir do .proto atualizado:
``` bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/user.proto
```

Execute o cliente (certifique-se de que o servidor está em execução):
``` bash
python main.py
```
