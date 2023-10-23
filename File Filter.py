def filter_txt(files):
    return [f for f in files if f.endswith('.txt')] # jednoliterowa nazwa zmiennej w list comprehension jest ok
def main():
    files = ['pierwszy.txt', 'drugi.txt', 'ten powinien być usunięty.zip']
    filtered = filter_txt(files)
    print(filtered)

if __name__ == "__main__":
    main()