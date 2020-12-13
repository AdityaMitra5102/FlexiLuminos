import java.io.*;
class Test
{
    static void on()
    {
        try
        {
            Process ec=Runtime.getRuntime().exec("python switchon.py");
            System.out.println("Turning on");
        }
        catch(Exception excep){}
    }
    
    static void off()
    {
        try
        {
            Process ec=Runtime.getRuntime().exec("python switchoff.py");
            System.out.println("Turning off");
        }
        catch(Exception excep){}
    }	    
}
