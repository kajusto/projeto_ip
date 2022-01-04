#imagem a ser utilizada como ponto de partida
FROM alpine

#define a pasta dentro do container onde comandos serão executados
WORKDIR /app

# Install python/pip
RUN apk add --no-cache python3 py3-pip

#copia arquivos local para container
COPY . /app/

#porta a ser liberada
EXPOSE 5000

#executa o container
CMD ["python3", "api_karina.py"]