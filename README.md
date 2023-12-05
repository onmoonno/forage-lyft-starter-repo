# Lyft Back-End Engineer: Project Overview 
* Completed the job simulation, and took over a project for the Lyft Rentals team, Come up with a clean design for an existing, unfinished component.
* Drafted a UML class diagram representing a new reorganized architecture.
* Refactored the codebase with Factory and Strategy design pattern for multiple product creation and manipulation.
* Implemented unit tests and added new functionality using test-driven development.

## Code and Resources Used 

**Python Version:** 3.11  

**Packages:** datetime, unittest, ABC

**Scraper Github:** https://vagabond-systems/forage-lyft-starter-repo 

**Scraper Website:** https://www.theforage.com/virtual-experience

## System Design
Class diagram of the newly designed system with Factory and Strategy design parttern.

![alt text](https://github.com/onmoonno/forage-lyft-starter-repo/blob/main/Class%20Diagram.png)

## Model Building 

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : MAE = 11.22
*	**Linear Regression**: MAE = 18.86
*	**Ridge Regression**: MAE = 19.67

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 
