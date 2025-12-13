from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def hello():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Witaj! Aplikacja wdrożona przez GitHub Actions! Mega sztos zajecia pozdrawiam Szymon Trojak</h1><p>Aktualny czas serwera: {current_time}</p>"

if __name__ == '__main__':
    app.run()
