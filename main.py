import serial
import pygame
import time

def connect_serial(port, baud):
    try:
        s = serial.Serial(port, baud, timeout = 0.1)
        time.sleep(2)
        print(f"Connected to {port}")
        return s
    except:
        return None

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
port = "COM4"
baud = 9600
ser = connect_serial("COM4", 9600)


angle = 0
orig_image = pygame.image.load("robot_image.jpg").convert()

running = True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if ser is None:
        ser = connect_serial(port, baud)
        if ser is None:
            time.sleep(2)
    else:
        try:
            lines_to_read = 10
            while ser.in_waiting > 0 and lines_to_read > 0:
                line = ser.readline()
                lines_to_read -= 1
                """
                This allows me to read every line coming from the Arduino ie where the data coming ends with \n, 
                and stores it in the variable line
                """

                clean_line = line.decode("utf-8", errors="ignore").strip()
                """
                The decode converts the bytes(because the date we are receiving are in byte form) to a string format
                the strip removes the /n/r at the end
                """
                data_list = clean_line.split(",")

                if len(data_list) == 6:
                    try:
                        angle = -float(data_list[5])
                    except ValueError:
                        print(",,,")

        except(serial.SerialException, OSError):
            print("Connection Lost!")
            if ser: ser.close()
            ser = None # This triggers system to reconnect from the condtion earlier that says if ser is None, reconnect

    screen.fill((30, 30, 30))
    rotated_image = pygame.transform.rotate(orig_image, angle)
    rotated_rect = rotated_image.get_rect(center=(300, 300))
    screen.blit(rotated_image, rotated_rect)
    pygame.display.flip()

    
pygame.quit()

