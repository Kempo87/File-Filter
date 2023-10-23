

files = ['pierwszy.txt', 'drugi.txt', 'ten powinien być usunięty.zip']


# We select only those files whose name ends in ".txt"
txt_files = [file for file in files if file.endswith(".txt")]

print(txt_files)

# Funkcja do filtrowania plików z danym rozszerzeniem
def find_txt_files(files):
    return [file for file in files if file.endswith('.txt')]

# Testy funkcji
def test_find_txt_files():
    # Przypadek testowy: brak plików
    files = []
    assert find_txt_files(files) == []

    # Przypadek testowy: lista zawiera tylko pliki .txt
    files = ['pierwszy.txt', 'drugi.txt', 'trzeci.txt']
    assert find_txt_files(files) == ['pierwszy.txt', 'drugi.txt', 'trzeci.txt']

    # Przypadek testowy: lista zawiera różne rozszerzenia
    files = ['pierwszy.txt', 'drugi.doc', 'trzeci.txt', 'czwarty.pdf']
    assert find_txt_files(files) == ['pierwszy.txt', 'trzeci.txt']

    # Przypadek testowy: lista zawiera tylko pliki bez rozszerzenia
    files = ['plik1', 'plik2', 'plik3']
    assert find_txt_files(files) == []

    # Przypadek testowy: pusta lista
    files = []
    assert find_txt_files(files) == []