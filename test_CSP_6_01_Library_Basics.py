
import CSP_6_01_Library_Basics

from CSP_6_01_Library_Basics import process_expenses, analyze_scores, sanitize_usernames, identify_outliers, binarySearch, search_and_report


def test_process_expenses():
    assert process_expenses([10, 20]) == [11.5, 23]


def test_analyze_scores():
    assert analyze_scores([20,30]) == (25,30)


def test_sanitize_usernames():
    x = ["   Dogs Are Cool", "  Max will play division 1 football        "]
    assert sanitize_usernames(x) == ["dogs are cool", "max will play division 1 football"]



def test_identify_outliers():
    x = [10, 110, 20, 300, 999, 23]
    assert identify_outliers(x) == [110,300,999]


def test_binary_search():
    x = [10,20,23,110,300,999]
    assert binary_search(x,10) == (0,3)

def test_search_and_report():
    x = ["  Apple", "Banana ", "  CHERRY  ", " date "]
    assert search_and_report(x) == 3
