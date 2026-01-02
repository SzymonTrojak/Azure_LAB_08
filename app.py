import logging
from flask import Flask
import datetime
from azure.monitor.opentelemetry import configure_azure_monitor
app = Flask(__name__)


# 1. Importuj funkcję konfiguracyjną


# 2. Skonfiguruj Azure Monitor ZANIM stworzysz obiekt Flask
# Upewnij się, że masz ustawioną zmienną środowiskową APPLICATIONINSIGHTS_CONNECTION_STRING
# lub podaj ją bezpośrednio w connection_string="<twój_klucz>"
configure_azure_monitor(
    enable_live_metrics=True,  # TO JEST KLUCZOWE DLA LIVE METRICS
)


@app.route('/')
def hello():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>TEST! Aplikacja wdrożona przez GitHub Actions! Mega sztos zajecia pozdrawiam Szymon Trojak</h1><p>Aktualny czas serwera: {current_time}</p>"

if __name__ == '__main__':
    app.run()
