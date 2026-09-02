from notification_service import NotificationService
from pull_request import PullRequest


def test_pr_creation():
    pr = PullRequest("TestRepo", 1, "https://github.com/test", "opened")

    assert pr.repository == "TestRepo"
    assert pr.pr_number == 1
    assert pr.pr_url == "https://github.com/test"
    assert pr.action == "opened"


def test_notification_message():
    pr = PullRequest("TestRepo", 1, "https://github.com/test", "opened")

    notification = NotificationService()

    message = notification.create_message(pr)

    assert "Repository Name: TestRepo" in message
    assert "Pull Request Number: 1" in message
    assert "Action: opened" in message
