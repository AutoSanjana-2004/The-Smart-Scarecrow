#include <Servo.h>

Servo myservo; 

void setup() {
  myservo.attach(D0);
  pinMode(D2,INPUT);
  Serial.begin(9600);
  pinMode(D1,OUTPUT);
  pinMode(D3,INPUT);
  

}

void loop() {
  int x1=digitalRead(D0);
  int x2=digitalRead(D3);
  Serial.println(x1);
  Serial.println(x2);
  if(x1==0 && x2==0){
    digitalWrite(D1,HIGH);
    myservo.write(0);
    delay(1000);
    myservo.write(180);
    delay(1000);
  }
  else if(x1==0 && x2==1){
    digitalWrite(D1,HIGH);
    myservo.write(0);
    delay(1000);
  }
  else if(x1==1 && x2==0){
    digitalWrite(D1,HIGH);
    myservo.write(180);
    delay(1000);
  }
  else
  {
    digitalWrite(D1,LOW);
    myservo.write(90);
  }
  delay(2000);

}
