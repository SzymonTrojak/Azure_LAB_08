# ⚙️ CI/CD z GitHub Actions i Azure App Service

## 🚀 Wprowadzenie i Cel
To repozytorium dokumentuje i przechowuje rozwiązania z **Laboratorium 8**, skupiającego się na automatyzacji procesów **Continuous Integration/Continuous Deployment (CI/CD)**.

Celem laboratorium jest stworzenie w pełni zautomatyzowanego potoku wdrażania za pomocą **GitHub Actions**. Workflow ten ma za zadanie automatycznie budować i wdrażać naszą aplikację **Python/Flask** (rozwijaną w Laboratorium 4) do środowiska **Azure App Service** za każdym razem, gdy zmiany zostaną wprowadzone do głównej gałęzi repozytorium.

## ✨ Kluczowe Technologie i Praktyki

| Technologia/Praktyka | Opis |
| :--- | :--- |
| **CI/CD** | Zbiór praktyk automatyzujących budowanie, testowanie i wdrażanie oprogramowania, co zapewnia szybsze i bardziej niezawodne dostarczanie zmian.  |
| **GitHub Actions** | Platforma CI/CD wbudowana w GitHub, umożliwiająca tworzenie zautomatyzowanych przepływów pracy (workflows) reagujących na zdarzenia w repozytorium. |
| **Azure App Service** | Usługa hostingu aplikacji webowych Microsoft Azure, wykorzystywana jako cel naszego zautomatyzowanego wdrożenia (Deployment Target). |
| **Python/Flask** | Prosta aplikacja webowa, która jest przedmiotem procesu automatycznego wdrożenia. |

## 🛠️ Struktura Projektu (Workflow)

Główna konfiguracja CI/CD znajduje się w pliku:
`./.github/workflows/main.yml`

Ten plik definiuje kroki, które są wykonywane po zdarzeniu `push` na gałęzi `main`:

1.  **Checkout:** Pobranie kodu z repozytorium.
2.  **Setup Python:** Konfiguracja odpowiedniego środowiska Python.
3.  **Install Dependencies:** Instalacja wymaganych pakietów (np. z `requirements.txt`).
4.  **Deployment:** Logowanie do Azure i wdrożenie aplikacji do App Service przy użyciu profilu publikacji.
