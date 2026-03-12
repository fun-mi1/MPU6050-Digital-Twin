#include "Wire.h"
#include <MPU6050_light.h>

MPU6050 mpu(Wire);

long timer = 0;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  byte status = mpu.begin();
  Serial.print(F("MPU6050 status: "));
  Serial.println(status);
  while(status!=0){ } // stop everything if could not connect to MPU6050
  
  Serial.println(F("Calculating offsets, do not move MPU6050"));
  delay(1000);
  mpu.calcOffsets(true,true); // gyro and accelero
  Serial.println("Done!\n");
  
}

void loop() {
  mpu.update();

  if(millis() - timer > 20){ // print data every second 
    Serial.print(mpu.getGyroX()); Serial.print(",");
    Serial.print(mpu.getGyroY()); Serial.print(",");
    Serial.print(mpu.getGyroZ()); Serial.print(",");
    Serial.print(mpu.getAngleX()); Serial.print(",");
    Serial.print(mpu.getAngleY()); Serial.print(",");
    Serial.println(mpu.getAngleZ());
    timer = millis();
  }

}
