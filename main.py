import grpc
from google.protobuf import empty_pb2
from proto import user_pb2, user_pb2_grpc

class UserServiceClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = user_pb2_grpc.UserServiceStub(self.channel)
    
    def create_user(self, name, email):
        request = user_pb2.CreateUserRequest(name=name, email=email)
        return self.stub.CreateUser(request)
    
    def get_user(self, user_id):
        request = user_pb2.GetUserRequest(id=user_id)
        return self.stub.GetUser(request)
    
    def list_users(self):
        return self.stub.ListUsers(empty_pb2.Empty())

def display_menu():
    print("\n" + "="*50)
    print("🏪 TechShop - Gerenciamento de Usuários")
    print("="*50)
    print("1. 👤 Criar novo usuário")
    print("2. 🔍 Buscar usuário por ID")
    print("3. 📜 Listar todos os usuários")
    print("4. 🚪 Sair")
    print("="*50)
    return input("Escolha uma opção: ")

def main():
    client = UserServiceClient()
    
    while True:
        try:
            choice = display_menu()
            
            if choice == '1':
                print("\n" + "-"*30 + " Novo Usuário " + "-"*30)
                name = input("Nome: ").strip()
                email = input("Email: ").strip()
                new_user = client.create_user(name, email)
                print(f"\n✅ Usuário criado com sucesso!")
                print(f"   ID: {new_user.id} | Nome: {new_user.name} | Email: {new_user.email}")
                
            elif choice == '2':
                print("\n" + "-"*28 + " Buscar Usuário " + "-"*28)
                try:
                    user_id = int(input("ID do usuário: "))
                    user = client.get_user(user_id)
                    if user.id:
                        print(f"\n🆔 ID: {user.id}")
                        print(f"👤 Nome: {user.name}")
                        print(f"📧 Email: {user.email}")
                    else:
                        print("\n⚠️ Usuário não encontrado!")
                except ValueError:
                    print("\n❌ ID deve ser um número inteiro!")
                    
            elif choice == '3':
                print("\n" + "-"*28 + " Todos os Usuários " + "-"*26)
                users = client.list_users()
                if len(users.users) == 0:
                    print("\nℹ️ Nenhum usuário cadastrado!")
                else:
                    for user in users.users:
                        print(f"\n⭐ ID: {user.id}")
                        print(f"   Nome: {user.name}")
                        print(f"   Email: {user.email}")
                        print("-"*50)
                
            elif choice == '4':
                print("\n👋 Até logo!")
                break
                
            else:
                print("\n❌ Opção inválida! Tente novamente.")
                
        except grpc.RpcError as e:
            print(f"\n🚨 Erro de comunicação: {e.code().name}")
            print(f"   Detalhes: {e.details()}")
        except Exception as e:
            print(f"\n⚠️ Erro inesperado: {str(e)}")

if __name__ == '__main__':
    main()
