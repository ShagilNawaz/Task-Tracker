import { useEffect, useState } from "react";
import { fetchTasks } from "../api/tasks";

export default function TaskList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetchTasks().then(setTasks);
  }, []);

  return (
    <ul>
      {tasks.map((task) => (
        <li key={task.id}>
          {task.title} - {task.completed ? "✅" : "❌"}
        </li>
      ))}
    </ul>
  );
}