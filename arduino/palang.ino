#include <Servo.h>

Servo myServo;

int servo = 1;
int DistanceMin = 10;
int sensor[2] = {0, 5, 6};
int led[3] = {0, 8, 9}; // 8 merah 9 hijau

void setup() {
  myServo.attach(servo);
  pinMode(sensor[1], OUTPUT); // trigger
  pinMode(sensor[2], OUTPUT); // echo
  myServo.write(0);
  for(int i = 1; i <= 3; i++){
    pinMode(led[i], OUTPUT); // led
  }
  digitalWrite(led[1], HIGH);
  digitalWrite(led[2], LOW);
}

void loop() {
  long duration, distance;

  digitalWrite(sensor[1], LOW);
  delayMicroseconds(2);
  digitalWrite(sensor[1], HIGH);
  delayMicroseconds(10);
  digitalWrite(sensor[1], LOW);

  duration = pulseIn(sensor[2], HIGH);
  distance = duration * 0.034 / 2;

  if(distance < DistanceMin){
    myServo.write(120);
    digitalWrite(led[1], LOW);
    digitalWrite(led[2], HIGH);
  } else {
    myServo.write(-120);
    digitalWrite(led[1], HIGH);
    digitalWrite(led[2], LOW);
  }
}
