# NaiveBayes
Some text classification, using Naive Bayes, written in python 3 

# Data

There are the 3 classes of text:
politik, wirtschaft, sport
For each of them there is test data and trainings data. Check out the following folder tree: 
```
./data
├── politik
│   ├── test
│   │   ├── p007.txt
...............
│   │   └── p098.txt
│   └── train
│       ├── p001.txt
...............
│       └── p099.txt
├── sport
│   ├── test
│   │   ├── s002.txt
...............
│   │   └── s093.txt
│   └── train
│       ├── s001.txt
│       ├── s003.txt
...............
│       └── s099.txt
├── stopwords
│   └── german
│       ├── stop-words_german_1_de.txt
│       └── stop-words_german_2_de.txt
└── wirtschaft
    ├── test
    │   ├── w002.txt
...............
    │   └── w099.txt
    └── train
        ├── w001.txt
..............
        └── w098.txt
```

# Execution
The test program is in main.py. 
Just execute it with
`python3.4 main.py`
