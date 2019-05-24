# Creating machine learning target function
## - Python Programming for Finance p. 10

Hello and welcome to part 10 (and 11) of the Python for Finance tutorial series. In the previous tutorial, we began to build our labels for our attempt at using machine learning for investing with Python. In this tutorial, we're going to use what we did last tutorial to actually generate our labels when we're ready.

Full code up to this point:
# Output
To Run this in terminal use

```
python Projectfiles/P9_ProforFinanace.py
```
We will zoom into some companies to get:

![](./output_graphs/PX-1.png)


# My Note
You can learn more about **Args & Kwargs** here:
https://pythonprogramming.net/args-kwargs-intermediate-python-tutorial/

The function that we create here is saying: based on the value of 0.02 we can decide to buy or sell for example as you can see col larger than requirement or (1) means buy, otherwise (-1) means sell and (0) means hold this stock.

```
def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement  = 0.02
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1

    return 0
```

# Problem




# Inspiration

https://pythonprogramming.net/args-kwargs-intermediate-python-tutorial/
