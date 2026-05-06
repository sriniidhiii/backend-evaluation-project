const express = require("express");
const Log = require("./logging_middleware/logger");

const app = express();
app.use(express.json());

const TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJjYi5zYy51NGN5czIzMDQ3QGNiLnN0dWRlbnRzLmFtcml0YS5lZHUiLCJleHAiOjE3NzgwNTgzNjQsImlhdCI6MTc3ODA1NzQ2NCwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6ImJmOGU5ZjIxLTc3ZmMtNDQ5Zi04N2MxLTEyOGEwNWUyYTBjYyIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6InNyaW5pZGhpIiwic3ViIjoiZmQzNTY3YWYtYTlkZi00NmNkLWJmY2YtMTcwZWZjNTUzNWZmIn0sImVtYWlsIjoiY2Iuc2MudTRjeXMyMzA0N0BjYi5zdHVkZW50cy5hbXJpdGEuZWR1IiwibmFtZSI6InNyaW5pZGhpIiwicm9sbE5vIjoiY2Iuc2MudTRjeXMyMzA0NyIsImFjY2Vzc0NvZGUiOiJQVEJNbVEiLCJjbGllbnRJRCI6ImZkMzU2N2FmLWE5ZGYtNDZjZC1iZmNmLTE3MGVmYzU1MzVmZiIsImNsaWVudFNlY3JldCI6InBHZVFRUWV5WU1qdUpoc2cifQ.kKauzcQJ8i7CWB3yALtNre-l1bavlSa0pdxtiUhg0U0";

app.get("/", async (req, res) => {
  await Log("backend", "info", "route", "Root API hit", TOKEN);
  res.status(200).send("Home route working");;
});

app.get("/error", async (req, res) => {
  await Log("backend", "error", "handler", "Test error log", TOKEN);
  res.status(200).send("Error route working");
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});