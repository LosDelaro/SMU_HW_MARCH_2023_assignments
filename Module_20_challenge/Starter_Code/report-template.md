# Module 12 Report Template

## Overview of the Analysis

In this section, describe the analysis you completed for the machine learning models used in this Challenge. This might include:

* Explain the purpose of the analysis.
This models purpose is to build a model that can identify the creditworthiness of borrowers.

* Explain what financial information the data was on, and what you needed to predict.
The data was on the columns of the data set of interest_rate ,borrower_income,debt_to_income,num_of_accounts,derogatory_marks,total_debt,loan_status. The prediction was needed on creditworthiness.

* Provide basic information about the variables you were trying to predict (e.g., `value_counts`).
The basic information on variables used to predict the creditworthiness are :
        
*interest_rate      
*borrower_income     
*total_debt          
*loan_size           
*num_of_accounts     
*debt_to_income      
*derogatory_marks   

* Describe the stages of the machine learning process you went through as part of this analysis.
The list of stages required for this process are
1. import pandas libraries :pandas,numpy, ML helpers from scikitlear such as train_test_split, confusion _matrix,classification _report, roc_auc_score, roc_curve. Scaling from scikitlear StandardScaler and MinMax. and several others for algorithms and trees.
2. Read in the data set
3.Data set review for any cleaning or inputing of columns. 
4. Review for multicolinarity 
5.Check for any inbalances on feature target
6. Split the data into training and testing datasets 
7. Create a logistic regression model with unscaled data.
8. Conclude that a logistic regression model predicts both a healthy and high risk loan at almost 100% accuracy. 
9. Further exploration was done using scaled data did improve the AUC score for the linear regression model. 
10. Additonal exploration done with algorithims on unscaled data with Kneighbors , RandomForest, Ada boost, GRadientBoosting, Xgb,
lgbm. This led to the conclusing the adaboost algorithm had a better auc score than the liner regression  

* Briefly touch on any methods you used (e.g., `LogisticRegression`, or any resampling method).
No Resampling method done on this module. However additional exploration done with MinMax scaler and other algorithms

## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:LogisticRegression()
  * Description of Model 1 Accuracy
  *The accuracy score for the training set for the linear regression  is .99 which is the same for the testing set, which indicates  the model is performing well along all classes with understanding of some imbalance. This helps to understand the models overall performance. 
  *Precision score for the the lr reflects a low rate of false positives. This is help full with this scenario to identify any unwanted biases.
  *Recall scores for the lr reflect .89 the model is good at capturing most of the positive instances
  *AUC score for the lr model had a auc score of 0.9964386161309239 



* Machine Learning Model 2:AdaBoostClassifier
  * Description of Model 2 Accuracy- The adaboost model had a accuracy of 1.00 which indicates the model is performing at 100% along all classes and no imbalances. 
  
  *Precision - AdaBoost showed only 5 false positives while the LR model had 67 . Which would imply some of the biases has been removed. 
  
  *Recall scores - Recall score was .99 which was much higher than the LR model that resulted in .89 recall . 

## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best? The model of best fit would be linear regression althought performance metics may indicate it is not the best compared to ada boost however in the end it would be the most explainable to stakeholders.

* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? ) Performance does depend on the probelm . If trying to predict high risk, the data represents a financial industry that requires it to remain in good financial health because of the nature of their business. Having too many loans having a high risk of defaulting puts the business and being involvent because of too many losses. 

If you do not recommend any of the models, please justify your reasoning. The Linear regression model is the model to recommend. It provides the best method to explain to stake holders why this model should be pursued. It has the major advantage of explainability and mathmatical representation for explanation. 
