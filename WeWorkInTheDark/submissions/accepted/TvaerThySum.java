import java.util.Scanner;

public class TvaerThySum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();

        while (n > 9) {
            long digitSum = 0;
            while (n > 0) {
                digitSum += n % 10;
                n /= 10;
            }
            n = digitSum;
        }
        System.out.println(n);
		sc.close();
    }
}
