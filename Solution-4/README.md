# Assignment-4
Assignment-4

#### Complete the following:

#### Name: Thomas Martin
#### Email: trm7f7@umsystem.edu

<br/>
 
Write brief explanation here:

#### Part 1:
	The SVM took a long time to run, but produced the best results.
	Using KMeans returned unusable results, instead using KNeighborsClassifier produced results.
	I used MultinomialNB() for implementing the bigram and stop_words part of the assignment. Using a bigram vectorizer did not affect the results much, and using stop_words increased the accuracy by 4%.
	The text manipulation was not too difficult, but I am curious how some of the modifications (stemming and lemmatization) actually affect results.

#### Part 2:
	I experiemented with many layering methods and found that I got the most consistent results (across both datasets) with the current configuration (5 hidden layers; all weights initialized with Ones, and all biases initialized with RandomUniform; relu on the first and last hidden, elu on the middle three). 
	I had problems with the Diabetes data and reducing the loss ( not < .46). Standardization actually seemed to make the Diabetes results more erractic, although seemed to converge around 76% consistently with or without standardizing. 
	The Breast Cancer data converged around the same accuracy with our without standardization (96%), but did reach that mark faster with standardization (epoch 20).
