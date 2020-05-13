# Golden Section Search
Implementacja projektu na zajęcia z Teorii Sterowania. Wszystkie materiały związane z projektem można znaleźć w folderze [docs/src](docs/src). Zasady pracy nad projektem znajdują się w pliku [Definition of Done](docs/dod.md).

## Temat projektu
Metoda minimalizacji funkcji nieliniowej ciągłej w kierunku (metoda złotego podziału) - optymalizacja funkcji nieliniowej ciągłej bez ograniczneń dla podanego kierunku poszukiwań. Omówienie efektywności działania algorytmu dla różnych funkcji testowych.

## TODO
Wszystkie taski dotyczące projektu można znaleźć w zakładce [Projects](https://github.com/damianschmidt/golden-section-search/projects/1?add_cards_query=is%3Aopen).

### Uwagi prowadzącej
Parametry wejściowe:
 - funkcja wejściowa
 - punkt startowy
 - kierunek
 - długość przedziału τ
 - dokładność ε
 
Koniec przedziału: x<sub>b</sub> = x<sub>0</sub> + τ * kierunek
 
Funkcja jest z założenia funkcją monoticzną, dlatego jeśli nie jest (bo nie ma w założeniach) to może wpaść w minimum lokalne.

Kierunek jest wektorem(?) na przykład [1, 2].

Narysować warstwice dla n = 2 i zaznaczyć ostateczny punkt optymalny.

### Uwagi podczas oddania

Testowane na funkcjach:

- f(x) = sin(x1) * sin(x2) * exp(-(x1^2 + x2^2))
  - x0 = [-4, 4]
  - d = [1, -1]

- f(x) = (2 - x1)^2 + (2 - x2)^2
  - x0 = [-2, -2]
  - d = [1, 1]

- f(x) = x1^4 + x2^4 - 0.62 * x1^2 - 0.62 * x2^2
  - x0 = ?
  - d = ?


Zrobić tak, aby sin(x1) * sin(x2) * exp(-(x1^2 + x2^2)) wpadało w oba minima. Oburzona o wynik dla x0 = [2, -3], d = [-1, 1]

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
