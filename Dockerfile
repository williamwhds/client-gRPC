# Usar uma imagem oficial do Node.js com versão LTS
FROM node:18

# Instalar git e dependências necessárias para compilar módulos nativos
RUN apt-get update && apt-get install -y git python3 make g++

# Clonar o repositório Git (substitua pela URL do seu repositório)
RUN git clone https://github.com/pepeu120/UserServiceRpc /app

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências primeiro para aproveitar o cache do Docker
COPY package*.json ./

# Instalar dependências
RUN npm install

# Copiar o restante dos arquivos do projeto
COPY . .

# Expor a porta 50051
EXPOSE 50051

# Comando para rodar a aplicação
CMD ["npm", "run", "start"]
