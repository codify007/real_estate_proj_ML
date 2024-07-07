document.addEventListener('DOMContentLoaded', function() {
    // Load the JSON file and populate the dropdown
    fetch('./public/columns.json')  // Correct path to your JSON file
        .then(response => response.json())
        .then(data => {
            const locations = data.data_columns.filter(column => !["total_sqft", "bath", "bhk"].includes(column));
            const selectElement = document.getElementById('location');
            locations.forEach(location => {
                const option = document.createElement('option');
                option.value = location;
                option.textContent = location;
                selectElement.appendChild(option);
            });
        })
        .catch(error => console.error('Error loading locations:', error));

    // Add event listener to the calculate button
    document.getElementById('calculate-price').addEventListener('click', function() {
        const location = document.getElementById('location').value;
        const area = document.getElementById('area').value;
        const bathrooms = document.getElementById('bathrooms').value;
        const bhk = document.getElementById('bhk').value;

        // Validate inputs
        if (location && area && bathrooms && bhk) {
            // Send the data to the Flask server
            fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    location: location,
                    area: area,
                    bathrooms: bathrooms,
                    bhk: bhk
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.querySelector('.total-price').textContent = 'Total price: ' + data.price;
                } else {
                    console.error('Error in prediction:', data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        } else {
            alert('Please fill all the fields.');
        }
    });
});




