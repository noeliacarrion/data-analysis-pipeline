from god import *

def main():
    data = read_file('../Input/MissingMigrants.csv')
    BASE_URL = "https://api.darksky.net/forecast" 
    data_clean = cleaning(data)
    data_apis = datafromApi(data_clean)
    plot_finals = analysis_plot()

if __name__ == "__main__":
    main()
