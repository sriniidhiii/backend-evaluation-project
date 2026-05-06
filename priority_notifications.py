import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJjYi5zYy51NGN5czIzMDQ3QGNiLnN0dWRlbnRzLmFtcml0YS5lZHUiLCJleHAiOjE3NzgwNjQ5ODEsImlhdCI6MTc3ODA2NDA4MSwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6ImM1ZjIzMTBhLTZmN2ItNGVkNS04ZTFmLTkzM2FhNzAxNTk3MSIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6InNyaW5pZGhpIiwic3ViIjoiZmQzNTY3YWYtYTlkZi00NmNkLWJmY2YtMTcwZWZjNTUzNWZmIn0sImVtYWlsIjoiY2Iuc2MudTRjeXMyMzA0N0BjYi5zdHVkZW50cy5hbXJpdGEuZWR1IiwibmFtZSI6InNyaW5pZGhpIiwicm9sbE5vIjoiY2Iuc2MudTRjeXMyMzA0NyIsImFjY2Vzc0NvZGUiOiJQVEJNbVEiLCJjbGllbnRJRCI6ImZkMzU2N2FmLWE5ZGYtNDZjZC1iZmNmLTE3MGVmYzU1MzVmZiIsImNsaWVudFNlY3JldCI6InBHZVFRUWV5WU1qdUpoc2cifQ.4wFf_cCLnBJf2MKUuf48NoWCSMLP-jRXTWmFH2CstKg"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

API = "http://20.207.122.201/evaluation-service/notifications"

# Priority mapping
PRIORITY = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}


def fetch_notifications():
    response = requests.get(API, headers=HEADERS)
    return response.json()["notifications"]


def sort_notifications(notifications):
    return sorted(
        notifications,
        key=lambda x: (
            PRIORITY[x["Type"]],
            x["Timestamp"]
        ),
        reverse=True
    )


def main():
    notifications = fetch_notifications()
    top10 = sort_notifications(notifications)[:10]

    print("\nTop 10 Priority Notifications:\n")
    for n in top10:
        print(n)


if __name__ == "__main__":
    main()