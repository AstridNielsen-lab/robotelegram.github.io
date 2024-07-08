# Aplicativo de Interação com Telegram usando Flask

Este repositório contém um aplicativo Flask desenvolvido para interagir com o Telegram. O aplicativo permite enviar mensagens para o Telegram, aguardar a resposta e reproduzir a resposta como áudio.

## Instalação

Siga os passos abaixo para configurar e executar o aplicativo localmente:

### Pré-requisitos

- Python 3.6 ou superior instalado
- Conta Telegram válida e API ID/API Hash obtidos do Telegram Apps.

### Passos de Instalação

1. Clone nosso repositório:
   ```bash
   git clone https://github.com/AstridNielsen-lab/robotelegram.github.io
   cd robotelegram.github.io
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   . venv/bin/activate  # No Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
     ```plaintext
     API_ID=seu_api_id_do_telegram
     API_HASH=sua_api_hash_do_telegram
     ```

4. **Protegendo suas Chaves de API**
   Certifique-se de que suas chaves de API e outras informações sensíveis não sejam commitadas no repositório. Utilize um arquivo `.gitignore` para evitar isso. Seu arquivo `.gitignore` deve incluir:
   ```plaintext
   .env
   ```

### Uso

1. Execute o aplicativo:
   ```bash
   python main.py
   ```

2. O aplicativo Flask será executado localmente em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Acesse o aplicativo Flask no seu navegador.
   - Insira a mensagem desejada no campo de texto e clique em "Enviar".
   - Aguarde a resposta do Telegram ser exibida na página.
   - Para reproduzir a resposta como áudio, clique no botão "Reproduzir Áudio".

### Contribuição

Contribuições são bem-vindas! Para sugestões, melhorias ou correções, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Links Úteis

Para saber mais sobre a Radio Tatuapé FM e outros setores da Like Look Solutions CNPJ 36.992.198/0001-84, visite os links abaixo:

- Nossa Rádio no Tatuapé: [https://www.radiotatuapefm.com.br](https://www.radiotatuapefm.com.br)
- Setor de Marketing Comercial: [https://likelook.wixsite.com/marketing](https://likelook.wixsite.com/marketing)
- Setor de Ensino Social de Tecnologia: [https://radiotatuapefm.wixsite.com/disparattechno](https://radiotatuapefm.wixsite.com/disparattechno)
- Setor de Avanços em Tecnologia Comercial: [https://likelook.wixsite.com/solutions](https://likelook.wixsite.com/solutions)

### Imagens

![Tela](https://raw.githubusercontent.com/AstridNielsen-lab/robotelegram.github.io/index.html/Tela.jpeg)

![Código](https://raw.githubusercontent.com/AstridNielsen-lab/robotelegram.github.io/index.html/code.jpeg)