import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJjYi5zYy51NGN5czIzMDQ3QGNiLnN0dWRlbnRzLmFtcml0YS5lZHUiLCJleHAiOjE3NzgwNjI4NDIsImlhdCI6MTc3ODA2MTk0MiwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6IjkwZGZiYTA5LTczMDctNGMyYy05NzM1LWI4NTIxNjk3YjFhNiIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6InNyaW5pZGhpIiwic3ViIjoiZmQzNTY3YWYtYTlkZi00NmNkLWJmY2YtMTcwZWZjNTUzNWZmIn0sImVtYWlsIjoiY2Iuc2MudTRjeXMyMzA0N0BjYi5zdHVkZW50cy5hbXJpdGEuZWR1IiwibmFtZSI6InNyaW5pZGhpIiwicm9sbE5vIjoiY2Iuc2MudTRjeXMyMzA0NyIsImFjY2Vzc0NvZGUiOiJQVEJNbVEiLCJjbGllbnRJRCI6ImZkMzU2N2FmLWE5ZGYtNDZjZC1iZmNmLTE3MGVmYzU1MzVmZiIsImNsaWVudFNlY3JldCI6InBHZVFRUWV5WU1qdUpoc2cifQ.WdPzFAZqFEMI47C17vTb-V4t0l6zyiwIoog7QWrc7Sg"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

API = "http://20.207.122.201/evaluation-service/notifications"


def fetch_notifications():
    res = requests.get(API, headers=HEADERS)
    return res.json()["notifications"]


def priority_score(notification):
    type_weight = {
        "Placement": 3,
        "Result": 2,
        "Event": 1
    }
    return type_weight.get(notification["Type"], 0)


def main():
    notifications = fetch_notifications()

    notifications.sort(
        key=lambda x: (priority_score(x), x["Timestamp"]),
        reverse=True
    )

    top10 = notifications[:10]

    print("Top 10 Notifications:")
    for n in top10:
        print(n)


if __name__ == "__main__":
    main()
