

class FewShotPosts:
    def __init__(self, filepath="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None