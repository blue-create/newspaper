class CollocationArticles:
    def __init__(self, documents, nltk_collocations):
        self.documents = documents
        self.nltk_collocations = nltk_collocations

    def BigramCollocations(self, top_n=10, min_freq=3, doc_type=True):
        if doc_type == True:
            finder = self.nltk_collocations.BigramCollocationFinder.from_documents(self.documents)
            finder.apply_freq_filter(min_freq)
            return finder.nbest(self.nltk_collocations.BigramAssocMeasures().likelihood_ratio, top_n)
        else:
            finder = self.nltk_collocations.BigramCollocationFinder.from_words(self.documents)
            finder.apply_freq_filter(min_freq)
            return finder.nbest(self.nltk_collocations.BigramAssocMeasures().likelihood_ratio, top_n)

    def TrigramCollocations(self, top_n=10, min_freq=3, doc_type=True):
        if doc_type == True:
            finder = self.nltk_collocations.TrigramCollocationFinder.from_documents(self.documents)
            finder.apply_freq_filter(min_freq)
            return finder.nbest(self.nltk_collocations.TrigramAssocMeasures().likelihood_ratio, top_n)

        else:
            finder = self.nltk_collocations.TrigramCollocationFinder.from_words(self.documents)
            finder.apply_freq_filter(min_freq)
            return finder.nbest(self.nltk_collocations.TrigramAssocMeasures().likelihood_ratio, top_n)
