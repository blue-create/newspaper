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
        docs_sw = [[tok.text for tok in doc if 
            # remove stopwords 
            tok.is_stop == False and 
            # remove punctuation
            tok.is_punct == False and
            # remove numbers
            tok.is_digit == False and
            # remove whitespace
            tok.is_space == False] 
            for doc in docs]
        # lemmatize 
        docs_lem = [[tok.lemma_ for tok in doc] for doc in docs_sw]