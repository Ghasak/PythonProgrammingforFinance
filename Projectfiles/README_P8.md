# Company correlation table
## - Python Programming for Finance p.8

Hello and welcome to part 8 of the Python for Finance tutorial series. In the previous tutorial, we showed how to combine all of the daily pricing data for the S&P 500 companies. In this tutorial, we're going to see if we can find any interesting correlation data. To do this, we'd like to visualize it, since it's a lot of data. We're going to use Matplotlib for this, along with Numpy.

# Output
To Run this in terminal use

```
python Projectfiles/P8_ProforFinanace.py
```
![](./output_graphs/PX-1.png)
Also you through VSCODE:
![](./output_graphs/PX-2.png)
# My Note
We have here worked on the **visualization**, now we can work on correlation and looking on mean. The values of the

# Problem
In the original code there was a problem at the following function and it has been altered.

```
heatmap = ax.pcolor(data, cmap = "RdYlGn") # Before it was: plt.cm.RdYlGn
```
# Inspiration

https://pythonprogramming.net/stock-price-correlation-table-python-programming-for-finance/
