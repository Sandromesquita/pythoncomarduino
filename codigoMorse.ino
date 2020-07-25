byte led=10;

void setup() {
  pinMode(led, OUTPUT);
}

void loop() {
 //LETRA "S" EM CODIGO MORSE
  for(int x=0; x<3; x++){
    digitalWrite(led, HIGH);
    delay(150);
    digitalWrite(led, LOW);
    delay(100);
  }

//LETRA "O" EM CODIGO MORSE
  for(int x=0; x<3; x++){
    digitalWrite(led, HIGH);
    delay(400);
    digitalWrite(led, LOW);
    delay(100);
  }

 //LETRA "S" EM CODIGO MORSE
  for(int x=0; x<3; x++){
    digitalWrite(led, HIGH);
    delay(150);
    digitalWrite(led, LOW);
    delay(100);
  }
delay(5000);
}
