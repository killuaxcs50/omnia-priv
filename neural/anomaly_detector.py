#!/usr/bin/env python3

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import json
import os

class AnomalyDetector:
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = self.build_model()
        self.threshold = 0.1
    
    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(20,)),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(8, activation='relu'),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(20, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='mse')
        return model
    
    def generate_normal_data(self, samples=1000):
        # Generate normal system behavior data
        data = np.random.normal(0, 1, (samples, 20))
        return data
    
    def generate_anomalous_data(self, samples=100):
        # Generate anomalous data
        data = np.random.normal(3, 1, (samples, 20))
        return data
    
    def train(self):
        # Generate training data
        normal_data = self.generate_normal_data()
        
        # Normalize data
        normal_data_scaled = self.scaler.fit_transform(normal_data)
        
        # Train autoencoder
        self.model.fit(
            normal_data_scaled, normal_data_scaled,
            epochs=50,
            batch_size=32,
            verbose=0
        )
        
        # Calculate threshold
        reconstructions = self.model.predict(normal_data_scaled)
        mse = np.mean(np.power(normal_data_scaled - reconstructions, 2), axis=1)
        self.threshold = np.mean(mse) + 3 * np.std(mse)
    
    def detect_anomalies(self, data):
        # Scale data
        data_scaled = self.scaler.transform(data)
        
        # Get reconstructions
        reconstructions = self.model.predict(data_scaled)
        
        # Calculate MSE
        mse = np.mean(np.power(data_scaled - reconstructions, 2), axis=1)
        
        # Detect anomalies
        anomalies = mse > self.threshold
        
        return {
            'anomalies': anomalies.tolist(),
            'mse_scores': mse.tolist(),
            'threshold': self.threshold
        }
    
    def analyze_system(self):
        # Generate test data (mix of normal and anomalous)
        normal_data = self.generate_normal_data(500)
        anomalous_data = self.generate_anomalous_data(50)
        test_data = np.vstack([normal_data, anomalous_data])
        
        # Detect anomalies
        results = self.detect_anomalies(test_data)
        
        return {
            'total_samples': len(test_data),
            'anomalies_detected': sum(results['anomalies']),
            'detection_rate': sum(results['anomalies']) / len(test_data),
            'average_mse': np.mean(results['mse_scores']),
            'max_mse': max(results['mse_scores'])
        }

if __name__ == "__main__":
    detector = AnomalyDetector()
    
    # Train the detector
    print("Training neural network...")
    detector.train()
    
    # Analyze system
    print("Analyzing system for anomalies...")
    analysis = detector.analyze_system()
    
    # Save results
    os.makedirs('../logs', exist_ok=True)
    with open('../logs/neural_analysis.json', 'w') as f:
        json.dump(analysis, f, indent=2)
    
    print("Neural network analysis completed")
    print(f"Anomalies detected: {analysis['anomalies_detected']}/{analysis['total_samples']}")
    print(f"Detection rate: {analysis['detection_rate']:.2%}")
