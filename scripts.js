document.addEventListener('DOMContentLoaded', () => {
    const pages = [
        { title: 'Home', file: 'home.html' },
        { title: 'Greek Grammar Tables', file: 'Greek Grammar Tables.html' },
        { title: 'Greek Words You Already (Kinda) Know', file: 'Greek Words You Already (Kinda) Know.html' },
        { title: 'Greek Grammar Tables - BIG', file: 'Greek Grammar Tables - BIG.html' },

    ];

    const pageSelect = document.getElementById('page-select');
    const contentContainer = document.getElementById('content');
    const themeToggle = document.getElementById('theme-toggle');

    // Populate the page select options
    pages.forEach(page => {
        const option = document.createElement('option');
        option.value = page.file;
        option.textContent = page.title;
        pageSelect.appendChild(option);
    });

    // Load the page content based on the selected option
    const loadPageContent = (file) => {
        fetch(`pages/${file}`)
            .then(response => response.text())
            .then(content => {
                contentContainer.innerHTML = content;
            })
            .catch(error => {
                contentContainer.innerHTML = '<p>Error loading content.</p>';
            });
    };

    // Set up event listener for page selection
    pageSelect.addEventListener('change', (event) => {
        loadPageContent(event.target.value);
    });

    // Load the default page
    loadPageContent('home.html');

    // Theme toggle functionality
    const toggleTheme = () => {
        document.documentElement.classList.toggle('dark-mode');
        const isDarkMode = document.documentElement.classList.contains('dark-mode');
        localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
    };

    // Set up event listener for theme toggle
    themeToggle.addEventListener('change', toggleTheme);

    // Load theme preference from local storage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.documentElement.classList.add('dark-mode');
        themeToggle.checked = true;
    }
});