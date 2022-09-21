class Preprocessor:
    def __init__(self, newspaper_data, nlp, stopwords):
        self.title = newspaper_data[0]
        self.newspaper = newspaper_data[3]
        self.text = newspaper_data[1]
        self.date = newspaper_data[2]
        self.nlp = nlp
        self.stopwords = stopwords

    def preprocess(self):
        # create doc object containing token features
        docs = list(self.nlp.pipe(self.text))
        docs_post = [[tok.lemma_ for tok in doc if
                    # remove stopwords
                    tok.is_stop == False and
                    # remove punctuation
                    tok.is_punct == False and
                    # remove numbers
                    tok.is_digit == False and
                    # remove whitespace
                    tok.is_space == False and
                    # only include ASCII characters
                    tok.is_ascii = True]
                   for doc in docs]
        self.text_post = docs_post
