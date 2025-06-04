export async function fetchTasks() {
  const res = await fetch("http://localhost:5000/tasks");
  return await res.json();
}

export async function addTask(title) {
  return fetch("http://localhost:5000/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });
}