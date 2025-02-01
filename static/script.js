function updateDetectedObjects() {
    fetch('/detected_objects')
        .then(response => response.json())
        .then(data => {
            const objectList = document.getElementById('object-list');
            objectList.innerHTML = '';
            for (const [obj, count] of Object.entries(data.object_counts)) {
                const li = document.createElement('li');
                li.textContent = `${obj}: ${count}`;
                objectList.appendChild(li);
            }
        });
}

setInterval(updateDetectedObjects, 1000);
