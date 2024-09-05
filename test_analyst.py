from project import validate_indicator, validate_country, com_sep, link, log_in, revealor
import tradingeconomics as te

def test_com_sep():
    assert com_sep("Mexico")== ["Mexico"]
    assert com_sep("Mexico, tt, xx, sweden")== ["Mexico", "tt", "xx", "sweden"]
    assert com_sep("  new zealand,  albania,  Afghanistan  ,")== ["new zealand", "albania", "Afghanistan", "" ]

def test_revealor():
    assert revealor(["Thailand"])== "Thailand"
    assert revealor(["Thailand", "Germany", "Bangladesh"])== "Thailand, Germany, Bangladesh"

def test_validate_indicator():
    assert validate_indicator("  1 Year MLF Rate  ,14-Day Reverse Repo Rate,      15 Year Mortgage Rate" )== ["1 Year MLF Rate", "14-Day Reverse Repo Rate", "15 Year Mortgage Rate"]
    assert validate_indicator("Imports, Exports")== []
    assert validate_indicator("1 year MLF Rate")== []


    








