function sendScreenSize(id, csrf_token) {
    var csrf = csrf_token;
    
    const width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    const height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

    fetch('', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            id: id,
            width: width,
            height: height,
            csrfmiddlewaretoken: csrf,
        }),
    })
    .then(response => response.json())
    .then(responseData => {
        console.log(responseData);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}