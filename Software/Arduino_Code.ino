// Smart Priority-Based Load Management
// Author: GURUPRASATH K C

const int criticalLoad = 2;
const int essentialLoad = 3;
const int nonCriticalLoad = 4;
const int voltagePin = A0;
float voltageThreshold = 220.0;

void setup() {
  pinMode(criticalLoad, OUTPUT);
  pinMode(essentialLoad, OUTPUT);
  pinMode(nonCriticalLoad, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  float voltage = analogRead(voltagePin)*(5.0/1023.0)*50;
  Serial.println(voltage);
  if(voltage < voltageThreshold){
    digitalWrite(nonCriticalLoad, LOW);
    digitalWrite(essentialLoad, HIGH);
    digitalWrite(criticalLoad, HIGH);
  } else {
    digitalWrite(nonCriticalLoad, HIGH);
    digitalWrite(essentialLoad, HIGH);
    digitalWrite(criticalLoad, HIGH);
  }
  delay(1000);
}
