# Machine learning
## - Python Programming for Finance p. 12

Hello and welcome to part 12 of the Python for Finance tutorial series. In the previous tutorial we covered how to take our data and create features and labels out of it, which we can then feed through a machine learning algorithm with the hope that it will learn to map relationships of existing price changes to future price changes for a company.



Full code up to this point:
# Output
To Run this in terminal use

```
python Projectfiles/P11_ProforFinanace.py
```
We will zoom into some companies to get:

![](./output_graphs/PX-1.png)


# My Note
if you want to get the version of a specific library in your virtualenv you can write the following

```
print('sklearn: %s' % sklearn.__version__)
```



# Problem
Use this import by replacing ** cross_validation** with **model_selection**
```
from sklearn import svm,  model_selection, neighbors  # before model_selection was cross_validation
```

There are another problem that I encountered with which is about the default **n_estimators** in the random forest classifier and here is the solution

intead writing

```
model = RandomForestClassifier()
```
Write
```
model = RandomForestClassifier(n_estimators = 100)
```
This will not produce any error rather than a warning can be trace to the **sklearn** library, for more details see:
https://machinelearningmastery.com/how-to-fix-futurewarning-messages-in-scikit-learn/





# Inspiration

https://pythonprogramming.net/machine-learning-stock-prices-python-programming-for-finance/
