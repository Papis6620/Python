
# Projekt: Generowanie labiryntu

## Opis projektu

Aplikacja generuje labirynty przy użyciu algorytmu DFS. Labirynty mogą być wizualizowane, zapisywane i ładowane z plików. Interfejs graficzny aplikacji został stworzony w oparciu o bibliotekę Tkinter, a wizualizacja labiryntu wykorzystuje matplotlib.

## Funkcjonalności

1. **Generowanie labiryntu**

   - Użytkownik podaje szerokość i wysokość labiryntu.
   - Labirynt generowany jest przy użyciu algorytmu DFS

2. **Wizualizacja labiryntu**

   - Labirynt jest wyświetlany w formie graficznej za pomocą matplotlib.

3. **Zapisywanie labiryntu**

   - Labirynt można zapisać do pliku z rozszerzeniem `.maze`.
   - Aby zapisać labirynt do pliku, należy wcześniej wygenerować labirynt.

4. **Wczytywanie labiryntu**

   - Użytkownik może wczytać wcześniej zapisany labirynt i ponownie go wyświetlić.

5. **Interfejs graficzny**

   - Aplikacja oferuje prosty i intuicyjny interfejs z menu głównym, pozwalający na:
     - Generowanie nowego labiryntu
     - Zapisane wygenerowanego labiryntu
     - Wczytywanie istniejeącego labiryntu
     - Zamknięcie aplikacji

## Struktura kodu

1. **get\_maze\_size**:

   - Pobiera od użytkownika rozmiar labiryntu.

2. **initialize\_maze**:

   - Tworzy początkową strukturę labiryntu z wszystkimi ścianami.

3. **generate\_maze**:

   - Generuje labirynt za pomocą algorytmu DFS:
       - Zaczynamy od komórki (0,0), oznaczając ją jako odwiedzoną.
       - Losujemy kolejność ruchów (góra, dół, lewo, prawo) i sprawdzamy, czy można przejść do sąsiedniej nieodwiedzonej komórki.
       - Jeśli można, przechodzimy do niej, usuwamy odpowiednią ścianę i dodajemy poprzednią pozycję do stosu.
       - Jeśli nie możemy się ruszyć, cofamy się po stosie, aż znajdziemy komórkę z dostępnym ruchem.
       - Proces trwa, aż wszystkie komórki zostaną odwiedzone.

4. **visualize\_maze**:

   - Wizualizuje labirynt przy użyciu matplotlib.

5. **save\_maze**:

   - Zapisuje labirynt do pliku `.maze`.
   - Plik .maze zawiera:
       - WIDTH (int): Szerokość labiryntu
       - HEIGHT (int): Wysokość labiryntu
       - horizontal_walls (np.array): Tablicę zawierającą poziome ściany
       - vertical_walls (np.array): Tablicę zawierającą pionove ściany

6. **load\_maze**:

   - Wczytuje labirynt z pliku `.maze`.

7. **main\_menu**:

   - Obsługuje menu główne aplikacji.

---

Autor: Patryk Krzywda

