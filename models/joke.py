class Joke:
    def __init__(self, words: list[str]):
        self.setup = words[0].capitalize()
        self.punchline = words[1].capitalize()
        self.joke = f"""
            Knock knock.
            Who's there?
            {self.setup}.
            {self.setup} who?
            {self.punchline}!
        """
    
    def tell(self):
        print(self.joke)