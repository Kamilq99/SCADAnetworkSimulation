FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

RUN add-apt-repository -y ppa:oisf/suricata-stable && \
    apt-get update && \
    apt-get install -y suricata && \
    rm -rf /var/lib/apt/lists/*

COPY suricata.yaml /etc/suricata/suricata.yaml

CMD ["suricata", "-c", "/etc/suricata/suricata.yaml", "-i", "eth0"]