# Traffic light simulation system

## Project Description

Ten projekt symuluje system sygnalizacji świetlnej zarządzany przez system SCADA (Supervisory Control and Data Acquisition), który komunikuje się z PLC (Programmable Logic Controller). Wizualizacja sygnalizacji świetlnej jest obsługiwana przez aplikację frontendową za pomocą HTML i CSS. Docker jest używany do konteneryzacji każdego komponentu systemu, co ułatwia wdrażanie i zarządzanie.

### Components

1. **Lights**:
    - `Lights.html`: HTML file creating a traffic light visualization.
    - `LightsStyle.css`: CSS file styling the traffic light.
    - `Dockerfile`: Configuring Docker to serve HTML and CSS files using Nginx.

2. **SCADA**:
    - `scada_controller.py`: Python script simulating a SCADA system that sends commands to a PLC every 30 seconds.
    - `Dockerfile`: Docker configuration for SCADA system.

3. **PLC**:
    - `PLC.py`: A Python script simulating a PLC that controls traffic lights based on commands received from a SCADA system.
    - `Dockerfile`: Docker configuration for PLC.

## Jak Uruchomić

### Wymagania

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Kroki do Uruchomienia

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

# Wygląd Wizualizacji

![Red Light](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation/assets/83961352/24c03f55-cbe7-43b3-a3b6-3c69d35284c3)
![Yellow Light](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation/assets/83961352/33285bb9-293e-4807-96f8-fcdf97bcc485)
![Green Light](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation/assets/83961352/99875af1-c3f3-46ed-b4b4-f2bb584352d3)
