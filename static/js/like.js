
 /* idea like  */
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
             console.log(`Idea ${ideaId} likes updated to ${data.like_count}`);
             document.getElementById(`likes-count-${ideaId}`).innerText = data.like_count;
             let icon = document.getElementById(`like-icon-${ideaId}`);
             if (data.status === 'like') {
                 icon.style.color = 'red'; // Qizil rangda
             } else {
                 icon.style.color = 'black'; // Odatdagi rang
             }
         } else {
             console.error('Unexpected response:', data);
         }
     })
     .catch(error => console.error('Error:', error));
 }


 /* post like  */


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
             console.log(`Event ${eventId} likes updated to ${data.like_count}`);
             document.getElementById(`likes-count-${eventId}`).innerText = data.like_count;
             let icon = document.getElementById(`like-icon-${eventId}`);
             if (data.status === 'like') {
                 icon.style.color = 'red';
             } else {
                 icon.style.color = 'black';
             }
         } else {
             console.error('Unexpected response:', data);
         }
     })
     .catch(error => console.error('Error:', error));
 }

