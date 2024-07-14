function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function likeIdea(ideaId) {
    fetch(`/like/idea/${ideaId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'like' || data.status === 'unlike') {
            document.getElementById(`likes-count-${ideaId}`).innerText = data.like_count;
            let icon = document.getElementById(`like-icon-${ideaId}`);
            if (data.status === 'like') {
                icon.style.color = 'red';
                localStorage.setItem(`like-idea-${ideaId}`, 'liked');
            } else {
                icon.style.color = 'black';
                localStorage.removeItem(`like-idea-${ideaId}`);
            }
        } else {
            console.error('Unexpected response:', data);
        }
    })
    .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.like-icon').forEach(icon => {
        const ideaId = icon.getAttribute('id').split('-')[2];
        if (localStorage.getItem(`like-idea-${ideaId}`) === 'liked') {
            icon.style.color = 'red';
        }
    });
});


function likeEvent(eventId) {
    fetch(`/like/event/${eventId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'like' || data.status === 'unlike') {
            document.getElementById(`likes-count-${eventId}`).innerText = data.like_count;
            let icon = document.getElementById(`like-icon-${eventId}`);
            if (data.status === 'like') {
                icon.style.color = 'red';
                localStorage.setItem(`like-event-${eventId}`, 'liked');
            } else {
                icon.style.color = 'black';
                localStorage.removeItem(`like-event-${eventId}`);
            }
        } else {
            console.error('Unexpected response:', data);
        }
    })
    .catch(error => console.error('Error:', error));
}

// Page load
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.like-icon').forEach(function(icon) {
        const ideaId = icon.id.split('-').pop();
        if (localStorage.getItem(`like-idea-${ideaId}`) === 'liked') {
            icon.style.color = 'red';
        }
    });

    document.querySelectorAll('.like-icon').forEach(function(icon) {
        const eventId = icon.id.split('-').pop();
        if (localStorage.getItem(`like-event-${eventId}`) === 'liked') {
            icon.style.color = 'red';
        }
    });
});
