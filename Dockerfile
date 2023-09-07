# getting base image python
FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev libgl1-mesa-glx swig
CMD ["python", "app.py"]