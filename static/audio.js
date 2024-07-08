// Função para reproduzir áudio a partir de um arquivo recebido do Flask
function playAudio(audioFileName) {
    var audioElement = new Audio('/static/' + audioFileName); // Ajuste o caminho conforme necessário
    audioElement.play();
}

// Event listener para o botão de reproduzir áudio
document.getElementById('playAudioBtn').addEventListener('click', function() {
    fetch('/send_prompt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: 'Texto a ser enviado para o Telegram' })
    })
    .then(response => response.json())
    .then(data => {
        var audioFileName = data.audioFileName;
        playAudio(audioFileName);
        document.getElementById('responseText').innerText = data.response;
    })
    .catch(error => console.error('Erro ao enviar prompt:', error));
});
