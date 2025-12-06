const sButton = document.getElementById('submit');

sButton.addEventListener("click", () => {
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
        })
        .catch(error => {
            console.error('Error:', error);
        });
});