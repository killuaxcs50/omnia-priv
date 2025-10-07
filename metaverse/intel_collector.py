#!/usr/bin/env python3

import requests
import json
import os
from datetime import datetime
import time
import random

class MetaverseIntelCollector:
    def __init__(self):
        self.platforms = {
            'decentraland': {
                'api_url': 'https://api.decentraland.org/v1',
                'threat_types': ['smart_contract_vuln', 'nft_theft', 'land_scam']
            },
            'sandbox': {
                'api_url': 'https://api.sandbox.game/v1',
                'threat_types': ['asset_theft', 'account_compromise', 'fraud']
            },
            'cryptovoxels': {
                'api_url': 'https://api.cryptovoxels.com/v1',
                'threat_types': ['parcel_scam', 'fake_marketplace', 'phishing']
            }
        }
    
    def scan_platform(self, platform_name):
        platform = self.platforms.get(platform_name)
        if not platform:
            return None
        
        # Simulate API call
        time.sleep(0.5)  # Simulate network delay
        
        # Generate random threat data
        threats = []
        for threat_type in platform['threat_types']:
            if random.random() > 0.7:  # 30% chance of each threat type
                threats.append({
                    'type': threat_type,
                    'severity': random.choice(['low', 'medium', 'high', 'critical']),
                    'confidence': random.uniform(0.5, 1.0),
                    'timestamp': str(datetime.now())
                })
        
        return {
            'platform': platform_name,
            'threats': threats,
            'scan_time': str(datetime.now())
        }
    
    def collect_intelligence(self):
        intelligence = []
        
        for platform_name in self.platforms.keys():
            print(f"Scanning {platform_name}...")
            platform_data = self.scan_platform(platform_name)
            if platform_data:
                intelligence.append(platform_data)
        
        return intelligence
    
    def analyze_threats(self, intelligence):
        threat_summary = {
            'total_platforms': len(intelligence),
            'total_threats': sum(len(data['threats']) for data in intelligence),
            'critical_threats': 0,
            'high_threats': 0,
            'platform_breakdown': {}
        }
        
        for data in intelligence:
            platform = data['platform']
            threats = data['threats']
            
            threat_summary['platform_breakdown'][platform] = len(threats)
            
            for threat in threats:
                if threat['severity'] == 'critical':
                    threat_summary['critical_threats'] += 1
                elif threat['severity'] == 'high':
                    threat_summary['high_threats'] += 1
        
        return threat_summary
    
    def generate_recommendations(self, threat_summary):
        recommendations = []
        
        if threat_summary['critical_threats'] > 0:
            recommendations.append("Critical threats detected - Immediate action required")
        
        if threat_summary['high_threats'] > 2:
            recommendations.append("Multiple high-severity threats - Prioritize investigation")
        
        for platform, count in threat_summary['platform_breakdown'].items():
            if count > 3:
                recommendations.append(f"High threat concentration on {platform} - Enhanced monitoring recommended")
        
        if not recommendations:
            recommendations.append("No significant threats detected - Maintain current security posture")
        
        return recommendations

if __name__ == "__main__":
    collector = MetaverseIntelCollector()
    
    # Collect intelligence
    print("Collecting metaverse threat intelligence...")
    intelligence = collector.collect_intelligence()
    
    # Analyze threats
    threat_summary = collector.analyze_threats(intelligence)
    
    # Generate recommendations
    recommendations = collector.generate_recommendations(threat_summary)
    
    # Save results
    os.makedirs('../logs', exist_ok=True)
    with open('../logs/metaverse_intel.json', 'w') as f:
        json.dump({
            'intelligence': intelligence,
            'summary': threat_summary,
            'recommendations': recommendations,
            'timestamp': str(datetime.now())
        }, f, indent=2)
    
    print("Metaverse intelligence collection completed")
    print(f"Total threats detected: {threat_summary['total_threats']}")
    print(f"Critical threats: {threat_summary['critical_threats']}")
    print("Recommendations:")
    for rec in recommendations:
        print(f"- {rec}")
