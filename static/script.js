document.getElementById('searchForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const user = document.getElementById('user').value;
  const senha = document.getElementById('senha').value;
  const search = document.getElementById('search').value;

  const response = await fetch('/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user, senha, search })
  });

  const jobs = await response.json();
  const jobList = document.getElementById('jobList');
  jobList.innerHTML = '';

  jobs.forEach(job => {
      const li = document.createElement('li');
      li.innerHTML = `<a href="${job.url}" target="_blank">${job.titulo}</a>`;
      jobList.appendChild(li);
  });
});
