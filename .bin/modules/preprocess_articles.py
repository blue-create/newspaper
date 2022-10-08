class Preprocessor:
""" Docustring for comments about this class:
    
    Different pre-processing steps should live in separate functions
    
        Usual steps: 
        > lowercase 
        > remove punctuation/numbers/special characters 
        > tokenize (using spacy pipe) 
        > remove stopwords (maybe using nltk list)
        > lemmatize (NB: should be a separate function for this)
        
     Functions should not alter corpus metadata (date/newspaper)! 
         Exception: title may need to be tidied up {task for later}
         
         Current behaviour: preprocessor removes all other indexes 
         eg. title/date/newspaper is not returned
         
"""
    
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
