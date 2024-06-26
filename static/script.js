document.addEventListener('DOMContentLoaded', function() {
    let videoPlayer = document.getElementById('video-feed');
    let toggleCameraBtn = document.getElementById('toggle-camera');
    let startStopBtn = document.getElementById('start-stop');
    let streaming = false;

    // Função para alternar a câmera ligada/desligada
    toggleCameraBtn.addEventListener('click', function() {
        if (streaming) {
            videoPlayer.pause();
            streaming = false;
            toggleCameraBtn.textContent = 'Turn Camera On';
        } else {
            videoPlayer.play();
            streaming = true;
            toggleCameraBtn.textContent = 'Turn Camera Off';
        }
    });

    // Lógica para iniciar/parar a aplicação (simulação)
    startStopBtn.addEventListener('click', function() {
        alert('Starting/Stopping the application!');
    });
});
