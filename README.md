# Golden Section Search
Implementacja projektu na zajęcia z Teorii Sterowania. Wszystkie materiały związane z projektem można znaleźć w folderze [docs/src](docs/src). Zasady pracy nad projektem znajdują się w pliku [Definition of Done](docs/dod.md).

## Temat projektu
Metoda minimalizacji funkcji nieliniowej ciągłej w kierunku (metoda złotego podziału) - optymalizacja funkcji nieliniowej ciągłej bez ograniczneń dla podanego kierunku poszukiwań. Omówienie efektywności działania algorytmu dla różnych funkcji testowych.

## TODO
- [X] Stworzenie repozytorium i podstawowej struktury projektu
- [X] Ustalenie workflow i wymagań projektu (np. wersja intepretera Pythona)
- [X] Dodanie przykładowych funkcji
- [ ] Implementacja GUI
    - [X] ComboBox z możliwością wpisywania funkcji
    - [X] Możliwość wyboru kryterium stopu
    - [X] Możliwość wpisania ilości iteracji (kryt. stopu)
    - [X] Możliwość wpisania przedziałów poszukiwań
    - [X] Prompter do obserwacji wyników
    - [ ] Rysowanie warstwic dla n = 2
    - [ ] Możliwość wpisywania ograniczeń rysunku
    - [ ] ...
- [X] Implementacja algorytmu dla n = 1
- [ ] Implementacja parsera funkcji
    - [X] Implementacja leksera
    - [X] Implementacja parsera
    - [X] Implementacja interpretera
    - [ ] ...
- [ ] Implementacja algorytmu dla n <= 5
- [ ] ...
- [ ] Zrobienie dokumentacji projektu

## Praca z projektem
Aby uruchomić aplikację po sklonowaniu repozytorium, należy zainstalować wymagane paczki.

### Virual Enviroment
Żeby nie zaśmiecać sobie kompa globalnie, warto stworzyć wirtualne środowisko. PyCharm robi to automatycznie, kiedy tworzy projekt, ale jeśli wykorzystywane jest inne IDE albo venv nie został stworzony można to zrobić wpisując w terminal komendę:
```
python3 -m venv /path/to/new/virtual/environment (Linux)
python -m venv /path/to/new/virtual/environment (Windows)
```
W miejsce `/path/to/new/virtual/environment` można wstawić po prostu `venv`, wtedy środowisko zostanie stworzone w folderze, w którym aktualnie znajduje się użytkownik pod folderm `venv`. Aby aktywować środowisko należy wpisać:
```
source /path/to/new/virtual/environment/bin/activate (Linux)
.\path\to\new\virtual\environment\Scripts\activate (Windows)
```

### Instalacja paczek
Wszystkie potrzebne do uruchomienia projektu paczki można znaleźć w pliku [requirements.txt](requirements.txt). W celu zainstalowania potrzebnych paczek należy wpisać:
```
pip3 install -r requirements.txt (Linux)
pip install -r requirements.txt (Windows)
```

### Uruchamianie aplikacji
Uruchomienie aplikacji sprowadza się do wpisania komendy:
```
python3 run.py (Linux)
python run.py (Windows)
```
Oczywiście można zrobić to z IDE uruchamiając plik `run.py`.
