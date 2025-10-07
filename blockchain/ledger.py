#!/usr/bin/env python3

import hashlib
import json
import os
from datetime import datetime
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        return hashlib.sha256(
            str(self.index).encode() +
            str(self.timestamp).encode() +
            str(self.data).encode() +
            str(self.previous_hash).encode() +
            str(self.nonce).encode()
        ).hexdigest()
    
    def mine_block(self, difficulty):
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
    
    def create_genesis_block(self):
        return Block(0, str(datetime.now()), "Genesis Block", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
    def save_to_file(self, filename):
        os.makedirs('../blockchain/ledger', exist_ok=True)
        with open(f'../blockchain/ledger/{filename}', 'w') as f:
            chain_data = []
            for block in self.chain:
                chain_data.append({
                    'index': block.index,
                    'timestamp': block.timestamp,
                    'data': block.data,
                    'previous_hash': block.previous_hash,
                    'hash': block.hash,
                    'nonce': block.nonce
                })
            json.dump(chain_data, f, indent=2)

if __name__ == "__main__":
    # Create blockchain
    blockchain = Blockchain()
    
    # Add security log entries
    log_entries = [
        "Security scan initiated",
        "Quantum threat detection completed",
        "AI simulation finished",
        "Auto-response activated",
        "Neural analysis completed"
    ]
    
    for entry in log_entries:
        block = Block(
            len(blockchain.chain),
            str(datetime.now()),
            entry,
            ""
        )
        blockchain.add_block(block)
    
    # Save blockchain
    timestamp = int(time.time())
    blockchain.save_to_file(f'security_log_{timestamp}.json')
    
    print("Blockchain ledger created successfully")
    print(f"Chain valid: {blockchain.is_chain_valid()}")
