#!/usr/bin/env python

"""
FILE DESCRIPTION

"""

from constants import LOCAL_ROOT

from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def aggregate():
    fgs = pd.DataFrame()

    for year in range(2015, 2020):
        file = LOCAL_ROOT + 'Dataset/{} PFF All Plays.csv'.format(year)
        df = pd.read_csv(
            file,
            low_memory=False    # Silence dType Error
        )

        fg = df.loc[
            df['pff_SPECIALTEAMSTYPE'].astype(str) == 'FIELD GOAL'
        ]
        print('{}: {} FGs'.format(year, len(fg)))

        fgs = pd.concat([fgs, fg])

    fgs = classify_fg(fgs)
    fgs = fgs.dropna(
        axis=1,
        how='all'
    )
    fgs.to_csv('all_FGs.csv')


def classify_fg(fgs):
    fgs[['kickResult', 'kickLocation']] = fgs['pff_KICKRESULT'].str.split(' - ', expand=True)
    fgs['kickResult'] = np.where(fgs['kickResult'] == 'MISSED', 0, 1)

    return fgs


def select(fgs):
    fgs = fgs[[
        'pff_HASH', 'pff_KICKYARDS', 'kickResult'
    ]]
    fgs = fgs.dropna(
        subset=['pff_HASH']
    )
    return fgs


def metrics(model, x, y, threshold=0.5):
    y_prob = model.predict_proba(x)[:, 1]
    predictions = np.where(y_prob > threshold, 1, 0)
    print("\nConfusion Matrix (t={})".format(threshold))
    print(confusion_matrix(y, predictions))
    f1_ = f1_score(y, predictions)
    print("F1:", f1_)

    return f1_


def log_reg(fgs, threshold=0.5):
    fgs = select(fgs).dropna(axis=0)

    y = fgs['kickResult']
    X = fgs.drop(['kickResult'], axis=1)

    hash_, yards = X['pff_HASH'], X['pff_KICKYARDS']

    hash_ = np.array(hash_).reshape(-1, 1)
    one_hot = OneHotEncoder(sparse=True).fit_transform(hash_).toarray()
    hash_ = pd.DataFrame(one_hot, columns=['hash_C', 'hash_L', 'hash_R'])
    X_prep = hash_.join(yards.astype(int))

    data = X_prep.join(y)
    data = data.dropna()
    X_prep = data.drop(columns=['kickResult'])
    y = data['kickResult']

    X_train, X_test, y_train, y_test = train_test_split(
        X_prep, y, test_size=0.2
    )

    lr_model = LogisticRegression(
        random_state=42,
        solver='lbfgs'
    )
    lr_model = lr_model.fit(X_train, y_train)
    f1_score = metrics(lr_model, X_test, y_test, threshold)

    return lr_model, f1_score


df = pd.read_csv('data/all_FGs.csv')

thresholds = np.arange(0.5, 1.05, 0.05)
f1_scores = []
for t in thresholds:
    model, f1 = log_reg(df, round(t, 2))
    f1_scores.append(f1)
plt.plot(thresholds, f1_scores)
plt.show()
