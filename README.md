# Golden Section Search
Implementacja projektu na zajęcia z Teorii Sterowania.

## Temat projektu
Metoda minimalizacji funkcji nieliniowej ciągłej w kierunku (metoda złotego podziału) - optymalizacja funkcji nieliniowej ciągłej bez ograniczneń dla podanego kierunku poszukiwań. Omówienie efektywności działania algorytmu dla różnych funkcji testowych.

## TODO
- Ustalenie workflow i wymagań projektu (np. wersja intepretera Pythona)
- Implementacja GUI
- Zrozumienie działania metody
- ...
- Zrobienie dokumentacji projektu

## Praca z projektem
Aby uruchomić aplikację po sklonowaniu repozytorium, należy zainstalować wymagane paczki.

### Virual Enviroment
Żeby nie zaśmiecać sobie kompa globalnie, warto stworzyć wirtualne środowisko. PyCharm robi to automatycznie, kiedy tworzysz projekt, ale jeśli korzystasz z innego IDE albo venv nie został stworzony możesz to zrobić wpisują w terminal komendę (instrukcja dla Linuxa, w Windowsie może być troszkę inaczej):
```
python3 -m venv /path/to/new/virtual/environment
```
W miejsce /path/to/new/virtual/environment można wstawić po prostu venv. Aby aktywować środowisko należy wpisać:
```
source /path/to/new/virtual/environment/bin/activate
```

### Instalacja paczek
Wszystkie potrzebne do uruchomienia projektu paczki można znaleźć w pliku `setup.py` w części `install_requires`. W celu zainstalowania potrzebnych paczek należy wpisać:
```
python3 setup.py install
```

### Uruchamianie aplikacji
Uruchomienie aplikacji sprowadza się do wpisania komendy:
```
python3 run.py
```
Oczywiście można zrobić to z IDE uruchamiając plik `run.py`.
