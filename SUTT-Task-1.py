import pandas as pd
import json

def clean_cell_value(value):

# Removing the unnecessary asterisks

    if isinstance(value, str):
        if set(value.strip()) == {'*'}:
            return ""
        return " ".join(value.split())
    return value

def extract_daily_menu(df):
#Exporting the menu into json, date being the key
    menu_data = {}
    
    for col in range(df.shape[1]):
        date_value = df.iloc[0, col]
        if pd.isna(date_value):
            continue
        
        date_key = date_value.strftime("%d-%m-%Y")
        menu_data[date_key] = {
            "Breakfast": [clean_cell_value(df.iloc[row, col]) for row in range(2, 11) if pd.notna(df.iloc[row, col])],
            "Lunch": [clean_cell_value(df.iloc[row, col]) for row in range(13, 21) if pd.notna(df.iloc[row, col])],
            "Dinner": [clean_cell_value(df.iloc[row, col]) for row in range(23, 30) if pd.notna(df.iloc[row, col])],
        }
    
    return menu_data

def save_to_json(data, filename="mess_menu.json"):
#export to JSON
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def main():
    excel_file = "sutt.xlsx"
    sheet = "Sheet1"
    df = pd.read_excel(excel_file, sheet_name=sheet)
    
    menu_json = extract_daily_menu(df)
    print(json.dumps(menu_json, indent=4))
    save_to_json(menu_json)

if __name__ == "__main__":
    main()
