import random
from datetime import datetime

class HealthAssistant:
    def __init__(self):
        self.symptoms_db = {
            'fever': ['General Medicine', 'Take rest', 'Stay hydrated', 'Monitor temperature'],
            'cough': ['General Medicine', 'Use mask', 'Avoid cold drinks', 'Steam inhalation'],
            'headache': ['Neurology', 'Rest in dark room', 'Stay hydrated', 'Avoid screen time'],
            'chest pain': ['Cardiology', 'URGENT: Seek immediate medical attention', 'Avoid exertion'],
            'back pain': ['Orthopedics', 'Apply ice pack', 'Gentle stretching', 'Proper posture'],
            'child fever': ['Pediatrics', 'Monitor temperature', 'Keep child hydrated', 'Consult pediatrician']
        }
        
        self.preventive_tips = [
            "Wash hands regularly with soap and water",
            "Maintain proper hygiene",
            "Get adequate sleep (7-8 hours)",
            "Exercise regularly for 30 minutes",
            "Eat a balanced diet rich in fruits and vegetables",
            "Stay hydrated - drink 8-10 glasses of water daily",
            "Get annual health checkups",
            "Keep vaccinations up to date"
        ]
    
    def analyze_symptoms(self):
        """AI symptom checker"""
        print("\n" + "="*50)
        print("🤖 AI HEALTH ASSISTANT")
        print("="*50)
        
        print("\nDescribe your symptoms (comma-separated):")
        print("Example: fever, cough, headache")
        
        symptoms_input = input("\nYour symptoms: ").lower().strip()
        symptoms = [s.strip() for s in symptoms_input.split(',')]
        
        print("\n🤔 Analyzing your symptoms...")
        import time
        time.sleep(2)
        
        matches = []
        recommendations = []
        
        for symptom in symptoms:
            for key in self.symptoms_db:
                if key in symptom:
                    matches.append(key)
                    recommendations.extend(self.symptoms_db[key])
        
        if matches:
            print("\n📊 ANALYSIS RESULTS:")
            print("-" * 40)
            print(f"Detected symptoms: {', '.join(matches)}")
            
            # Department recommendation
            departments = set()
            for rec in recommendations:
                if rec in ['Cardiology', 'Neurology', 'Pediatrics', 'Orthopedics', 'General Medicine']:
                    departments.add(rec)
            
            if departments:
                print(f"\n🏥 Recommended Department: {', '.join(departments)}")
            
            print("\n💡 RECOMMENDATIONS:")
            unique_recs = list(dict.fromkeys(recommendations))
            for rec in unique_recs:
                if rec not in departments:
                    print(f"   • {rec}")
        else:
            print("\n📊 ANALYSIS RESULTS:")
            print("No specific symptoms detected. Consider a general checkup.")
        
        # Preventive tips
        print("\n🌟 PREVENTIVE HEALTH TIPS:")
        tips = random.sample(self.preventive_tips, min(3, len(self.preventive_tips)))
        for tip in tips:
            print(f"   • {tip}")
        
        return matches
    
    def suggest_services(self, user_history=None):
        """AI-based service suggestions based on user history"""
        print("\n" + "="*50)
        print("🎯 PERSONALIZED SERVICE SUGGESTIONS")
        print("="*50)
        
        services = {
            'Health Checkup Package': 'Comprehensive health screening at ₹999',
            'Dental Checkup': 'Free dental checkup this month',
            'Vaccination Drive': 'Flu vaccine available at subsidized rates',
            'Wellness Workshop': 'Free workshop on stress management',
            'Teleconsultation': 'Video consultation with specialists',
            'Home Healthcare': 'Nursing and physiotherapy at home',
            'Lab Tests': '20% off on all diagnostic tests',
            'Pharmacy Delivery': 'Free medicine delivery within hospital premises'
        }
        
        print("\n🎯 RECOMMENDED FOR YOU:")
        
        # AI-based recommendations
        if user_history:
            print("\nBased on your history:")
            if 'emergency' in user_history:
                print("   • Emergency response training available")
            if 'appointment' in user_history:
                print("   • Follow-up consultation recommended")
        
        print("\n📋 AVAILABLE SERVICES:")
        for service, desc in list(services.items())[:5]:
            print(f"   • {service}: {desc}")
        
        print("\n💡 TIP: Regular health checkups can detect issues early!")