document.getElementById('url-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const longUrl = document.getElementById('long-url').value;

    // Send the POST request with the long URL
    const response = await fetch('/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ long_url: longUrl })
    });

    const data = await response.json();

    // Display the shortened URL if the response is correct
    if (data.short_url) {
        document.getElementById('result').innerHTML = `Shortened URL: <a href="${data.short_url}" target="_blank">${data.short_url}</a>`;
    } else {
        document.getElementById('result').innerHTML = 'Error shortening URL.';
    }
});
