# EECE5644 Final Project: Speed Dating
## Project Description
The main goal of this project is to find the weight of importance of each attribute. Which
characteristics (of those measured in the dataset) are the most important in determining a potential
match between two people? By doing this, we can make predictions of whether or not two people
(based on information they provide) will be a match, or make predictions about what type of people a
person will match with. We can also assess the likelihood of a person finding a match based on the
information they provide.

1. Weight of importance of each attribute? What are the most important attributes when it comes
to the matching rate? PCA/LDA, L1 Regularization and various feature extraction methods
2. Can we divide the data into meaningful clusters? Various Clustering Methods

   1. How do the importance of attributes change between local clusters? E.g., for prospective
   lawyers, how important is it that the other person is smart? And for prospective
   engineers?

3. Is there a big difference between how people perceive themselves and how others perceive
them? Various Clustering Methods 
   1. If the previous question can be answered. Does the difference between self-perception
   and outward perception affect the rate at which a person matches with others?
4. Is it likely that a person who is perceived as intelligent and who also perceives themselves as
intelligent achieves a high matching rate?
5. Could we make predictions on the matching rate of a person in a specific cluster? Random
Forest, Naive Bayes Classifier, Logistic Regression, SVM

We can use this data to create a model as a basis for an application or service to match potential
dates together. A Bayes classifier could be used to predict whether someone would be a potential match
for others based on their profile information (location, income, major, hobbies, etc). Regression could be
used to predict what type of person someone would match with based on their profile information. We
can use methods such as k-means to verify our classifier / regression model, and we could use pca/lda or
regularization (l1 or l2) to potentially reduce computational complexity / runtime of our model. We will
have to normalize our input data as many of them exist on different scales.

## Results
Please in order to reproduce the results provided in the project final report, check the code from the `imblearn_experiment.ipynb` (containing Experiment 2 with the imblearn package) and `main.ipynb` (containing all experiments except Experiment 2) files.

## Authors
* Robert Ashby
* Helena Calatrava
* Hwijong Im
* Kuo Yang
