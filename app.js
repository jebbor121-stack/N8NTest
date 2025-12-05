document.addEventListener('DOMContentLoaded', () => {
    console.log('App loaded successfully!');
    const welcomeMessageElement = document.getElementById('welcome-message');
    if (welcomeMessageElement) {
        welcomeMessageElement.textContent = 'Welcome to our awesome app! We're glad you're here!';
    }
});