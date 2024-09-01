document.getElementById("submit-button").addEventListener("click", function() {
    var query = document.getElementById("query-input").value;
    var type = document.querySelector('input[name="type"]:checked').value;
    var formData = new FormData();
    formData.append("query", query);
    formData.append("type", type);

    fetch("/analyze", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.summary) {
            document.getElementById("summary-output").textContent = data.summary;
        }
        if (data.sentiment) {
            document.getElementById("sentiment-output").textContent = data.sentiment;
        }
        if (data.error) {
            document.getElementById("error-output").textContent = data.error;
        }
    })
    .catch(error => console.error("Error:", error));
});