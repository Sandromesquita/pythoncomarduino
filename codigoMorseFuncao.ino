//byte led = 10;
int y=0;

void setup() {
  pinMode(10, OUTPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  piscaLed(150, 100, 10, 3);
  Serial.print("Escrevendo S.");
  piscaLed(400, 100, 10, 3);
  Serial.print("O.");
  piscaLed(150, 100, 10, 3);
  Serial.println("S");
  Serial.println("Enviado S.O.S. " + String(y) + " vez.");
  Serial.print("Enviado S.O.S. ");
  Serial.print(y);
  Serial.println(" vezes.");
  /* piscaLed(150,100, 13, 10);
    Serial.print("Escrevendo S.");
    piscaLed(400,100, 13, 10);
    Serial.print("O.");
    piscaLed(150,100, 13, 10);
    Serial.println("S");
    Serial.println("Enviado S.O.S.!");*/
}

void piscaLed(int tl, int td, byte porta, int qtd) {
  for (int x = 0; x < qtd; x++) {
    digitalWrite(porta, HIGH);
    delay(tl);
    digitalWrite(porta, LOW);
    delay(td);
  }
  y++;
  return y;
}
