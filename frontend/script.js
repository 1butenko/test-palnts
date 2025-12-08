document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registrationForm');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const fname = document.getElementById("fname").value;
        const sname = document.getElementById("sname").value;
        const program = document.getElementById("program").value;

        const dataToSend = {
            "first-name": fname,
            "second-name": sname,
            "program": program
        };

        fetch('http://localhost:4040/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dataToSend)
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                window.location.href = 'exam.html';
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Registration failed. Please try again.');
            });
    });
});