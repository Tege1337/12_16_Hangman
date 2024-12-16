from country_list import get_countries
import random
from colorama import Fore, Back, Style
from ascii import current_lives


countries = get_countries()
guesses = []


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

def pro_countries():
    pro_diff_countries = []
    for country in countries:
        if len(country) > 14:
            pro_diff_countries.append(country)
    return pro_diff_countries

print(Fore.BLACK + "Akasztófa 💀💀💀" + Fore.WHITE)
print(Fore.GREEN + "Kezdő szint (1.) \n" + Fore.BLACK + "8 karakterig terjedő országok")
print(Fore.YELLOW + "Haladó szint (2.) \n" + Fore.BLACK + "14 karakterig terjedő országok")
print(Fore.RED + "Professzionális szint (3.)\n" + Fore.BLACK + "14 feletti karakterszámú országok" + Fore.WHITE)
difficulty = str(input("Kérlek válassz egy nehézségi szintet! (Az indexét írd be) "))

 
if difficulty == "1" or difficulty == "1.":
    print("Kezdő szint kiválasztva! ")
    
    lives = 7
    print(f"{lives} életed van! ")
    
    country = easy_countries()
    random_country = random.choice(country)
    print(random_country)

    for char in random_country:
        print("_ " * len(char), end="")
    guess_input = str(input("Kérlek adj meg egy tippet (betű) "))


elif difficulty == "2" or difficulty == "2.":
    print("Haladó szint kiválasztva! ")
    country = adv_countries()

    lives = 6
    print(f"{lives} életed van! ")


elif difficulty == "3" or difficulty == "3.":
    print("Professzionális szint kiválasztva! ")
    country = pro_countries()

    lives = 5
    print(f"{Fore.RED}{"🫀 " * lives} ({lives}) életed van! {Fore.WHITE}")

    random_country = random.choice(country)
    goal = list(random_country)
    
    for char in goal:
        if char == " ":
            print(" ", end="")
        else:
            print("_", end=" ")

