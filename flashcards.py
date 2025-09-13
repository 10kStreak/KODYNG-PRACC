import random

slovicka = {
    "Pes": ["Dog", "Doggo"],
    "Kočka":  ["Cat", "Kitty"],
    "Párek": ["Sausage", "Glizzy"],

}

print("Ahoj! Vítej v PopUpFlashCards!")

while True:
    ceske_slovo = random.choice(list(slovicka.keys()))
    if random.choice([True, False]):
        print(f"\nJak se anglicky řekne '{ceske_slovo}' ?")
        odpoved = input("Tvoje odpověď: ").lower()
        spravne_odpovedi = [o.lower() for o in slovicka[ceske_slovo]]
     
    else:
        anglicka_varianta = random.choice(slovicka[ceske_slovo])
        print(f"\nJak se česky řekne '{anglicka_varianta}' ?")
        odpoved = input("Tvoje odpověď: ").lower()
        spravne_odpovedi = [ceske_slovo.lower()]

    if odpoved == 'konec':
        print("Díky za procvičení!")
        break
    if odpoved in spravne_odpovedi:
        print("Super! Správná odpověď!")
    else:
        print(f"Špatně! Správná odpověď je: {', '.join(spravne_odpovedi)}")