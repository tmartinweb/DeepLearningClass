#####################################################################################################################
# Import Statements #
#######################
import os
import pandas as pd
import sklearn
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

#####################################################################################################################
# Set console output options for pandas -> Mostly for debugging #
#################################################################
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def run():  # Method to be called from Main()
    ####################################################################################################################
    # Read input file #
    ###################
    file_name = 'glass.csv'
    df_train = pd.read_csv(file_name)

    ####################################################################################################################
    # Preprocessing based on Dataframe #
    ####################################

    # Change 'Types' based on 0 index and lack of a Type == 4
    df_train['Type'] = sklearn.preprocessing.LabelEncoder().fit_transform(df_train['Type'])

    # Create a set of the headings of features (not including target feature)
    column_set = {'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe'}

    ####################################################################################################################
    # Dataframe Manipulation: df_train ~~> df_train, df_test, df_validation #
    #########################################################################

    # Split data into training dataframe and test/validation dataframe
    df_train, df_test = train_test_split(df_train, test_size=.3, random_state=16)
    # Split test/validation dataframe into separate test and validation dataframes
    df_test, df_validate = train_test_split(df_test, test_size=.3, random_state=16)

    # Pop the feature we are to test against for each dataframe
    train_target = df_train.pop('Type')
    validate_target = df_validate.pop('Type')
    test_target = df_test.pop('Type')

    # Copy the split data into each model's own frames
    svm_train, svm_test = df_train.copy(), df_test.copy()
    nbt_train, nbt_test = df_train.copy(), df_test.copy()
    knn_train, knn_test = df_train.copy(), df_test.copy()

    ####################################################################################################################
    # Preprocessing based on Algorithms #
    #####################################

    # Support Vector Machine Preprocessing
    # Most resources indicate that Standardization [-1, 1] is the best method
    scale = StandardScaler().fit(svm_train)
    svm_train = pd.DataFrame(scale.transform(svm_train))
    svm_test = pd.DataFrame(scale.transform(svm_test))

    # Naive Bayes Preprocessing
    # Most resources indicate that BernoulliNB() is made for binary/boolean data
    # Utilized quantile-based partitioning (each set will have -near- equal number of members)
    for column in column_set:
        nbt_train[column] = pd.qcut(nbt_train[column], 2, labels=False, duplicates='drop')
        nbt_test[column] = pd.qcut(nbt_test[column], 2, labels=False, duplicates='drop')

    # K-Nearest Neighbors Preprocessing
    # Most resources indicate Normalization [0, 1] is the best method
    norm = MinMaxScaler().fit(knn_train)
    knn_train = pd.DataFrame(norm.transform(knn_train))
    knn_test = pd.DataFrame(norm.transform(knn_test))
    for column in range(0, len(knn_train.columns)):
        knn_train[column] = pd.qcut(knn_train[column], 10, labels=False, duplicates='drop')
        knn_test[column] = pd.qcut(knn_test[column], 10, labels=False, duplicates='drop')

    ###################################################################################################################
    # Driver Code #
    ###############

    # Create instances of models
    tf_model_svm = SVC(C=5.0)  # Also played with LinearSVC
    tf_model_nbt = BernoulliNB()  # Also played with MultinomialNB
    tf_model_knn = KNeighborsClassifier()  # JUST FOR FUN

    # Train models, passing in our training and target dataframes
    tf_model_svm.fit(svm_train, train_target)
    tf_model_nbt.fit(nbt_train, train_target)
    tf_model_knn.fit(knn_train, train_target)

    # Run test dataframe through prediction and classification methods for evaluation of fitness
    print("\n~~~~    Test Evaluation Output    ~~~~")

    # Predict model fitness
    svm_pred = tf_model_svm.predict(svm_test)
    nbt_pred = tf_model_nbt.predict(nbt_test)
    knn_pred = tf_model_knn.predict(knn_test)

    # Print output
    print("SVM - Report:\n", metrics.classification_report(test_target, svm_pred, zero_division=0))
    print("NBT - Report:\n", metrics.classification_report(test_target, nbt_pred, zero_division=0))
    print("KNN - Report:\n", metrics.classification_report(test_target, knn_pred, zero_division=0))

#####################################################################################################################
# main() function entry #
#########################


def main():  # Standard base code
    run()


if __name__ == '__main__':
    main()


#####################################################################################################################
# End of File #
#####################################################################################################################

