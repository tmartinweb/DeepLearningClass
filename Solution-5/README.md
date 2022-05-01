# Assignment-5
Assignment-5
<br/>
** Part-2 Dataset available in your Canvas assignment file **
<br/>
#### Complete the following:

#### Name: Thomas Martin
#### Email: trm7f7@umsystem.edu

<br/>

Write brief explanation here:

  #### Part 1:
              The current configuration seemed to provide the most consistent results.
              Input layer, 3 Dense layers, and an output layer, with BatchNormalizing and Dropout layers interspersed, and with 'tanh' giving the best results
              In fact, sigmoid gave the worst results.
              I also slowed the learning rate and added 5 more epochs, again seemed to get the most consistent results.
              Seemed to be a 1-3% accuracy gain by standardizing the data, maybe because of the BatchNormaliztion layers??
              Functional Model is a bit easier to read.
  
  #### Part 2:
              What fun, what fun!
              The three mistakes were not defining input_dim (which should be the length of the padded text), the output layer should have 1 node (binary classification), and the loss function should be binary_crossentropy.
              I used the GroupShuffleSplit() method to split data by the 'type' feature. And I dropped the rows meant for unsupervised learning.
              Results for the imdb data NOT embedded around 50% accuracy, while with the embedded layer it reached close to 90%.
              I don't think I did the 20 newsgroups correctly, 50% whether embedded or not.
