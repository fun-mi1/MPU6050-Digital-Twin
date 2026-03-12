# Simple MPU6050 Digital Twin

A real-time visualizer that syncs a physical MPU6050 sensor with a 2D image in Python. This project demonstrates the concept of a **Digital Twin** by mapping the Z-axis (Yaw) of the gyroscope to a Pygame interface.

## Features
- **Real-time Rotation:** 1:1 mapping of sensor angle to screen image.
- **Auto-Reconnect:** System automatically detects and reconnects if the USB cable is unplugged.
- **Buffer Management:** Prevents lag by clearing old sensor data and focusing on the most recent "now."

## Tech Stack
- **Hardware:** Arduino Uno, MPU6050 Accelerometer/Gyro.
- **Software:** Python 3, Pygame, PySerial.

## How to Use
1. Upload the code in `/arduino` to your board.
2. Ensure your board is on `COM4` (or update the `port` variable in `main.py`).
3. Install dependencies: `pip install pygame pyserial`
4. Run `python python/main.py`.
