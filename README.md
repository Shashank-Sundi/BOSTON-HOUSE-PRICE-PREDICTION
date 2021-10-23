# BOSTON-HOUSE-PRICE-PREDICTION


[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://boston-house-price-pred-sundi.herokuapp.com/)&nbsp;
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)&nbsp;
<img src="https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg">&nbsp;
![GitHub repo size](https://img.shields.io/github/repo-size/Shashank-Sundi/BOSTON-HOUSE-PRICE-PREDICTION)&nbsp;
![Lines of code](https://img.shields.io/tokei/lines/github/Shashank-Sundi/BOSTON-HOUSE-PRICE-PREDICTION?style=flat)

Machine Learning Project to predict the expected price of  house in Boston area , based on the specified user inputs .

<img src="static\images\todd-kent-178j8tJrNlc-unsplash.jpg" alt="house" />
<hr>


## Deployment

The model has been deployed using REST API using flask, on Heroku : https://boston-house-price-pred-sundi.herokuapp.com/

<hr>

## Original Dataset and Python Notebook

Original Dataset : https://www.kaggle.com/c/boston-housing

Python Notebook : https://shashank-sundi.github.io/BOSTON-HOUSE-PRICE-PREDICTION/

Python Notebook : https://github.com/Shashank-Sundi/NOTEBOOKS/blob/main/Boston-Housing-Price-Prediction.ipynb

<hr>

## Project Description

| PROBLEM | MODELS USED  |LIBRARIES USED   |IDE's USED|
| :-------- | :------- | :------------------------- | :-------|
| **Predicting Prices of Boston Houses**| `XGBOOST,ADABOOST ,LOG-REG ,KNN ,RANDOM FOREST ,DECISION TREE ,SVC ,NAIVE BAYES, STACKING CLASSIFIER ` | `Sklearn , Seaborn ,Pandas ,Numpy ,Scipy ,Xgboost `|`PyCharm,` `VS Code,` `Jupyter Notebook`|

<hr>

## Project Execution

### (A) **Analysis in Jupyter Notebook**


| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1|Extracted dataset from above link  |
|2| Validated data types of the features and analysed the statistical properties of the features
|3|Performed EDA on data - checked the distribution of data using NPP, KDE plots ; checked for outliers via boxplots
|4|Found outliers and imputing them with the mean value for the corresponding features
|5| Standardizing the data 
|6| Metric used to evaluate models - r2 score
|7| Trained and tested various models on the data and chose the model which gave highest accuracy score 
|8| Random Forest gave the second highest highest r2 score ( 89.06 % )
|9| Exported the RF model via pickle


### (B) **Building the Application**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1| Built REST API using Flask framework ; created routes for home page and pred
|2| Built html pages for data input and results prediction
|3| Created the requirements.txt , Procfile , etc. and all other requirements to be satisfied for deployment.
|4| Deployed the model on Heroku via Git Bash terminal

<hr>

## Screenshots

### **Enter the required inputs in home page and press predict button**

<img src="static\images\boston homepage.PNG" alt="FIFA" />

### **The Prediction Page**

<img src="static\images\boston resultpage.PNG" alt="FIFA"/>

<hr>
  
## Contact

<a href="https://www.linkedin.com/in/shashank-sundi-4b78561b1"> ![alt text](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)</a>&emsp;
<a href="https://www.instagram.com/shashank_sundi13/">![alt text](https://img.shields.io/badge/Shashank_Sundi-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)</a>&emsp;
<a href="mailto:sundi.sn@gmail.com">![alt text](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>

<hr>
