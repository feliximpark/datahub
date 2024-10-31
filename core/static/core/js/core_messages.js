document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        const messageContainers = document.querySelectorAll('.message-container');
        messageContainers.forEach(function(container) {
            container.classList.remove('show');
            container.classList.add('fade');
        });
    }, 3000);
});