#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:20:33 2018

@author: Allan Krueger (klimber.mail@gmail.com)
"""

from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
import numpy as np


categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']

#twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
twenty_train = load_files("20news-bydate-train/", categories=categories, encoding="ANSI")
twenty_test = load_files("20news-bydate-test/", categories=categories, encoding="ANSI")
#twenty_train.target_names
#len(twenty_train.data)
#len(twenty_train.filenames)

tfidf_transformer = TfidfTransformer()

text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None))])
text_clf.fit(twenty_train.data, twenty_train.target)

docs_test = twenty_test.data

predicted = text_clf.predict(docs_test)
np.mean(predicted == twenty_test.target)