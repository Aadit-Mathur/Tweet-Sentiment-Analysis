import java.io.*;
import java.util.Scanner;

public class Java_Input_Sentiment{
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter tweet: ");
        String tweet = sc.nextLine();
        sc.close();

        ProcessBuilder pb = new ProcessBuilder("python", "Model_Call_for_Java.py", tweet);
        pb.redirectErrorStream(true);
        
        Process process = pb.start();

        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line;

        while((line = reader.readLine())!=null){
            System.out.println(line);
        }
    }
}