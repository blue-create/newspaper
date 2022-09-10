class Preprocessor:
    def __init__(self, newspaper_data):
        self.title = newspaper_data.title
        self.newspaper = newspaper_data.newspaper
        self.text = newspaper_data.text
        self.date = newspaper_data.date

    def preprocess(self):
        self.text = self.text.lower()