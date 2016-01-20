__author__ = 'pascal'

doc1 = {"China", "Chinese", "Beijing", "Chinese"}
doc2 = {"China", "Chinese", "Chinese", "Shanghai"}
doc3 = {"China", "Chinese", "Macao"}
doc4 = {"Japan", "Tokyo", "Japan", "Chinese"}


docs = [{doc1, doc2, doc3},
        {doc4}]
classes = {"China", "Japan"}
vocabulary_all = {"Chinese", "Beijing", "Shanghai", "Macao", "Tokyo", "Japan"}
N = [len(docs[0]), len(docs[1])]
vocab = [{"Chinese", "Beijing", "Shanghai", "Macao"},
         {"Chinese", "Tokyo", "Japan"}]
terms = [{"Chinese": 5, "Beijing": 1, "Shanghai": 1, "Macao": 1, "Tokyo": 0, "Japan": 0},
         {"Chinese": 1, "Beijing": 0, "Shanghai": 0, "Macao": 0, "Tokyo": 1, "Japan": 1}]

def count_tokens_of_terms_in_china(dict):
    count = 0
    for key in dict:
        count = count + dict[key] + 1


def count_tokens_of_terms_in_japan(dict):
    count = 0
    for key in dict:
        count = count + dict[key] + 1

# Training
condprob =  [
                {
                    "Chinese": (terms[0]["Chinese"] + 1) / count_tokens_of_terms_in_china(terms[0]),
                    "Japan"  : (terms[0]["Japan"]   + 1) / count_tokens_of_terms_in_china(terms[0]),
                    "Tokyo"  : (terms[0]["Tokyo"]   + 1) / count_tokens_of_terms_in_china(terms[0])}
                ,
                {
                    "Chinese": (terms[1]["Chinese"] + 1) / count_tokens_of_terms_in_japan(terms[1]),
                    "Japan"  : (terms[1]["Japan"]   + 1) / count_tokens_of_terms_in_japan(terms[1]),
                    "Tokyo"  : (terms[1]["Tokyo"]   + 1) / count_tokens_of_terms_in_japan(terms[1])
                }
]




