import java.io.*;
public class Main
{
    public static void main(String args[])
    {
        //Process ec=Runtime.getRuntime().exec("sh /home/pi/Desktop/Program/run.sh");
        try
        {
            new Server().main();
        }
        catch(Exception excep)
        {
            main(args);
        }
    }
}