import requests
import tradingeconomics as te
import sys
import pandas as pd
import random as r


def log_in():
    global account_type
    print(
        f"""
This is a simple \033[1;4m Data Exploration and Analysis tool\033[0m for INDICATOR DATA by countries.
The data is gathered from TradingEconomics website. Visit at: https://tradingeconomics.com

\033[1mI want to log-in as a/an:\033[0m \n<1> Default User (Account type: Free)\n<2> Existing Free User of TradingEconomics\n<3> Existing Premium User of TradingEconomics
(Type in the corresponding integer only)
"""
    )
    while True:
        try:
            key = int(input(">>> ").strip())
            if key == 1:
                apikey = "3cfb51495de84f9:ku5xzon6e63jmas"
                te.login(apikey)
                account_type = key
                break
            elif key == 2 or key == 3:
                while True:
                    apikey = input(
                        "Input your API-Key from TradingEconomics account: "
                    ).strip()
                    try:
                        te.login(apikey)
                        account_type = key
                        break
                    except:
                        print("Please check your input and try again.")
                break
            else:
                print("Input one among these two integers: '1' or '2'")
        except (ValueError, UnboundLocalError):
            print("Input one INTEGER only: '1' or '2'")

    global API_KEY
    API_KEY = apikey


def commentary(variable):
    if variable == "indicator":
        return f"Please select and type Indicator(s) from :{link("indicator")}\nFor Example: Imports; or Imports, 1 Year MLF Rate\n[Case-sensitive, comma-separated(if multiple)]"
    elif variable == "country":
        return f"Please select and type Country(s) from: {validate_country()}"


def link(variable):
    if variable == "indicator":
        return f"https://api.tradingeconomics.com/indicators?c={API_KEY}"
    elif variable == "country":
        return f"https://api.tradingeconomics.com/country?c={API_KEY}"


def com_sep(str):
    t = str.split(",")
    list = []
    for one in t:
        list.append(one.strip())
    return list


def validate_indicator(indicator, apikey="guest:guest"):
    r = requests.get(f"https://api.tradingeconomics.com/indicators?c={apikey}")
    indicator_list = [i["Category"] for i in r.json()]
    indicator = indicator.split(",")
    new_list = []
    for one in indicator:
        if one.strip() in indicator_list:
            new_list.append(one.strip())
        else:
            break
    return new_list


def validate_country(_country="_all_available_countries|not_typable__"):
    url_country = link("country")
    data = requests.get(url_country)
    country_list_premium = [i["Country"] for i in data.json()]
    country_list_free = ["Mexico", "Sweden", "New Zealand", "Thailand"]
    country_list = []
    o = []
    if account_type in (1, 2) or API_KEY == "guest:guest":
        country_list = o = country_list_free
    if account_type == 3 and API_KEY != "guest:guest":
        country_list = country_list_premium
        o = url_country
    global country
    list = _country.split(",")
    country = []
    for one in list:
        if one.strip().title() in country_list:
            country.append(one.strip().title())

    if list[0] == "_all_available_countries|not_typable__":
        if account_type in (1, 2) or API_KEY == "guest:guest":
            return f"{', '.join(o)}"
        elif account_type == 3 or API_KEY != "guest:guest":
            return o

    return country


def column_select(json_dict_list):
    pairs = {}
    for i, column in enumerate(json_dict_list[0].keys()):
        pairs[i] = column
    print(
        f"""\n\nSelect columns to analyze: \nfor all columns: input 'all'\nfor specific columns: integer(key) corresponding to the column name, *comma-separated*.\n\n{pairs}"""
    )
    while True:
        try:
            n = com_sep(input(">>> "))
            digits = []
            for i in n:
                if (len(n) == 1 and n[0] == "all") or (
                    int(i) in pairs.keys() and 0 <= int(i) <= 16
                ):
                    digits.append(i)
                else:
                    print(
                        "Outside the provided options or range of integers(keys). Try again."
                    )
                    continue
            break
        except ValueError:
            print("Only 'all' or corresponding INTEGERS are valid inputs.")
            continue

    global selected_columns
    selected_columns = []
    if digits[0] == "all":
        selected_columns = list(pairs.values())
    else:
        for i in digits:
            selected_columns.append(pairs[int(i)])
    return selected_columns


def generate_newtable(json_data, selected_columns):
    nt = []
    for datum in json_data:
        nr = {}
        for i in selected_columns:
            nr[i] = datum[i]
        nt.append(nr)
    return nt


def customize(dataframe):
    while True:
        y = input(
            "Want to narrow down or customize the table visualization (Recommended if your data is so complex)? y/n: "
        )
        if y == "y":
            while True:
                print(
                    f"""
Select COLUMNS,ROWS and VALUES, \033[4mno greater than Two\033[0m for each, according to your preference: Comma-separated
VALUES must be the ones that you will compare or visualize.
Read the tutorial before you proceed...

type in corresponding integer:
        {[f"{n}: {i}" for n,i in enumerate(selected_columns)]}
    """
                )
                col = colrow_generator(com_sep(input("COLUMNS: ")))
                row = colrow_generator(com_sep(input("ROWS: ")))
                value = colrow_generator(com_sep(input("VALUES: ")))
                if col != None and row != None and value != None:
                    new_df = dataframe.pivot(index=row, columns=col, values=value)
                    print(new_df)
                    breakloop = True
                    while True:
                        t = input("Change? y/n: ").strip()
                        if t == "y":
                            breakloop = False
                            break
                        elif t == "n":
                            break
                        else:
                            print("Type y or n.")
                            continue
                    if breakloop == True:
                        break
                else:
                    print("Please check your inputs and try again.")
        elif y.strip() == "n":
            print("Great!")
            break
        else:
            print("type y or n")
            continue
        break


def colrow_generator(list):
    l = []
    if len(list) <= 3:
        try:
            for n in list:
                l.append(selected_columns[int(n)])
            return l
        except:
            return None
    else:
        print("Number of input(s) must not exceed 3")
        return None


def solid_or_percentage_increase_from_previous_value(df):
    while True:
        y_n = input(
            "Do you want to calculate the increase in Value from the previous? y/n?: "
        )
        if y_n.strip() == "y":
            df["Value Change"] = df["LatestValue"] - df["PreviousValue"]
            df["Percentage Change(%)"] = (
                (df["Value Change"] / df["PreviousValue"]) * 100
            ).round(2)
            print(df)
            tf = True
            while True:
                if (
                    "Category" in selected_columns
                    and "Country" in selected_columns
                    and len(countries) > 1
                ):
                    quiz = input("Wanna play a quiz? y/n: ")
                    if quiz.strip() == "y":
                        r_ind = r.choice(indicator)
                        choosen_catdf = df[df["Category"] == r_ind]
                        print(choosen_catdf)
                        max_val = abs(choosen_catdf["Value Change"]).max()
                        gg = choosen_catdf[
                            abs(choosen_catdf["Value Change"]) == max_val
                        ]
                        c = [i for i in gg["Country"]]
                        while True:
                            x = input(
                                f"Which country shows the highest change in value (Value Change) in {r_ind} category?: "
                            )
                            if x.strip().title() in c:
                                print(f"Correct! It's {x.title()}")
                                break
                            else:
                                try_ = input(
                                    "Oops! Not quite.\n Try again(t) or Reveal answer(r)? t/r: "
                                )
                                if try_.strip() == "t":
                                    continue
                                elif try_.strip() == "r":
                                    print(
                                        "The answer is/are:",
                                        revealor(c),
                                        "\nThank you!",
                                    )
                                else:
                                    print("Type in either 't' or 'r'.")
                                    continue
                                break
                        return df
                    elif quiz.strip() == "n":
                        return df
                    else:
                        print("Type in either 'y' or 'n'.")
                        continue
                return df
        elif y_n.strip() == "n":
            return df
        else:
            print("Type in either 'y' or 'n'.")


def revealor(list):
    if len(list) == 1:
        return list[0]
    elif len(list) > 1:
        return f"{', '.join(list)}"


def main():
    global data
    log_in()
    global indicator
    global countries
    while True:
        print(f"\n{commentary("country")}")
        countries = validate_country(input("Countries: "))
        if countries != []:
            break
        else:
            continue
    while True:
        print(f"\n{commentary("indicator")}")
        indicator = validate_indicator(input("Indicator: "), API_KEY)
        if indicator != []:
            break
        else:
            continue
    data = te.getIndicatorData(
        country=countries, indicators=indicator, output_type="dict"
    )
    if data is not None:
        selected_columns = column_select(data)
        new_data = generate_newtable(data, selected_columns)
        df = pd.DataFrame(new_data)
        df.index += 1
        print("\n\n", df)
        if len(indicator) > 1 or len(countries) > 1:
            customize(df)
        if "LatestValue" in selected_columns and "PreviousValue" in selected_columns:
            df = solid_or_percentage_increase_from_previous_value(df)

        while True:
            ans = input("Do you want to export this data to a JSON file? y/n: ").strip()
            if ans == "y":
                path = input("PATH: ").strip()
                try:
                    df.to_json(path, orient="records")
                    break
                except:
                    print("Sorry, there might have been a problem. Check your input.")
                    continue
            elif ans == "n":
                sys.exit(
                    "\nHope we have eased your work!\nThank you and see you again.\n"
                )
            else:
                continue
    else:
        sys.exit(
            "No data available for the provided combination of Country and Indicator. Please try again."
        )


if __name__ == "__main__":
    main()
