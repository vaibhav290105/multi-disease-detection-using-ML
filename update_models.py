import pandas as pd
import pickle

idx = int(input("""Select the Machine Learning Algorithm
[1] Logistic Regression
[2] Random Forest classifier
[3] Support vecter machine
[4] K Nearest neighbor 
[5] Decision tree classifier
[6] Gaussian naive bayes
[7] K means\n > """))

if idx == 1:
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
elif idx == 2:
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_jobs=-1)
elif idx == 3:
    from sklearn import svm   
    model = svm.LinearSVC()
elif idx == 4:
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier(n_neighbors=6)
elif idx == 5:
    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier(criterion = "gini",random_state = 100,max_depth=3, min_samples_leaf=5)
elif idx == 6:
    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
elif idx == 7:
    from sklearn.cluster import KMeans
    model = KMeans(n_clusters=2, random_state=0)


def heart_disease_prediction():
    dataset = pd.read_csv('Dataset/heart.csv')
    dataset.corr()
    X = dataset.drop(['target'], axis=1)
    y = dataset['target']
    classifier = model
    classifier.fit(X, y)
    pickle.dump(classifier, open('Models/heart_model.sav', 'wb'))


def kidney_disease_prediction():
    dataset = pd.read_csv('Dataset/kidney_disease.csv')
    dataset.classification = dataset.classification.replace("ckd\t", "ckd")
    dataset.drop('id', axis=1, inplace=True)
    dataset['classification'] = dataset['classification'].replace(
        ['ckd', 'notckd'], [1, 0])
    dataset = dataset.dropna(axis=0)
    dataset['wc'] = dataset['wc'].replace(["\t6200", "\t8400"], [6200, 8400])
    dataset['pcv'] = dataset['pcv'].astype(int)
    dataset['wc'] = dataset['wc'].astype(int)
    dataset['rc'] = dataset['rc'].astype(float)
    dictonary = {
        "rbc": {
            "abnormal": 1,
            "normal": 0,
        },
        "pc": {
            "abnormal": 1,
            "normal": 0,
        },
        "pcc": {
            "present": 1,
            "notpresent": 0,
        },
        "ba": {
            "notpresent": 0,
            "present": 1,
        },
        "htn": {
            "yes": 1,
            "no": 0,
        },
        "dm": {
            "yes": 1,
            "no": 0,
        },
        "cad": {
            "yes": 1,
            "no": 0,
        },
        "appet": {
            "good": 1,
            "poor": 0,
        },
        "pe": {
            "yes": 1,
            "no": 0,
        },
        "ane": {
            "yes": 1,
            "no": 0,
        }
    }
    dataset = dataset.replace(dictonary)
    dataset.corr()
    X = dataset.drop(
        ['classification', 'sg', 'appet', 'rc', 'pcv', 'hemo', 'sod'], axis=1)
    y = dataset['classification']
    classifier = model
    classifier.fit(X, y)
    pickle.dump(classifier, open('Models/kidney_model.sav', 'wb'))


def diabetes_prediction():
    dataset = pd.read_csv('Dataset/diabetes.csv')
    X = dataset.drop(columns='Outcome', axis=1)
    Y = dataset['Outcome']
    classifier = model
    classifier.fit(X, Y)
    pickle.dump(classifier, open("Models/diabetes_model.sav", 'wb'))


def parkinsons_prediction():
    dataset = pd.read_csv('Dataset/parkinsons.csv')
    X = dataset.drop(columns=['name', 'status'], axis=1)
    Y = dataset['status']
    classifier = model
    classifier.fit(X, Y)
    pickle.dump(classifier, open("Models/parkinsons_model.sav", 'wb'))


heart_disease_prediction()
kidney_disease_prediction()
diabetes_prediction()
parkinsons_prediction()