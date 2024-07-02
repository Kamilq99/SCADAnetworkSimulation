# Ochrona Urządzeń OT/IoT za pomocą Suricata


![SCADA](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation/assets/83961352/087715ea-3307-4249-8046-1f6f58666dc9)


## Przegląd Projektu

Celem tego projektu jest przedstawienie, jak chronić urządzenia OT (Operation Technology) oraz IoT (Internet of Things) przed zagrożeniami hakerskimi za pomocą systemu Suricata. Symulacja obejmuje urządzenia zarządzane za pomocą Docker i Docker Compose, wykorzystując Python oraz framework Flask do emulacji urządzeń.

## Struktura Repozytorium

Repozytorium składa się z trzech głównych folderów oraz pliku `docker-compose.yaml`:

1. **lights**:

   - Zawiera kod w języku Python symulujący działanie świateł drogowych.
   - Zawiera plik `Dockerfile`, który buduje kontener symulujący działanie świateł drogowych.

2. **scada_controller**:

   - Zawiera skrypt w języku Python symulujący działanie sterownika SCADA (Supervisory Control and Data Acquisition).
   - Zawiera plik `Dockerfile`, który buduje kontener symulujący sterownik SCADA.

3. **suricata**:
   - Zawiera tylko plik `Dockerfile`, który buduje środowisko Suricata do monitoringu i zapobiegania zagrożeniom w sieci.

Plik `docker-compose.yaml` w głównym katalogu repozytorium uruchamia wszystkie te kontenery, zapewniając ich współpracę w celu stworzenia kompleksowego środowiska symulacyjnego.

## Jak Zacząć

### Wymagania

- Docker
- Docker Compose

### Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twojnick/twoje-repo.git
   cd twoje-repo
   ```
