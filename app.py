from flask import Flask

app = Flask(__name__)

# Prosta klasa pomocnicza udająca wiersz z bazy danych,
# aby zadziałało odwołanie row.Title w pętli.
class MockRow:
    def __init__(self, title):
        self.Title = title

@app.route('/')
def index():
    tasks_html = "<h1>Witaj! Aplikacja wdrożona przez GitHub Actions!</h1><ul>"
    tasks_html = "<h1>Witaj! Aplikacja wdrożona przez GitHub Actions!</h1><ul>"

    # Zamiast łączenia się z bazą, tworzymy listę "wierszy" ręcznie
    # na podstawie danych, które podałeś w SQL.
    rows = [
        MockRow('Nauczyc sie Azure App Service'),
        MockRow('Polaczyc aplikacje z baza danych')
    ]

    # Pętla pozostaje bez zmian, iteruje po przygotowanej liście.
    for row in rows:
        tasks_html += f"<li>{row.Title}</li>"

    tasks_html += "</ul>"
    return tasks_html

if __name__ == '__main__':
    app.run(debug=True)