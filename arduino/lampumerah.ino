
int M[4] = {0, 3, 6, 9};
int K[4] = {0, 2, 5, 8};
int H[4] = {0, 1, 4, 7};


void transisi(int a, int b){
  digitalWrite(H[a], LOW);
  delay(500);
  digitalWrite(K[a], HIGH);
  delay(500);
  digitalWrite(K[a], LOW);
  digitalWrite(M[a], HIGH);
  delay(500);
  digitalWrite(M[b], LOW);
  digitalWrite(K[b], HIGH);
  digitalWrite(H[b], LOW);
  delay(500);
  digitalWrite(K[b], LOW);
  digitalWrite(H[b], HIGH);
}

void setup() {
  for(int i = 1; i < 4; i++){
    pinMode(M[i], OUTPUT);
    pinMode(K[i], OUTPUT);
    pinMode(H[i], OUTPUT);
  }
}

void loop() {
  transisi(3, 1);
  delay(3000);
  transisi(1, 2);
  delay(3000);
  transisi(2, 3);
  delay(3000);
}
