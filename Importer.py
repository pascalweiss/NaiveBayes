__author__ = 'pascal'

import glob
from LabeledData import LabeledData
from LabeledDoc import LabeledDoc
import string

class Importer:
    stopwords = []

    def add_stop_words(self, folder_path):
        for filename in glob.glob(folder_path + '*.txt'):
            with open(filename, encoding='utf8') as f:
                words = f.read().split()
                terms = list(map(self._clean_string, words))
                self.stopwords += terms

    def extract_training_data(self, folder_path, label):
        """
        files needs to be in subfolder 'train'
        files need suffix .txt
        :param folder_path:
        :return: Object of type LabeledData
        """
        return LabeledData(label, self._import_files(folder_path + 'train/', label))

    def extract_test_data(self, folder_path, label):
        """
        files needs to be in subfolder 'test'
        files need suffix .txt
        :param folder_path:
        :return: list of strings with content
        """
        return LabeledData(label, self._import_files(folder_path + 'test/', label))

    def _import_files(self, path, label):
        data = []
        for filename in glob.glob(path + '*.txt'):
            with open(filename, encoding='utf8') as f:
                text = f.read()
                words = text.split()
                terms = list(map(self._filter_stopwords, words))
                terms = list(filter(None, terms))
                terms = list(map(self._clean_string, terms))
                terms = list(filter(None, terms))
                # data.append(terms)
                data.append(LabeledDoc(label, terms, filename))
        return data

    def _clean_string(self, str):
        # filtered_str = ''.join(e for e in str if e.isalnum()).lower()
        # if filtered_str != '':
        #     return filtered_str
        result = str.translate(str.maketrans("", "", string.punctuation)).lower()
        return result


    def _filter_stopwords(self, str):
        if str not in self.stopwords:
            return str