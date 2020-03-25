void setup() 
{
  Serial.begin(9600);
  pinMode(A7,INPUT);
}
void loop() 
{
  long sum = 0;
  for(int i = 0 ; i < 500 ; i++)
  {
    sum += analogRead(A7);
  }
  long temp = sum/500;
  Serial.println(temp);
}
