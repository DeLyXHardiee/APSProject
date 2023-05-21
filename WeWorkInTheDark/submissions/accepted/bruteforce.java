import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bruteforce {
    public static void main(String[] args) throws IOException {
        long startTime = System.currentTimeMillis();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputStr = br.readLine();
        String[] inputList = inputStr.split(" ");
        int x = Integer.parseInt(inputList[0]);
        int y = Integer.parseInt(inputList[1]);
        int[][] area = new int[x][y];
        int n = Integer.parseInt(inputList[2]);

        for (int i = 0; i < n; i++) {
            String[] guards = br.readLine().split(" ");
            int guards_x = Integer.parseInt(guards[0]);
            int guards_y = Integer.parseInt(guards[1]);
            int guards_amount = Integer.parseInt(guards[2]);
            area[guards_x][guards_y] += guards_amount;
            // System.out.println(guards_x + " " + guards_y + " updated: " + area[guards_x][guards_y]);
        }

        int m = Integer.parseInt(br.readLine().trim());

        for (int i = 0; i < m; i++) {
            String[] query = br.readLine().split(" ");
            String command = query[0];

            if (command.equals("e")) {
                int ezio_x = Integer.parseInt(query[1]);
                int ezio_y = Integer.parseInt(query[2]);
                int ezio_range = Integer.parseInt(query[3]);
                int x_lower_bound = Math.max(0, ezio_x - ezio_range);
                int y_lower_bound = Math.max(0, ezio_y - ezio_range);
                int x_upper_bound = Math.min(x - 1, ezio_x + ezio_range);
                int y_upper_bound = Math.min(y - 1, ezio_y + ezio_range);
                // String bounds = "Bounds: " + x_lower_bound + " " + y_lower_bound + " " + x_upper_bound + " " + y_upper_bound;
                // System.out.println(bounds);
                int amount = 0;
                for (int row = x_lower_bound; row <= x_upper_bound; row++) {
                    for (int col = y_lower_bound; col <= y_upper_bound; col++) {
                        amount += area[row][col];
                    }
                }
                System.out.println(amount);
            } else if (command.equals("r")) {
                int r_x = Integer.parseInt(query[1]);
                int r_y = Integer.parseInt(query[2]);
                int r_amount = Integer.parseInt(query[3]);
                area[r_x][r_y] += r_amount;
            } else if (command.equals("k")) {
                int k_x = Integer.parseInt(query[1]);
                int k_y = Integer.parseInt(query[2]);
                area[k_x][k_y] = 0;
            }
        }

        long endTime = System.currentTimeMillis();
        long elapsed_time = endTime - startTime;
        System.out.println("Elapsed time: " + elapsed_time + " milliseconds");
    }
}
