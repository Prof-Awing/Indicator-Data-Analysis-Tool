# Indicator Data Exploration and Analysis Tool

#### Description
This tool fetches indicator data of countries from [TradingEconomics](https://tradingeconomics.com/indicators) website. It first fetches the data, then allows the user to explore and visualize the data the way he/she prefers. The user can also customize and simplify the visualization, if the complexity of the data requires him/her to. Next, the user might like to run a simple analysis of the change in values-- both *absolute* and *percentage* change. Fun part: requiring that you have included the columns *Catagory AND Country*, one can optionally play a simple quiz, which asks which country has the highest change in value for a randomly chosen indicator (if you have more than one). If you want to export the data as a JSON file, you're welome.

#### So the steps are:

+ Logging in choosing an account.

+ Choosing Country(s)

+ Choosing Indicator(s)

+ Selecting Columns

+ View the DataFrame

+ Customizing or Pivoting the DataFrame. (Conditional: Atleast requires more than one indicator or that the data be more complex.)

+ Change in Value (Conditional: Requires columns 'LatestValue' and 'PreviousValue' to be selected.)

+ Quiz (Conditional: depends on 3,4)

+ Export as JSON (Optional)

### Log-In
At first you will see the prompt below which expects you to select your account type for TradingEconomics:
```
This is a simple  Data Exploration and Analysis tool for INDICATOR DATA by countries.
The data is gathered from TradingEconomics website. Visit at: https://tradingeconomics.com

I want to log-in as a/an:
<1> Default User (Account type: Free)
<2> Existing Free User of TradingEconomics
<3> Existing Premium User of TradingEconomics
(Type in the corresponding integer only)

>>>
```
> [!NOTE]
> You are supposed to input only **one of the three given digits**. Other inputs will be invalid, and you will be reprompted.

You are **recommended** to type **1** if you don't have, or intend to login with, an existing account of yours in TradingEconomics.

If you have a **free** account you want to log-in with, type **2**.

If you want to log-in with a **premium** account, type **3**.

### Input Country
You will then be prompted to type in the Country, with instructions for countries available for you. The prompt looks like this:
```
Please select and type Country(s) from: Mexico, Sweden, New Zealand, Thailand
Countries:
```
 **Free accounts**(1 or 2) only have 4 mentioned countries available, and those will be shown with the prompt. For **premium account**(3), you will see a link redircting to a webpage for available countries to type in *(we will see in Input Indicator section)*.

If you intend to put many countries, values should be **Comma-Separated**.

#### Example:
```
Countries: Mexico
```
or
```
Countries: Thailand, New Zealand, Sweden
```
Wrong or Unavailable inputs will result in reprompt.

### Input Indicator
The input instructions of Indicators are same as that of Countries. The indicators are CASE-SENSITIVE.
The prompt looks like this:
```
Please select and type Indicator(s) from :https://api.tradingeconomics.com/indicators?c=3cfb51495de84f9:ku5xzon6e63jmas
For Example: Imports; or Imports, 1 Year MLF Rate
[Case-sensitive, comma-separated(if multiple)]
Indicator:
```

Follow the link to look for available indicators according to your account: `Ctrl + Left-Click` *on the link given above the prompt.*
#### Example:
```
Indicator: Imports
```
or
```
Indicator: Imports, Exports, Interest Rate
```

### Select Columns
the provided prompt:
```
Select columns to analyze:
for all columns: input 'all'
for specific columns: integer(key) corresponding to the column name, *comma-separated*.

{0: 'Country', 1: 'Category', 2: 'Title', 3: 'LatestValueDate', 4: 'LatestValue', 5: 'Source', 6: 'SourceURL', 7: 'Unit', 8: 'URL', 9: 'CategoryGroup', 10: 'Adjustment', 11: 'Frequency', 12: 'HistoricalDataSymbol', 13: 'CreateDate', 14: 'FirstValueDate', 15: 'PreviousValue', 16: 'PreviousValueDate'}
>>>
```
#### Example:
```
>>> 0, 1, 4, 15
```
or
```
>>> all
```

### View DataFrame
the output will be a Pandas DataFrame:
```
        Country Category  LatestValue  PreviousValue
1     Thailand  Imports      27093.8        24578.5
2     Thailand  Exports      25720.6        24796.6
3       Sweden  Imports     149500.0       162500.0
4       Sweden  Exports     156000.0       170600.0
5  New Zealand  Imports       7110.0         5450.0
6  New Zealand  Exports       6150.0         6040.0
```
or if you have typed `all` :
```
        Country Category                Title      LatestValueDate  ...           CreateDate       FirstValueDate PreviousValue    PreviousValueDate
1     Thailand  Imports     Thailand Imports  2024-07-31T00:00:00  ...  2013-04-23T15:25:00  1991-01-31T00:00:00       24578.5  2024-06-30T00:00:00
2     Thailand  Exports     Thailand Exports  2024-07-31T00:00:00  ...  2013-04-23T15:09:00  1991-01-31T00:00:00       24796.6  2024-06-30T00:00:00
3       Sweden  Imports       Sweden Imports  2024-07-31T00:00:00  ...  2014-05-27T11:47:00  1960-01-31T00:00:00      162500.0  2024-06-30T00:00:00
4       Sweden  Exports       Sweden Exports  2024-07-31T00:00:00  ...  2014-05-27T11:47:00  1960-01-31T00:00:00      170600.0  2024-06-30T00:00:00
5  New Zealand  Imports  New Zealand Imports  2024-07-31T00:00:00  ...  2014-03-27T09:56:00  1960-01-31T00:00:00        5450.0  2024-06-30T00:00:00
6  New Zealand  Exports  New Zealand Exports  2024-07-31T00:00:00  ...  2014-03-27T09:56:00  1951-01-31T00:00:00        6040.0  2024-06-30T00:00:00

[6 rows x 17 columns]
```
So you get it, selecting only the required columns might get you the best output. But yes, do what seems best for you.

### Customizing or Pivoting the df
```
Want to narrow down or customize the table visualization (Recommended if your data is so complex)? y/n:
```
You require to have **more than one** `Indicator` or `Countries` to come to this section. Otherwise, you will be forwarded to the next section automatically.

Two things can be done in this section:

+ In this section, you can compare the values of the indicators and countries.

+ If you have a complex data structure, like the one we get from typing `all`, you can simplify, narrow-down or arrange data by pivoting the dataframe in this section.

Type either `y` for *yes*, or `n` for *no*.

`y` will forward you to:
```
Select COLUMNS,ROWS and VALUES, no greater than Two for each, according to your preference: Comma-separated
VALUES must be the ones that you will compare or visualize.
Read the tutorial before you proceed...

type in corresponding integer:
        ['0: Country', '1: Category', '2: Title', '3: LatestValueDate', '4: LatestValue', '5: Source', '6: SourceURL', '7: Unit', '8: URL', '9: CategoryGroup', '10: Adjustment', '11: Frequency', '12: HistoricalDataSymbol', '13: CreateDate', '14: FirstValueDate', '15: PreviousValue', '16: PreviousValueDate']

COLUMNS:
ROWS:
VALUES:
```
For better convenience, we can refer the options e.g. `0: Country` as **key : value** pairs like we see in dictionaries. We can refer `COLUMNS`, `ROWS`, `VALUES` as **positions**.
> #### *IMPORTANT:*
> + You will select Integers(keys) corresponding to the Columns(values) according to your preference and input in `COlUMNS`, `ROWS`, `VALUES`(positions), where you want them to be in.
> + The **positions** will not contain the **keys** that you will select, rather their values will be presented in the **position**. For example: if you put `Category` (that is **key**, or **1**) for `COLUMN`, the output DataFrame will have columns such as: `Import`, `Export`, or **indicators** in your DataFrame.
> + No greater than **TWO** **keys** each **position**.
> + It is important to think of the relevance and rationality of inputs in each position. But yes, you have a `Change? y/n: ` option to repeat it.
> + `VALUES` **should** take **keys** whose **values** *can be distributed along the DataFrame*.

For example:
```
COLUMNS: 9, 1
ROWS: 0
VALUES: 4, 15
```
The Output:
```
              LatestValue           PreviousValue
CategoryGroup       Trade                   Trade
Category          Imports   Exports       Imports   Exports
Country
New Zealand        7110.0    6150.0        5450.0    6040.0
Sweden           149500.0  156000.0      162500.0  170600.0
Thailand          27093.8   25720.6       24578.5   24796.6
```
Type `n` in `Change? y/n: `  to move forward.

### Analysis: Change in Value
```
Do you want to calculate the increase in Value from the previous? y/n?:
```
You require to have both `LatestValue` **and** `PreviousValue` columns in your DataFrame (not the pivotized one) to proceed to this section.

Otherwise, you will be forwarded to the next section.

This section will calculate the change in value from `PreviousValue` to `LatestValue`, and make two new columns:

1. `Value Change` will show **absolute** change in value for each row.
2. `Percentage Change(%)` will show **percentage** change in value for each row.

Output(Partial):
```
Value Change Percentage Change(%)
      2515.3                10.23
       924.0                 3.73
    -13000.0                -8.00
    -14600.0                -8.56
         ...                  ...
```
### Quiz (Just Fun)
This section requires that you have selected `Catagory` column in your data, and have **more than one** `Countries`. Otherwise, the section will automatically be skipped.
```
Wanna play a quiz? y/n:
```
This section asks you if you can tell which country have the highest change in value (Value Change) in a randomly selected catagory.
```
Which country shows the highest change in value (Value Change) in Imports category?: Sweden
Correct! It's Sweden
```
Or if you are wrong:
```
Which country shows the highest change in value (Value Change) in Imports category?: Thailand
Oops! Not quite.
 Try again(T) or Reveal answer(R)? t/r:
```
Thus, typing `t` or `r`, you are good to go.

### Export as JSON(Optional)
```
Do you want to export this data to a JSON file? y/n: y
PATH: ../rough/data.json
```
`PATH` is actually the path, where you want to save your file, including the filename with `.json` suffix. For example:
```
PATH: ../rough/data.json
```
else, in the current repository:
```
PATH: data.json
```






