#!/bin/bash

# OMNIA-PRIV Setup Script
# This script sets up the complete OMNIA-PRIV environment

echo -e "${PURPLE}"
cat << 'BANNER'
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║                OMNIA-PRIV Setup Script                  ║
║                                                          ║
║        Quantum-Inspired Security Platform               ║
║                   AI-Powered Defense                    ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
BANNER
echo -e "${NC}"

# Check if run as root
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}[!] Please run as root${NC}"
    exit 1
fi

# Update system
echo -e "${YELLOW}[+] Updating system...${NC}"
apt update && apt upgrade -y

# Install dependencies
echo -e "${YELLOW}[+] Installing dependencies...${NC}"
apt install -y \
    python3 python3-pip python3-venv \
    curl wget git jq \
    build-essential \
    docker.io docker-compose \
    kubernetes-client \
    ethereum parity \
    steghide foremost binwalk \
    volatility3 chkrootkit unhide \
    nmap metasploit-framework \
    sqlmap hydra john hashcat \
    wireshark tcpdump \
    clamav rkhunter \
    lynis chkrootkit \
    openvpn wireguard \
    tor proxychains \
    yara suricata \
    snort ossec \
    auditd rsyslog \
    libssl-dev libffi-dev \
    python3-dev

# Install Python packages
echo -e "${YELLOW}[+] Installing Python packages...${NC}"
pip3 install --upgrade pip
pip3 install \
    qiskit pennylane cirq \
    tensorflow torch scikit-learn \
    transformers pandas numpy matplotlib \
    web3 py-solc-x \
    requests beautifulsoup4 \
    flask fastapi uvicorn \
    jupyter notebook

# Create virtual environment
echo -e "${YELLOW}[+] Creating virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate

# Install additional packages in venv
pip install -r requirements.txt

# Set up directories
echo -e "${YELLOW}[+] Setting up directories...${NC}"
mkdir -p logs reports blockchain/ledger ai/models quantum neural generative metaverse

# Initialize AI models
echo -e "${YELLOW}[+] Initializing AI models...${NC}"
python3 -c "
import tensorflow as tf
from qiskit import QuantumCircuit
import numpy as np

# Create quantum neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy')
model.save('ai/models/quantum_model.h5')
print('[+] Quantum AI models initialized')
"

# Initialize blockchain
echo -e "${YELLOW}[+] Initializing blockchain...${NC}"
cat > blockchain/ledger/genesis.json << 'EOF'
{
    "genesis_block": {
        "timestamp": "$(date -Iseconds)",
        "nonce": 0,
        "previous_hash": "0",
        "transactions": []
    }
}
EOF

# Set up permissions
echo -e "${YELLOW}[+] Setting up permissions...${NC}"
chmod +x omnia-priv.sh
chmod +x quantum/detection.py
chmod +x generative/attack_simulator.py
chmod +x blockchain/ledger.py
chmod +x neural/anomaly_detector.py
chmod +x metaverse/intel_collector.py

# Create systemd service
echo -e "${YELLOW}[+] Creating systemd service...${NC}"
cat > /etc/systemd/system/omnia-priv.service << 'EOF'
[Unit]
Description=OMNIA-PRIV Quantum Security Platform
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$(pwd)
ExecStart=$(pwd)/omnia-priv.sh --full-scan
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Enable service
systemctl daemon-reload
systemctl enable omnia-priv

# Create cron job for daily scans
echo -e "${YELLOW}[+] Setting up cron job...${NC}"
(crontab -l 2>/dev/null; echo "0 2 * * * $(pwd)/omnia-priv.sh --full-scan") | crontab -

# Complete setup
echo -e "${GREEN}[+] Setup completed successfully!${NC}"
echo -e "${GREEN}[+] To start OMNIA-PRIV, run: sudo ./omnia-priv.sh --full-scan${NC}"
echo -e "${GREEN}[+] To enable the service, run: sudo systemctl start omnia-priv${NC}"cd
