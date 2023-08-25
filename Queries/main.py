import pandas as pd
import webbrowser

# Dictionary mapping user selections to services and countries
services_map = {
    "1": "Dentist in ",
    "2": "Locksmith in ",
    "3": "Dermatologist in ",
    "4": "Pet Services in "
}

countries_map = {
    "1": "Canada",
    "2": "United States",
    "3": "England",
    "4": "Australia"
}

def user_input(prompt, options):
    while True:
        print(prompt)
        for key, value in options.items():
            print(f"Select {key} for {value}")
        user_selection = input("Enter your choice: ")
        if user_selection in options:
            return user_selection
        else:
            print("Error")

def do_search(query):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    search_url = f'https://www.google.com/search?q={query}'
    webbrowser.get("chrome").open_new_tab(search_url)

def open_csv(services, country):
    csv_file = f'{country}.csv'
    
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file)
    
    for query in df['Queries']:
        query = services_map[services] + query.replace(' ', '+')
        print(query)
        do_search(query)

def main():
    selected_services = user_input("Select a service:", services_map, '\n')
    selected_country = user_input("Select a country:", countries_map, '\n')
    
    open_csv(selected_services, countries_map[selected_country])

if __name__ == "__main__":
    main()
