function sendClickInfo(id, choice, csrf_token) {
    var csrf = csrf_token;

    // Get the current URL
    var current_url = window.location.href;

    fetch('', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            id: id,
            choice: choice,
            current_url: current_url,
            csrfmiddlewaretoken: csrf,
        }),
    })

    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json(); // You can adjust this based on your server response type
    })

    .catch(error => {
        console.error("Error:", error);
    });
}