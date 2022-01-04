import flask

from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] - True

@app.route('/api', methods=['POST'])
def ip():
        
    #input = input('Informe o IP: ') 172.17.135.233/25 - 172.17.135.129/24
    id_rede = request.json['id_rede']

    #Separar o IP da máscara (bitcount)
    separar = id_rede.split('/')
    ip = separar[0]
    mascara = separar[1]

    #Converter o IP para binário
    #Separar cada octeto (A,B,C e D)
    octeto = ip.split('.')
    a = octeto[0]
    b = octeto[1]
    c = octeto[2]
    d = octeto[3]

    #Converte cada octeto para binário (Abin, Bbin, Cbin, Dbin)
    Abin = bin(int(a))[2:]
    Bbin = bin(int(b))[2:]
    Cbin = bin(int(c))[2:]
    Dbin = bin(int(d))[2:]

    #Converte cada binário em string, com 8 caracteres completando com 0 a esquerda
    AbinStr = Abin.zfill(8) #acrescenta zero a esquerda
    BbinStr = Bbin.zfill(8)
    CbinStr = Cbin.zfill(8)
    DbinStr = Dbin.zfill(8)

    #Concatenar AbinStr, BbinStr, CbinStr, DbinStr
    IPbinStr = AbinStr + BbinStr + CbinStr + DbinStr

    #Identificar o IP de rede
    Nmascara = int(mascara)
    NetbinStr = IPbinStr[:Nmascara] 
    NetbinStr = NetbinStr.ljust(32,'0') #acrescenta a direita os zeros

    #Converter para decimal em 4 octetos
    PrimeiroOcteto = NetbinStr[0:8]
    SegundoOcteto  = NetbinStr[8:16]
    TerceiroOcteto = NetbinStr[16:24]
    QuartoOcteto   = NetbinStr[24:32]

    #converte de binario para decimal
    Adec = int(PrimeiroOcteto,2) 
    Bdec = int(SegundoOcteto,2)
    Cdec = int(TerceiroOcteto,2)
    Ddec = int(QuartoOcteto,2)

    ID_rede = str(Adec) +'.'+ str(Bdec) +'.'+ str(Cdec) +'.'+ str(Ddec) + '/' + mascara
    Default_gateway = str(Adec) +'.'+ str(Bdec) +'.'+ str(Cdec) +'.'+ str(Ddec +1)

    return jsonify(ID_rede=ID_rede, Default_gateway=Default_gateway)      

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)