int LDRPin = A0;
int LDRValue = 0;
int streetlight = 7;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LDRPin, INPUT);
  pinMode(streetlight, OUTPUT);
  Serial.print("<Information>:");
  Serial.print("\n");  

}

void loop() {
  // put your main code here, to run repeatedly:
  LDRValue = analogRead(LDRPin);
  Serial.print("LDRValue: ");
  Serial.println(LDRValue);

  if(LDRValue < 700){
    Serial.println("No light. LED ON");
    digitalWrite(streetlight, HIGH);
    delay(100);
  }
  else{
    Serial.println("Light! LED OFF");
    digitalWrite(streetlight, LOW);
    delay(100);
  }

}
