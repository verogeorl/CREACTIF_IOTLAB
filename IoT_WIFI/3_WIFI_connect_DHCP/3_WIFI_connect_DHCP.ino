#include <ESP8266WiFi.h>

const char* ssid = "LAPTOP-VG";
const char* password = "80fK250:";
const char* ahostname = "vika";

void setup() {
  Serial.begin(115200);
  delay(10);

  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.hostname(ahostname);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println(WiFi.localIP());
}

void loop() {
  WiFi.printDiag(Serial);
  Serial.print("MAC Address: ");
  Serial.print(WiFi.macAddress());
   Serial.print("\n");
  Serial.print("Host name ");
  Serial.print(ahostname);
  Serial.print("\n");
  Serial.print("ESP IP address ");
  Serial.println(WiFi.localIP());
  Serial.print("AP subnet mask: ");
  Serial.println(WiFi.subnetMask());
  Serial.print("AP gateway: ");
  Serial.println(WiFi.gatewayIP());
  delay(10000);
}
