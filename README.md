# The-Smart-Scarecrow
An Edge-AI Drone Sentinel for Intelligent Crop Defense

**Project Name:** Rhythm  
**Domain:** IoT   
**Institution:** T John Institute of Technology 

---

## 📖 Overview
**The Smart Scarecrow** (codenamed *Rhythm*) is an intelligent crop defense system designed to mitigate post-planting yield loss. By moving intelligence to the "Edge," the system provides a scalable, autonomous, and conflict-free farming infrastructure that protects against animal raiding and human intrusion.

## 🚩 Problem Statement
Existing solutions like physical or electric fences, manual guarding, and traditional scarecrows are often ineffective or labor-intensive. 
**Crop Raiding**: Stray and wild animals (buffaloes, goats, wild boars) cause significant yield loss.
**Intrusion**: Manual theft and human intrusion lead to further crop depletion.

## 🚀 Proposed Solution
Our system operates through a five-stage intelligent protocol:

1.  **Ground-Level Detection**: PIR sensors detect animals or humans at the perimeter.
2.  **Autonomous Aerial Verification**: Detection triggers a drone that classifies the intruder using TinyML.
3.  **Tiered Deterrent Response**: Targeted action based on classification:
    * **Domestic Animals**: Deterred via predator sounds.
    * **Wild Animals**: Deterred via predator sounds + Notification to rescue teams.
    * **Humans**: Triggered alarms + Notification to the owner.
4.  **Edge Analytics**: Local processing recognizes patterns to predict animal entry times.
5.  **Smart Notification Protocol**: Farmers and rescue teams are notified instantly based on the threat level.

## 📊 System Architecture
The workflow follows this logic:
**Start** → **Sensor Triggered (PIR)** → **Drone Activation** → **Capture & Classify (TinyML)** → **Tiered Response** → **Data Analysis**.

## 🛠️ Technology Stack

### Hardware Components 
* **Microcontrollers**: Arduino, ESP32 
* **Sensors**: PIR motion sensor, Ultrasonic sensor, GPS module 
* **Actuators**: High-decibel Piezo Buzzers, High-intensity Strobe LEDs

### AI and Software 
* **Development Environment**: Arduino IDE (C++) 
* **TinyML Framework**: Edge Impulse 
* **Computer Vision**: OpenCV and pre-trained models 

## 📈 Execution and Scalability 
* **Swarm Expansion**: Scaling from a single drone for 2-acre farms to synchronized swarms for 200+ acre plantations.
* **Community-Level Intelligence**: Enabling data sharing between neighboring farms to track migration patterns.
* **Cost-Effective Production**: Utilizing specialized AI chips instead of expensive computers to ensure affordability.

## 👥 Team Members 
* Anushree S G 
* Chaitra H G 
* Niveditha V 
* Sanjana B K 

---
> "The Smart Scarecrow isn't just a gadget; it's a scalable infrastructure... building the future of Conflict-Free Farming." 
