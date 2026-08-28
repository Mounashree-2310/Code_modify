from pull_request import PullRequest
from notification_service import NotificationService

def test_pr_creation():
    pr = PullRequest(
        "TestRepo",
        1,
        "Mounashree",
    )
    assert pr.repository == "TestRepo"
    assert pr.pr_number == 1
    assert pr.created_by == "Mounashree"

def test_notification_object():
    notification = NotificationService(
        "https://test-url.com"
    )
    assert (
        notification.flow_url
        == "https://test-url.com"
    )