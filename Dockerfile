FROM python:3.9-slim

# install system dependencies
RUN apt-get update && apt-get install -y \
    libpcap-dev \
    && rm -rf /var/lib/apt/lists/*

# define workdir on system
WORKDIR /app

# copy project files to system
COPY . .

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# command to start application
CMD ["python", "packet_sniffer.py"]
