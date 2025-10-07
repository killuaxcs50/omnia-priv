FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    jq \
    docker.io \
    kubernetes-client \
    steghide \
    foremost \
    binwalk \
    volatility3 \
    chkrootkit \
    unhide \
    nmap \
    hydra \
    john \
    hashcat \
    wireshark \
    clamav \
    rkhunter \
    lynis \
    tor \
    proxychains \
    yara \
    suricata \
    snort \
    ossec \
    auditd \
    rsyslog \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p logs reports blockchain/ledger ai/models quantum neural generative metaverse

# Set permissions
RUN chmod +x omnia-priv.sh
RUN chmod +x quantum/detection.py
RUN chmod +x generative/attack_simulator.py
RUN chmod +x blockchain/ledger.py
RUN chmod +x neural/anomaly_detector.py
RUN chmod +x metaverse/intel_collector.py

# Expose port
EXPOSE 8080

# Run the application
CMD ["./omnia-priv.sh", "--full-scan"]
