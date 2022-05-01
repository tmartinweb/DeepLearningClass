from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)

tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

# print(tfidf_Vect.vocabulary_)

clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)
predicted = clf.predict(X_test_tfidf)
report = metrics.classification_report(twenty_test.target, predicted, target_names=twenty_test.target_names)
print('First NB Report:\n' + report)


# Support Vector Machine
svc = SVC(kernel='linear')
svc.fit(X_train_tfidf, twenty_train.target)
svc_pred = svc.predict(X_test_tfidf)
svc_report = metrics.classification_report(twenty_test.target, svc_pred, target_names=twenty_train.target_names)
print('SVC Report:\n' + svc_report)

## find best number of clusters based on elbow method
# wcss = []
# for i in range(1,11):
#     kmeans = KMeans(n_clusters=i, max_iter=300, random_state=32)
#     kmeans.fit(X_train_tfidf)
#     wcss.append(kmeans.inertia_)
# import matplotlib.pyplot as plt
# plt.plot(range(1,11),wcss)
# plt.title('The Elbow Method')
# plt.xlabel('Number of Clusters')
# plt.ylabel('Wcss')
# plt.show()
# K-Nearest Neighbor
knn = KNeighborsClassifier()

knn.fit(X_train_tfidf, twenty_train.target)
knn_pred = knn.predict(X_test_tfidf)
knn_report = metrics.classification_report(twenty_test.target, knn_pred,
                                           target_names=twenty_test.target_names)
print('KNN Report:\n' + knn_report)

# Naive Bayes + bigram
mnb_bigram = MultinomialNB()

tfidf_Vect_bigram = TfidfVectorizer(ngram_range=(1, 2))
X_train_tfidf_bigram = tfidf_Vect_bigram.fit_transform(twenty_train.data)
X_test_tfidf_bigram = tfidf_Vect_bigram.transform(twenty_test.data)

mnb_bigram.fit(X_train_tfidf_bigram, twenty_train.target)
mnb_bigram_pred = mnb_bigram.predict(X_test_tfidf_bigram)
mnb_bigram_report = metrics.classification_report(twenty_test.target, mnb_bigram_pred,
                                                  target_names=twenty_test.target_names)
print('NB Bigram Report:\n' + mnb_bigram_report)

# Naive Bayes + bigram + stop_words
mnb_bigram_stop = MultinomialNB()

tfidf_Vect_bigram_stop = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
X_train_tfidf_bigram_stop = tfidf_Vect_bigram_stop.fit_transform(twenty_train.data)
X_test_tfidf_bigram_stop = tfidf_Vect_bigram_stop.transform(twenty_test.data)

mnb_bigram_stop.fit(X_train_tfidf_bigram_stop, twenty_train.target)
mnb_bigram_stop_pred = mnb_bigram_stop.predict(X_test_tfidf_bigram_stop)
mnb_bigram_stop_report = metrics.classification_report(twenty_test.target, mnb_bigram_stop_pred,
                                                       target_names=twenty_test.target_names)
print('NB Bigram and Stopwords Report:\n' + mnb_bigram_stop_report)
