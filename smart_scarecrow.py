import airsim
import time
import random

# Connect to drone
client = airsim.MultirotorClient()
client.confirmConnection()

# Define zones
zones = {
    "A": (10, 0, -5),
    "B": (0, 10, -5),
    "C": (-10, 0, -5),
    "D": (0, -10, -5)
}
zone = random.choice(["A", "B", "C", "D"])
print(f"📡 Sensor triggered in Zone {zone}")
# Get coordinates of triggered zone
target = zones[zone]

print(f"🚁 Drone moving to Zone {zone}...")

# Enable control and arm drone
client.enableApiControl(True)
client.armDisarm(True)

# Takeoff
client.takeoffAsync().join()
time.sleep(2)

# Move to selected zone
client.moveToPositionAsync(target[0], target[1], target[2], 5).join()
# Capture image from drone camera
print("📷 Capturing image...")

responses = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)
])

if responses:
    response = responses[0]

    # Convert to numpy array
    import numpy as np
    import cv2

    img1d = np.frombuffer(response.image_data_uint8, dtype=np.uint8)
    img = img1d.reshape(response.height, response.width, 3)

    # Save image
    cv2.imwrite("zone_capture.png", img)

    print("✅ Image captured and saved as zone_capture.png")
else:
    print("❌ Failed to capture image")