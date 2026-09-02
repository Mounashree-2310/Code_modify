

class NotificationService:
    def create_message(self, pull_request):
        return (
            f"A new Pull Request has been created.\n"
            f"Repository Name: {pull_request.repository}\n"
            f"Pull Request Number: {pull_request.pr_number}\n"
            f"Pull Request: {pull_request.pr_url}\n"
            f"Action: {pull_request.action}"
        )
