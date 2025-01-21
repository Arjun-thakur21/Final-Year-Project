// filepath: /d:/Arjun/project/bearing-fault-diagnosis/static/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    // Add any custom JavaScript here
    console.log('Custom JavaScript loaded');
});

// filepath: /d:/Arjun/project/bearing-fault-diagnosis/static/js/scripts.js
document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    themeToggle.addEventListener('click', function () {
        if (body.classList.contains('theme-dark')) {
            body.classList.remove('theme-dark');
            body.classList.add('theme-light');
        } else {
            body.classList.remove('theme-light');
            body.classList.add('theme-dark');
        }
    });
});