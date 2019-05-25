# Testing trading strategies with Quantopian Introduction 
## - Python Programming for Finance p.13

Hello and welcome to part 13 of the Python for Finance tutorial series. In this tutorial, we're going to begin talking about strategy back-testing. The field of back testing, and the requirements to do it right are pretty massive. Basically, what's required for us is to create a system that will take historical pricing data and simulate trading in that environment, and then gives us the results. That might sound simple, but, in order to analyze the strategy, we need to be tracking a bunch of metrics like what we sold, when, how often we trade, what our Beta and Alpha is, along with other metrics like drawdown, Sharpe Ratio, Volatility, leverage, and a bunch more. Along with that, we generally want to be able to visualize all of this. So, we can either write all of this ourselves, or we can use a platform to help us with that...



Full code up to this point:
# Output
To Run this in terminal use

```
python Projectfiles/P13_ProforFinanace.py
```
We will zoom into some companies to get:

![](./output_graphs/PX-1.png)


# My Note
We will learn about the Quantopian. Give you a fundamental data for each company up to - **One Minute**. Starting by Going to the website of 
https://www.quantopian.com/posts **Quantopian** which will offer a data and code for free for any resorce.

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
