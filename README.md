OPIS PROGRAMU: prosty program mający na celu filtrację listy plików, pozostawiając tylko te, które kończą się rozszerzeniem ".txt". 

Funkcja filter_txt(files): Ta funkcja przyjmuje listę plików jako argument i zwraca nową listę, która zawiera tylko pliki, których nazwy kończą się na ".txt". Wykorzystuje ona list comprehension do filtrowania plików na podstawie ich nazw.

Funkcja main(): Ta funkcja jest głównym punktem wejścia programu. Wewnątrz tej funkcji zdefiniowana jest lista files, która zawiera nazwy plików. Następnie wywoływana jest funkcja filter_txt(files) do filtrowania plików i wynik jest przypisywany do zmiennej filtered. Na koniec wynik jest wyświetlany na konsoli za pomocą funkcji print().

Warunek if __name__ == "__main__": sprawdza, czy program jest uruchamiany jako plik główny, a jeśli tak, to uruchamia funkcję main().

Program ten ma za zadanie zastosować prostą logikę filtrowania na liście plików i wyświetlić tylko te, które mają rozszerzenie ".txt". Wynik działania programu będzie wyglądać tak:
['pierwszy.txt', 'drugi.txt']
Plik o nazwie "ten powinien być usunięty.zip" jest pominięty, ponieważ nie spełnia warunku filtrowania kończącego się na ".txt".