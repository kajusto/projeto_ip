#imagem a ser utilizada como ponto de partida
FROM alpine

#define a pasta dentro do container onde comandos serão executados
WORKDIR /app

# Install python/pip
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip install Flask

#copia arquivos local para container
COPY . /app/

#porta a ser liberada
EXPOSE 5000

#executa o container
CMD ["python3", "api_karina.py"]