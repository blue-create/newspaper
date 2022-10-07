import spacy
from modules.preprocess_articles import *

""" Docustring comment for testing:
	unfortunately it seems we will have to restructure 
	this entire thing as a package for it to work
	
	Will do this later

"""

def test_preprocessor():
    # given
    text = ["!Seit@dem ran'k.£t s*ic)h um Ma3llor$y d5%as 0grö^ßte Myste/£ri$m"]
    expected = ['seitdem', 'rankt', 'sich', 'um', 'mallory', 'das', 'größte', 'mysterium']
    
    spacy_model = spacy.load("de_core_news_lg", disable=['ner', 'parser', 'tagger'])
    
    # when
    text_pre = Preprocessor(newspaper_data = text, nlp = spacy_model)
    text_pre.tokenize()
    text_pre.preprocess()
    
    text_preprocessed = text_pre.return_preprocessed()
    
    # then
    assert text_preprocessed == expected
    
