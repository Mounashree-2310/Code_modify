class PullRequest:
    def __init__(
        self,
        repository,
        pr_number,
        pr_url,
        action,
    ):
        self.repository = repository
        self.pr_number = pr_number
        self.pr_url = pr_url
        self.action = action