# import libraries
import sys
import re
import sqlalchemy as sqla
import pandas as pd
import numpy as np
import pickle
import os
from sklearn import datasets, linear_model
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import make_scorer, accuracy_score, f1_score, fbeta_score, classification_report
from sklearn.externals import joblib
from scipy.stats import hmean
from scipy.stats.mstats import gmean

from matplotlib import pyplot as plt

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

class StartingVerbExtractor(BaseEstimator, TransformerMixin):
    '''
    starting verb extractor

    class to, given a text, will return the "root" of verbs rather than their
    conjugated form.
    '''

    def starting_verb(self, text):
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            pos_tags = nltk.pos_tag(tokenize(sentence))
            first_word, first_tag = pos_tags[0]
            if first_tag in ['VB', 'VBP'] or first_word == 'RT':
                return True
        return False

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.starting_verb)
        return pd.DataFrame(X_tagged)

def load_data(database_filepath):
    '''
        input: database file name and relative path
        output: dataset read split in 
            - X: features
            - y: target
            - feature_columns: list of column names of features
        Description:
            Reads the DisasterResponse.db file and splits it into features and target for further processing.
        NOTES: Depending on which is your working directory you may need to adjust the relative path to the file.
    ''' 
    X = []
    y = []
    feature_columns = []

    try: 
        engine = sqla.create_engine('sqlite:///' + database_filepath)
        df = pd.read_sql_query("SELECT * FROM clasified_messages", engine)
        # features
        feature_columns = df.columns[~df.columns.isin(['id','original','message','genre'])]
        X = df['message'].values
        # target
        y = df[feature_columns].values
    except:
        print('error importing database file. Please check location:  ' + database_filepath)

    return X, y, feature_columns

def tokenize(text):
    '''
        input: A string of text
        output: a cleaned list of words
        
        description: Given a "text", it will:
            - lower case all words
            - replace url's (if there are any) for a place holder word
            - split into words
            - lemmatize each word (remove variations of endings on words)
            - remove spaces
    '''
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    tokens = nltk.word_tokenize(text)
    lemmatizer = nltk.WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

def model_pipeline (parameters = None):
    pipeline = Pipeline([
        ('features', FeatureUnion([

            ('text_pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
            ])),

            ('starting_verb', StartingVerbExtractor())
        ])),

        ('reg', MultiOutputClassifier(RandomForestClassifier(n_estimators=10)))
    ])
    if parameters == None:
        parameters = {}

    cv = GridSearchCV(pipeline, param_grid=parameters, n_jobs=4, cv=5)
    
    return cv

def evaluate_model(model, X_test, y_test, category_names):
    
    preds = model.predict(X_test)
    for cat in range(0, len(category_names)):
        print('Message category:', category_names[cat])
        print(classification_report(y_test[:, cat], preds[:, cat]))

def save_model(model, model_filepath):
    '''
        input: fitted model
        output: filepath and filename where to save the model
        Description:
            Save a model to a pickl file
    '''

    joblib.dump(model, open(model_filepath, 'wb'))

def main():
    if len(sys.argv) == 3:

        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = model_pipeline()
        
        print('Training model, this may take a while...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')

if __name__ == '__main__':
    main()


    