#!/usr/bin/env python3

from flask import Flask, render_template, jsonify, request
import json
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/scan')
def scan():
    # Run OMNIA-PRIV scan
    os.system('../omnia-priv.sh --full-scan')
    
    # Load latest results
    results = {}
    
    # Load quantum detection results
    if os.path.exists('../logs/quantum_detection.json'):
        with open('../logs/quantum_detection.json', 'r') as f:
            results['quantum'] = json.load(f)
    
    # Load AI simulation results
    if os.path.exists('../logs/ai_simulations.json'):
        with open('../logs/ai_simulations.json', 'r') as f:
            results['ai'] = json.load(f)
    
    # Load neural analysis results
    if os.path.exists('../logs/neural_analysis.json'):
        with open('../logs/neural_analysis.json', 'r') as f:
            results['neural'] = json.load(f)
    
    # Load metaverse intelligence
    if os.path.exists('../logs/metaverse_intel.json'):
        with open('../logs/metaverse_intel.json', 'r') as f:
            results['metaverse'] = json.load(f)
    
    return jsonify(results)

@app.route('/api/blockchain')
def blockchain():
    # Load blockchain data
    blocks = []
    for file in os.listdir('../blockchain/ledger'):
        if file.endswith('.json'):
            with open(f'../blockchain/ledger/{file}', 'r') as f:
                blocks.append(json.load(f))
    
    return jsonify(blocks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
