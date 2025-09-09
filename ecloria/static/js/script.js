
// nav toggle

const toggle = document.querySelector('.nav-toggle');
const menu = document.querySelector('.tabs ul');

toggle.addEventListener('click', () => {
    menu.classList.toggle('show');
});
