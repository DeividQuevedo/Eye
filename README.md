<b>Eye Monitoring</b>

Este é um projeto de monitoramento ocular desenvolvido em Python utilizando Flask para a interface web e OpenCV para processamento de imagem.

<b>Funcionalidades:</b>

Visualização da Câmera: Exibe o feed de vídeo da câmera em tempo real na interface web.
Detecção de Pontos Faciais: Utiliza o modelo dlib para detectar e exibir pontos faciais no vídeo da câmera.
Ativação e Desativação da Câmera: Permite iniciar e parar a transmissão do vídeo com um botão na interface web.

<b>1.Requisitos</b>

Certifique-se de ter Python 3 instalado. Você pode instalar as dependências necessárias usando o arquivo requirements.txt:

pip install -r requirements.txt

<b>2.Como Executar</b>

<b>2.1. Clone o repositório:</b>

git clone https://github.com/seu_usuario/eye-monitoring.git

cd eye-monitoring

<b>2.2. Instale as dependências:</b>

pip install -r requirements.txt

<b>2.3. Execute a aplicação:</b>

python app.py

<b>2.4. Acesse a aplicação:</b>

Abra o navegador e vá para http://127.0.0.1:5000.

<b>Estrutura do Projeto</b>

app.py: Script principal que configura e inicia a aplicação Flask.
templates/: Diretório contendo os templates HTML para a interface web.
static/: Diretório contendo arquivos estáticos como CSS e JavaScript.
detection/: Diretório contendo módulos Python para processamento de imagem e detecção facial.
haarcascade_frontalface_default.xml: Arquivo XML usado para detecção de faces (se necessário).

<b>Contribuições</b>

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para sugestões ou problemas encontrados.

Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
