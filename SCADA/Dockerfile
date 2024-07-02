FROM python:3.9-slim

WORKDIR /app

COPY scada_controller.py /app/

RUN pip install requests

CMD ["python", "scada_controller.py"]