#include <Stepper.h>

const int passosPorVolta = 32;

char cmd = '0';
int passoMotor1 = 0;
boolean resetar = false; 

Stepper motor1(passosPorVolta, 2, 3, 4, 5);
Stepper motor2(passosPorVolta, 8, 9, 10, 11);

void setup() {
  motor1.setSpeed(1300);
  motor2.setSpeed(300);
  Serial.begin(9600);
}

void loop() {

  if (resetar == false) {
    if (Serial.available() > 0) {  
      cmd = Serial.read();        
      Serial.println(cmd);        

      if (cmd == '1') {
        motor1.step(200);//5
        passoMotor1++;
        Serial.print("Passo Motor 1: ");
      }

      if (cmd == '2') {
        motor2.step(-15);
        Serial.println("Motor 2 acionado.");
      }
    }
  }

  if (passoMotor1 == 50) {
    resetar = true;
  }

  if (resetar == true) {
    motor1.step(-5);
    passoMotor1--;
    if (passoMotor1 == 0) {
      resetar = false;
    }
  }

  delay(500);
}