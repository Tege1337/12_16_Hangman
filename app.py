from country_list import get_countries
import random

countries = get_countries()
print(countries)

def easy_countries():
    easy_diff_countries = []
    for country in countries:
        if len(country) < 8:
            easy_diff_countries.append(country)
    return easy_diff_countries

def adv_countries():
    adv_diff_countries = []
    for country in countries:
        if len(country) < 14:
            adv_diff_countries.append(country)
    return adv_diff_countries

def adv_countries():
    pro_diff_countries = []
    for country in countries:
        if len(country) > 14:
            pro_diff_countries.append(country)
    return pro_diff_countries

difficulty = str(input("× AKASZTÓFA ×\n" 
                        "Kezdő szint (1.) \n"
                        "Haladó szint (2.) \n"
                        "Professzionális szint (3.)\n"
                        "Milyen szinten szeretnél játszani? "))

if difficulty == "1" or difficulty == "1.":
    print("Kezdő szint kiválasztva! ")
    country = easy_countries()
    random_country = random.choice(country)
    print(random_country)
    for char in random_country:
        print("_ " * len(char), end="")
elif difficulty == "2" or difficulty == "2.":
    print("Haladó szint kiválasztva! ")
    country = adv_diff_countries()
elif difficulty == "3" or difficulty == "3.":
    print("Professzionális szint kiválasztva! ")
    country = pro_diff_countries()

    
