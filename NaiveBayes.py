__author__ = 'pascal'

from LabeledData import LabeledData
from math import log

class NaiveBayes:
    prior_prob = {}
    cond_prob  = {}

    def train(self, labeled_data_list):
        vocab, n_docs  = self._extract_vocab_and_docs_count(labeled_data_list)
        for data_class in labeled_data_list:
            self.prior_prob[data_class.label] = float(len(data_class.data)) / n_docs
            # self.count_words(data_class)
            token_count = self._count_tokens(data_class.data, vocab)
            self.cond_prob[data_class.label] = self._calc_cond_prob(token_count)
            self.write_object_to_disc(data_class.label + '_dict.txt', self.cond_prob[data_class.label])
            pass

    def _count_tokens(self, docs, vocab_dict):
        n_token = vocab_dict.copy()
        for tokens in docs:
            for token in tokens.features:
                n_token[token] += 1
        return n_token


    def _extract_vocab_and_docs_count(self, data_list):
        n_docs = 0
        vocab_dict = {}
        for data_class in data_list:
            n_docs += len(data_class.data)
            for token_list in data_class.data:
                for token in token_list.features:
                    vocab_dict[token] = 0
        return vocab_dict, n_docs

    def _calc_cond_prob(self, token_count):
        cond_prob_class = {}
        for token in token_count:
            cond_prob_class[token] = (token_count[token] + 1) / (sum(token_count.values()) + len(token_count))
        return cond_prob_class

    def test(self, labeled_data_list):
        correct_predictions = 0
        n_predictions = 0
        for labeled_data in labeled_data_list:
            n_predictions += len(labeled_data.data)
            for doc in labeled_data.data:
                prediction = self.predict(doc)
                print(doc.doc_title + ': ' + prediction)
                if prediction == labeled_data.label:
                    correct_predictions += 1
        return correct_predictions / n_predictions

    def predict(self, doc):
        score = {}
        for data_class in self.prior_prob:
            score[data_class] = log(self.prior_prob[data_class])
            for token in doc.features:
                if token in self.cond_prob[data_class]:
                    score[data_class] += log(self.cond_prob[data_class][token])
                    # print(score[data_class])
        return max(score.keys(), key=(lambda k: score[k]))

    def count_words(self, labeledData):
        count = 0
        for doc in labeledData.data:
            count += len(doc.features)
        print('\n' + 'wordcount: ' + labeledData.label + ': ' + str(count))

    def write_object_to_disc(self, filename, data):
        with open(filename, 'w', encoding='utf8') as f:
            f.write(str(data))


