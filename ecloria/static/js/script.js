
// nav toggle

const toggle = document.querySelector('.nav-toggle');
const menu = document.querySelector('.tabs ul');

toggle.addEventListener('click', () => {
    menu.classList.toggle('show');
});

// search field 
const searchBtn = document.getElementById("searchBtn");
const searchInput = document.querySelector(".search-input");

searchBtn.addEventListener("click", () => {
    searchInput.classList.toggle("show");
    if (searchInput.classList.contains("show")) {
        searchInput.focus();
    }
});

// slider /////////////////////////////////////////////////////

