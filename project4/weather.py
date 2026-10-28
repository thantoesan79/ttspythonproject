import csv;
import os;

def read_weather_data(filename):
    weather_data={};
    try:
        with open(filename,'r')as file:
            reader = csv.DictReader(file);
            for row in reader:
                city = row["City"];
                try:
                    temp = float(row["Temperature"]);
                except ValueError:
                    print(f"Invalid temperature '{row['Temperature']}' for {city}.Skipping");
                if city not in weather_data:
                  weather_data[city] = [];
                weather_data[city].append(temp);
    except FileNotFoundError:
         print("File is not found! check the filename and try again ");
    return weather_data;


def show_weather_summaary(weather_data):
    if not weather_data:
        print("No Weather data to show");
        return;
    for city,temp in weather_data.items():
        avg_temp = sum(temp)/len(temp);
        max_temp = max(temp);
        min_temp = min(temp);
    print(f"{city} : ");
    print(f"Average Temperature :{avg_temp : .1f}C");
    print(f"Maximun Temperature :{max_temp : .1f}C");
    print(f"Minimun Temperature :{avg_temp : .1f}C \n");

def main():
    print("Weather Data Analyzer");
    filename = 'weather.csv';
    data = read_weather_data(filename);
    show_weather_summaary(data);


if __name__ == "__main__":
    main();