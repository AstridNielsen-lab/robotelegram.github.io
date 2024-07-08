from flask import Flask, request, jsonify, render_template
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from gtts import gTTS
import asyncio
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do Telegram
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
chat_link = os.getenv('CHAT_LINK')

# Inicializa o cliente TelegramClient com StringSession
session_name = 'session_gpt'
client = TelegramClient(StringSession(), api_id, api_hash)

# Inicializa o aplicativo Flask
app = Flask(__name__)
app.static_url_path = '/static'  # Configuração para servir arquivos estáticos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    data = request.get_json()
    prompt = data['prompt']
    response_text, audio_file_name = asyncio.run(handle_telegram_interaction(prompt))
    return jsonify({'response': response_text, 'audioFileName': audio_file_name})

async def handle_telegram_interaction(prompt):
    try:
        async with client:
            print("Conectado ao Telegram.")
            full_prompt = f"/new_chat {prompt}"  # Adiciona o comando /new_chat ao prompt
            await client.send_message(chat_link, full_prompt)
            print(f"Mensagem enviada para {chat_link}.")

            # Aguarda 6 segundos antes de buscar a resposta do Telegram
            await asyncio.sleep(6)

            # Loop para aguardar a resposta do Telegram
            for _ in range(10):  # Tentativas máximas
                messages = await client.get_messages(chat_link, limit=1)
                for message in messages:
                    if message.text:
                        response_text = message.text
                        tts = gTTS(text=response_text, lang='pt')
                        audio_file_name = f"static/response_{message.id}.mp3"
                        tts.save(audio_file_name)  # Salva o arquivo na pasta static
                        print(f"Áudio gerado e salvo: {audio_file_name}")
                        return response_text, audio_file_name
                await asyncio.sleep(1)  # Espera por 1 segundo antes de tentar novamente

            # Se não receber resposta após 10 tentativas
            print("Não foi possível receber resposta do Telegram.")
            return "", ""

    except Exception as e:
        print(f"Erro ao interagir com o Telegram: {e}")
        return "", ""

if __name__ == '__main__':
    app.run(debug=True)
