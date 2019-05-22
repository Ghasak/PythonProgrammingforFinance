# Getting all company pricing data in the S&P 500
## - Python Programming for Finance p.6
Hello and welcome to part 6 of the Python for Finance tutorial series. In the previous finance with Python tutorial, we covered how to acquire the list of companies that we're interested in (S&P 500 in our case), and now we're going to pull stock pricing data on all of them.

# My Note
Since we already have grabbed the data as **.pickle** from last script.p5, now we will comment the **save_sp500_tickers()** function to move to the next step.
Starting with reading the data that we saved before in the format **.pickle** and we will use basically the new function with the following format

```
def get_data_from_yahoo(reload_sp500 = False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open(ResourceDir+"/resources/sp500tickers.pickle","rb") as f: # rb for read the file
        tickers = pickle.load(f)
```
Here will create a relative directory using the os functionality **stock_dfs**. The purpose is to get the stocks for each company of our current 500 companies file.

# Problem 1
I was able to solve a problem in the code using the regular expression method **rstrip()** which remove the value of **\n** - new line. The function now is working

![](./output_graphs/PX-1.png)

# Problem 2

There are some company I couldnt get their stock files using the **yahoo** data grabber. then I have added this code to git rid of them.
```
non_valid_company = ["BDX","BBT","CF","COST","DOW","EVRG","HIG"]
with if statement checking as
if ticker in non_valid_company:
            continue

```
* Note: I have used continue rather than pass, because I don't want the checking to do nothing and go to next step, while continue will go to for and proceed to the next iteration.
# Inspiration

https://pythonprogramming.net/sp500-company-price-data-python-programming-for-finance/
