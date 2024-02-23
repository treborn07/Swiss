# Swiss
# Projeto de Chatbot e Ferramentas de Rede

#ABRA COM SUPER USUÁRIO!


Este é um projeto Python que consiste em dois arquivos: `chatbot.py` e `ferramentas_rede.py`. O `chatbot.py` implementa um chatbot simples que pode interagir com os usuários, enquanto o `ferramentas_rede.py` fornece várias funcionalidades relacionadas à rede, como localizar IP, encontrar o nome de host associado a um IP, verificar portas abertas, listar clientes conectados à rede Wi-Fi, entre outros.

## Requisitos

Este projeto requer as seguintes bibliotecas Python:

- `json`: Para manipulação de arquivos JSON.
- `difflib`: Para cálculo de similaridade entre sequências de texto.
- `textblob`: Para correção ortográfica e análise de texto (usado apenas no chatbot).
- `requests`: Para fazer solicitações HTTP (usado apenas nas ferramentas de rede).
- `socket`: Para operações de rede, como localizar endereços IP e encontrar o nome de host associado a um IP (usado apenas nas ferramentas de rede).
- `time`: Para operações relacionadas ao tempo (usado apenas nas ferramentas de rede).
- `subprocess`: Para chamar outros programas a partir do seu código (usado apenas nas ferramentas de rede).
- `os`: Para operações relacionadas ao sistema operacional, como obter o endereço IP público usando o comando `curl` (usado apenas nas ferramentas de rede).
- `whois`: Para consultar informações WHOIS de um domínio (usado apenas nas ferramentas de rede).
- `scapy`: Para realizar operações de varredura de rede e interações com pacotes de rede de forma avançada (usado apenas nas ferramentas de rede).

#IMPORTANTE
digite pip3 install instale as bibliotecas acima para o script funcionar perfeitamente
eles devem estar no mesmo diretório tanto o Wiss.py como o ia.py, ou seja na mesma pasta, mas fique tranquilo que você também pode alterar isso no código.

## Como usar
Abra com python3 ex: python3 Wiss.py
### Chatbot

Para usar o chatbot, execute o arquivo `chatbot.py`. Ele iniciará uma interação onde você pode conversar com o chatbot.

### Ferramentas de Rede

Para usar as ferramentas de rede, execute o arquivo `ferramentas_rede.py`. Ele exibirá um menu com várias opções relacionadas à rede, como localizar IP, encontrar o nome de host associado a um IP, verificar portas abertas, listar clientes conectados à rede Wi-Fi, entre outros. Siga as instruções no menu para utilizar as diferentes funcionalidades.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
