# LT2212 V20 Assignment 2

## Part 1

I split the news samples by spaces and lowercase all the words. Then I use `isalpha()` function to filter the words containing numbers or punctuations. In order to make the dataset smaller, I filter the words occur less than 5 times in the whole corpus. I get 18846 news samples and 32307 words ultimately.



## Part 2

I use PCA class in [scikit-learn](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.decomposition) doing dimensionality reduction.



## Part 3

`model_id #1`: GaussianNB

`model_id #2` : DecisionTreeClassifier



| Scores 	| GaussianNB 	| DecisionTreeClassifier 	|
|-----------	|:----------:	|:----------------------:	|
| Accuracy 	| 0.15889 	| 0.18594 	|
| Precision 	| 0.26179 	| 0.18656 	|
| Recall 	| 0.15889 	| 0.18594 	|
| F-measure 	| 0.14363 	| 0.18549 	|



## Part 4



