#imagem a ser utilizada como ponto de partida
FROM python:3.8.2-alpine

#define a pasta dentro do container onde comandos serão executados
WORKDIR /app
RUN pip install Flask
RUN pip install requests

#copia arquivos local para container
COPY . /app/

#porta a ser liberada
EXPOSE 5000

#executa o container
CMD ["python3", "api-desafio.py"]