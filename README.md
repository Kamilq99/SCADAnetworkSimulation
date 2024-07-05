# Ochrona Urządzeń OT/IoT za pomocą Suricata


# System Sygnalizacji Świetlnej z Symulacją SCADA i PLC

## Opis Projektu

Ten projekt symuluje system sygnalizacji świetlnej zarządzany przez system SCADA (Supervisory Control and Data Acquisition), który komunikuje się z PLC (Programmable Logic Controller). Wizualizacja sygnalizacji świetlnej jest obsługiwana przez aplikację frontendową za pomocą HTML i CSS. Docker jest używany do konteneryzacji każdego komponentu systemu, co ułatwia wdrażanie i zarządzanie.

### Komponenty

1. **Lights**:
    - `Lights.html`: Plik HTML tworzący wizualizację sygnalizacji świetlnej.
    - `LightsStyle.css`: Plik CSS stylizujący sygnalizację świetlną.
    - `Dockerfile`: Konfiguracja Dockera do serwowania plików HTML i CSS za pomocą Nginx.
    - `.dockerignore`: Plik określający, które pliki mają być ignorowane podczas budowania obrazu Docker.

2. **SCADA**:
    - `scada_controller.py`: Skrypt Pythona symulujący system SCADA, który co 30 sekund wysyła komendy do PLC.
    - `Dockerfile`: Konfiguracja Dockera dla systemu SCADA.

3. **PLC**:
    - `PLC.py`: Skrypt Pythona symulujący PLC, który steruje sygnalizacją świetlną na podstawie komend otrzymanych od systemu SCADA.
    - `Dockerfile`: Konfiguracja Dockera dla PLC.

## Jak Uruchomić

### Wymagania

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Kroki do Uruchomienia

1. Sklonuj repozytorium:

    ```bash
    git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation.git)
    ```

2. Zbuduj i uruchom kontenery:

    ```bash
    docker-compose up --build
    ```

3. Uzyskaj dostęp do wizualizacji sygnalizacji świetlnej:

    Otwórz przeglądarkę internetową i przejdź do `http://localhost:8080`.

### Konfiguracja Docker Compose

Plik `docker-compose.yml` jest używany do definiowania i uruchamiania aplikacji Docker z wieloma kontenerami. Konfiguracja obejmuje:

- **Lights**: Uruchamia serwer Nginx do serwowania plików HTML i CSS.
- **SCADA**: Uruchamia skrypt kontrolera SCADA.
- **PLC**: Uruchamia skrypt PLC.

#Wygląd Wizualizacji

![Red Light](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation/assets/83961352/24c03f55-cbe7-43b3-a3b6-3c69d35284c3)
![Yellow Light](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation/assets/83961352/33285bb9-293e-4807-96f8-fcdf97bcc485)
![Green Light](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation/assets/83961352/99875af1-c3f3-46ed-b4b4-f2bb584352d3)
