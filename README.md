# Golden Section Search
Implementacja projektu na zajęcia z Teorii Sterowania.

## Temat projektu
Metoda minimalizacji funkcji nieliniowej ciągłej w kierunku (metoda złotego podziału) - optymalizacja funkcji nieliniowej ciągłej bez ograniczneń dla podanego kierunku poszukiwań. Omówienie efektywności działania algorytmu dla różnych funkcji testowych.

## TODO
- [X] Stworzenie repozytorium i podstawowej struktury projektu
- [ ] Ustalenie workflow i wymagań projektu (np. wersja intepretera Pythona)
- [ ] Implementacja GUI
- [ ] Zrozumienie działania metody
- [ ] ...
- [ ] Zrobienie dokumentacji projektu

## Praca z projektem
Aby uruchomić aplikację po sklonowaniu repozytorium, należy zainstalować wymagane paczki. Instrukcja jest napisana dla systemu Linux. Na Windowsie zasada działania jest podobna, ale komendy się nieznacznie różnią.

### Virual Enviroment
Żeby nie zaśmiecać sobie kompa globalnie, warto stworzyć wirtualne środowisko. PyCharm robi to automatycznie, kiedy tworzy projekt, ale jeśli wykorzystywane jest inne IDE albo venv nie został stworzony można to zrobić wpisując w terminal komendę:
```
python3 -m venv /path/to/new/virtual/environment
```
W miejsce `/path/to/new/virtual/environment` można wstawić po prostu `venv`, wtedy środowisko zostanie stworzone w folderze, w którym aktualnie znajduje się użytkownik pod folderm `venv`. Aby aktywować środowisko należy wpisać:
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
