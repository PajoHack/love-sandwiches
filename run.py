import gspread
from google.oauth2.service_account import Credentials 


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('CREDS.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPRED_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPRED_CLIENT.open('love_sandwiches')


sales = SHEET.worksheet('sales')


data = sales.get_all_values()


def get_sales_data():
    """ 
    Get sales input figures from user.
    """

    print("Please enter sales figures from last market day")
    print("Data should be 6 numbers")
    print("Example: 10,45,12,5,32,87\n")

    data_str = input("Enter your data here: ")

    sales_data = data_str.split(",")
    validate_values(sales_data)


def validate_values(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted to int,
    or if there aren't exactly 6 values.
    """
    try: 
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


get_sales_data()
