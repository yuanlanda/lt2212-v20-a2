# LT2212 V20 Assignment 2

## Part 1

I split the news samples by spaces and lowercase all the words. Then I use `isalpha()` function to filter the words containing numbers or punctuations. In order to make the dataset smaller, I filter the words occur less than 5 times in the whole corpus. I get 18846 news samples and 29543 words ultimately.



## Part 2

I use TruncatedSVD class doing dimensionality reduction.



## Part 3

`model_id #1`: GaussianNB

`model_id #2` : DecisionTreeClassifier



## Part 4

100%(29543), 50%(14772), 25%(7386), 10%(2954), 5%(1477)

| Algorithms             | D-Reduction                                  |                Accuracy                 |                Precision                 | Recall                                    | F-measure                               |
| ---------------------- | -------------------------------------------- | :-------------------------------------: | :--------------------------------------: | ----------------------------------------- | --------------------------------------- |
| GaussianNB             | 1.0,          0.5,     0.25,   0.10,    0.05 | 0.6334, 0.1069, 0.1308, 0.1257, 0.1263  |  0.6525, 0.1568, 0.2024, 0.2460, 0.2755  | 0.6334, 0.1069, 0.1308, 0.1257, 0.1263    | 0.6367, 0.0845, 0.1065, 0.1051, 0.1126  |
| DecisionTreeClassifier | 1.0,          0.5,     0.25,   0.10,    0.05 | 0.4966, 0.1271, 0.1456, 0.1568,  0.1642 | 0.5022, 0.1290, 0.1490,  0.1583,  0.1675 | 0.4965, 0.1271, 0.1456,   0.1568,  0.1642 | 0.4967,  0.1274, 0.1468, 0.1572, 0.1653 |

My most time-consuming bug is that in part 1, when I filter the words which occur less than 5 times in my corpus, I forget to resize the index(value) of each unique word(key) in my dictionary, so I get a wrong values dictionary. Then in Part 3, I found both classifier training algorithms GaussianNB and DecisionTreeClassifier have a really bad performance, all the scores are less than ideal.

In general, `GaussianNB` has a better performance compared to `DecisionTreeClassifier`.  After 50% features deducting, all the scores in both classifiers are dramatically decreased. However, all the reductions in different reducing levels share a similar scores. 







