__author__ = 'pascal'

from Importer import Importer
from NaiveBayes import NaiveBayes



importer = Importer()

print('Loading stop words')
importer.add_stop_words('data/stopwords/german/')

# Importing training sets
training_data = []
print('Loading training data')
training_data.append(importer.extract_training_data('data/politik/',    label='politik'))
training_data.append(importer.extract_training_data('data/wirtschaft/', label='wirtschaft'))
training_data.append(importer.extract_training_data('data/sport/',      label='sport'))

nb = NaiveBayes()
print('Training')
nb.train(training_data)
# Importing test sets
test_data = []

print('Loading test data')
test_data.append(importer.extract_test_data('data/politik/',    label='politik'))
test_data.append(importer.extract_test_data('data/sport/',      label='sport'))
test_data.append(importer.extract_test_data('data/wirtschaft/', label='wirtschaft'))

print('Testing')
accuracy = nb.test(test_data)
print('accuracy: ' + str(accuracy))

