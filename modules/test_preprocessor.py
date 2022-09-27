import spacy
from preprocess_articles import Preprocessor

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
    