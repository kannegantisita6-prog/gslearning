fetch("/api/courses")
.then(res => res.json())
.then(data => {
  const container = document.getElementById("courses");
  data.forEach(c => {
    const div = document.createElement("div");
    div.innerHTML = `<h3>${c.title}</h3><a href="${c.url}" target="_blank">Watch</a><hr/>`;
    container.appendChild(div);
  });
});
