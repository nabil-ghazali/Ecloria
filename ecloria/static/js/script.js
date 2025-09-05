const button = document.getElementById('change-style');
const helloText = document.getElementById('hello-text');

button.addEventListener('click', () => {
    const colors = ['red', 'green', 'purple', 'orange', 'brown'];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    const randomSize = Math.floor(Math.random() * 30) + 30; // 30px à 60px

    helloText.style.color = randomColor;
    helloText.style.fontSize = randomSize + 'px';
});
