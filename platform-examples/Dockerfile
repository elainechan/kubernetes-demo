FROM python:3.7
COPY app.py .
COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install -r ./requirements.txt
CMD ["python", "app.py"]
# For the exposed pod script; prevents container from pausing
RUN ["/bin/sh", "-ec", "sleep 1000"]