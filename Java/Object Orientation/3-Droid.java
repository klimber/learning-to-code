/* Este programa simula um droid que consome bateria e voa. */

public class Droid{
  
  int batteryLevel;
  
  public Droid(){
    batteryLevel = 100;
  }
  
  public void activate(){
    System.out.println("Activated. How can I help you?");
    batteryLevel = batteryLevel - 5;
    System.out.println("Battery level: " + batteryLevel + " percent.");
  }
  
  public void chargeBattery(int hours){
    System.out.println("Droid charging...");
    batteryLevel = batteryLevel + (hours * 5);
    if(batteryLevel > 100){
      batteryLevel = 100;
    }
    System.out.println("Battery level: " + batteryLevel);
  }
  
  public int checkBatteryLevel(){
    System.out.println("Battery Level: " + batteryLevel);
    return batteryLevel;    
  }
  
  public void hover(int feet){
    if (feet > 2){
      System.out.println("Error! I cannot hover above 2 feet.");
    } else {
      System.out.println("Hovering...");
      batteryLevel = batteryLevel - 20;
      System.out.println("Battery Level: " + batteryLevel);
    }
  }
  
  public static void main (String[] args){
    Droid myDroid = new Droid();
    myDroid.activate();
    myDroid.chargeBattery(5);
    myDroid.hover(2);
    
  }
}
