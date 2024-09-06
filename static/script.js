document.addEventListener('DOMContentLoaded', () => {
    // Clear local storage on page load
    localStorage.clear();

    // Load saved data from local storage
    const elements = document.querySelectorAll('input, select');
    elements.forEach(element => {
        const value = localStorage.getItem(element.id);
        if (value !== null) {
            if (element.type === 'number') {
                element.value = Number(value);
            } else {
                element.value = value;
            }
        }
    });

    // Save data to local storage on input change
    document.getElementById('predictionForm').addEventListener('input', (event) => {
        localStorage.setItem(event.target.id, event.target.value);
    });
});
