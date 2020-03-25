int analogPin = A7;
void setup() 
{
  Serial.begin(9600);
  pinMode(analogPin,INPUT);
}
void loop() 
{
  long sum = 0;
  for(int i = 0 ; i < 500 ; i++)
  {
    sum += analogRead(analogPin);
  }
  long temp = sum/500;
  Serial.println(temp);
}
