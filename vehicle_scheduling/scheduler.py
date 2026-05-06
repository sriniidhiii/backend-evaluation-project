import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJjYi5zYy51NGN5czIzMDQ3QGNiLnN0dWRlbnRzLmFtcml0YS5lZHUiLCJleHAiOjE3NzgwNjI4NDIsImlhdCI6MTc3ODA2MTk0MiwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6IjkwZGZiYTA5LTczMDctNGMyYy05NzM1LWI4NTIxNjk3YjFhNiIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6InNyaW5pZGhpIiwic3ViIjoiZmQzNTY3YWYtYTlkZi00NmNkLWJmY2YtMTcwZWZjNTUzNWZmIn0sImVtYWlsIjoiY2Iuc2MudTRjeXMyMzA0N0BjYi5zdHVkZW50cy5hbXJpdGEuZWR1IiwibmFtZSI6InNyaW5pZGhpIiwicm9sbE5vIjoiY2Iuc2MudTRjeXMyMzA0NyIsImFjY2Vzc0NvZGUiOiJQVEJNbVEiLCJjbGllbnRJRCI6ImZkMzU2N2FmLWE5ZGYtNDZjZC1iZmNmLTE3MGVmYzU1MzVmZiIsImNsaWVudFNlY3JldCI6InBHZVFRUWV5WU1qdUpoc2cifQ.WdPzFAZqFEMI47C17vTb-V4t0l6zyiwIoog7QWrc7Sg"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

DEPOT_API = "http://20.207.122.201/evaluation-service/depots"
VEHICLE_API = "http://20.207.122.201/evaluation-service/vehicles"


# Fetch data from APIs
def fetch_data():
    depots = requests.get(DEPOT_API, headers=HEADERS).json()
    vehicles = requests.get(VEHICLE_API, headers=HEADERS).json()
    return depots, vehicles


# Knapsack logic (maximize impact)
def knapsack(tasks, max_hours):
    n = len(tasks)
    dp = [[0] * (max_hours + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        duration = tasks[i - 1]["Duration"]
        impact = tasks[i - 1]["Impact"]

        for h in range(max_hours + 1):
            if duration <= h:
                dp[i][h] = max(
                    dp[i - 1][h],
                    dp[i - 1][h - duration] + impact
                )
            else:
                dp[i][h] = dp[i - 1][h]

    return dp[n][max_hours]


# Main function
def main():
    depots, vehicles = fetch_data()

    # choose maximum available hours
    max_hours = max(d["MechanicHours"] for d in depots["depots"])

    # get all tasks
    tasks = vehicles["vehicles"]

    print("Max Mechanic Hours:", max_hours)
    print("Total Tasks:", len(tasks))

    result = knapsack(tasks, max_hours)

    print("Max Impact:", result)


if __name__ == "__main__":
    main()
