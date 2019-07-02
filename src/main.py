import acquisition
import after_main
import clean
import api

def main():
    data = read_file('../Input/MissingMigrants.csv')
    data_clean = cleaning(data)
    data_api = datafromApi(url, my_dataframe)

if __name__ == "__main__":
    main()