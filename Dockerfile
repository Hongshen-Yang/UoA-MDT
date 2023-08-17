# getting base image python
FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev libgl1-mesa-glx swig
RUN pip install box2d-py box2d Box2D
RUN pip install git+https://github.com/AI4Finance-Foundation/FinRL.git
CMD ["python", "app.py"]