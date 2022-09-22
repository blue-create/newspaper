class Preprocessor:
    def __init__(self, newspaper_data, nlp):
        self.title = newspaper_data[0]
        self.newspaper = newspaper_data[3]
        self.text = newspaper_data[1]
        self.date = newspaper_data[2]
        self.nlp = nlp

    def tokenize(self):
        # tokenize corpus
        docs = self.nlp.pipe(self.text)
        self.docs = docs

    def preprocess(self):
        # create doc object containing token features
        docs_preprocessed = [[tok.lemma_ for tok in doc if
                    # remove stopwords
                    tok.is_stop == False and
                    # remove punctuation
                    tok.is_punct == False and
                    # remove numbers
                    tok.is_digit == False and
                    # remove whitespace
                    tok.is_space == False and
                    # only include tokens of alphabetic characters
                    tok.is_alpha == True and 
                    # remove emails
                    tok.like_email == False
                    ]
                   for doc in self.docs]
        self.docs_preprocessed = docs_preprocessed

    def return_docs(self): 
        return self.docs

    def return_preprocessed(self):
        return self.docs_preprocessed
