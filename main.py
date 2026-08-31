from pull_request import PullRequest
from notification_service import NotificationService

def main():
    pr = PullRequest(
        repository="Code_modify",
        pr_number=16,
        pr_url="https://github.com/Mounashree-2310/Code_modify",
        action="opened",
    )

    notification = NotificationService()

    message = notification.create_message(pr)

    print(message)


if __name__ == "__main__":
    main()
