import pandas
import lxml

def get_df():

    df = pandas.read_html("https://docs.google.com/spreadsheets/d/1L541b2iHC1TnmA9qR3JVQm7JqLIlw9eXNkixQjKSvXU/edit#gid=1580249766", encoding='utf8', skiprows=1)[0]

    return df


if __name__ == "__main__":
    x = get_df()

    print(x)