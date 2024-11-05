document.getElementById('search-form').addEventListener('submit', function(event) {
  event.preventDefault();
  
  const jobTitle = document.getElementById('job-title').value;
  
  fetch('/search', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ title: jobTitle }),
  })
  .then(response => response.json())
  .then(data => {
      const resultsDiv = document.getElementById('results');
      resultsDiv.innerHTML = '';

      if (data.length === 0) {
          resultsDiv.innerHTML = '<p>Nenhuma vaga encontrada.</p>';
          return;
      }

      data.forEach(job => {
          const jobElement = document.createElement('div');
          jobElement.innerHTML = `<a href="${job.url}" target="_blank">${job.titulo}</a>`;
          resultsDiv.appendChild(jobElement);
      });
  })
  .catch(error => {
      console.error('Erro:', error);
  });
});
