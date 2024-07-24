const rate = (rating, post_id) => {
    fetch(`/rating/rate/${post_id}/${rating}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            window.location.reload();
        }
    });
}
