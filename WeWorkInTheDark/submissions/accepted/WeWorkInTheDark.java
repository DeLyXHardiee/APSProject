import java.io.BufferedReader;
import java.io.InputStreamReader;

public class WeWorkInTheDark {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int x = Integer.parseInt(input[0]);
        int y = Integer.parseInt(input[1]);
        var fenwick2d = new FenwickTree2D(x, y);
        int n = Integer.parseInt(input[2]);
        for (int i = 0; i < n; i++){
            String[] guards = br.readLine().split(" ");
            int guards_x = Integer.parseInt(guards[0]);
            int guards_y = Integer.parseInt(guards[1]);
            int guards_amount = Integer.parseInt(guards[2]);
            fenwick2d.update(guards_x, guards_y, guards_amount);
        }
        int m = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < m; i++){
            String[] query = br.readLine().split(" ");
            switch (query[0]){
                case "eaglevision":
                    int ezio_x = Integer.parseInt(query[1]);
                    int ezio_y = Integer.parseInt(query[2]);
                    int ezio_range = Integer.parseInt(query[3]);
                    int x_lower_bound = Math.max(0, ezio_x-ezio_range);
                    int y_lower_bound = Math.max(0, ezio_y-ezio_range);
                    int x_upper_bound = Math.min(x, ezio_x+ezio_range);
                    int y_upper_bound = Math.min(y, ezio_y+ezio_range);
                    System.out.println(fenwick2d.queryRange(x_lower_bound, y_lower_bound, x_upper_bound, y_upper_bound));
                    continue;

                case "reinforcements":
                    int r_x = Integer.parseInt(query[1]);
                    int r_y = Integer.parseInt(query[2]);
                    int r_amount = Integer.parseInt(query[3]);
                    fenwick2d.update(r_x, r_y, r_amount);
                    continue;

                case "kill":
                    int k_x = Integer.parseInt(query[1]);
                    int k_y = Integer.parseInt(query[2]);
                    fenwick2d.setToZero(k_x, k_y);
                    continue;
            }
        }

    }

}

class FenwickTree2D {
    private int[][] tree;
    private int n, m;

    public FenwickTree2D(int n, int m) {
        this.n = n;
        this.m = m;
        tree = new int[n+2][m+2];
    }

    public void update(int x, int y, int val) {
        for (int i = x+1; i <= n; i += i & -i) {
            for (int j = y+1; j <= m; j += j & -j) {
                tree[i][j] += val;
            }
        }
    }

    public int query(int x, int y) {
        int sum = 0;
        for (int i = x+1; i > 0; i -= i & -i) {
            for (int j = y+1; j > 0; j -= j & -j) {
                sum += tree[i][j];
            }
        }
        return sum;
    }

    public int queryRange(int x1, int y1, int x2, int y2) {
        return query(x2, y2) - query(x1-1, y2) - query(x2, y1-1) + query(x1-1, y1-1);
    }

    public void setToZero(int x, int y) {
        int value = query(x, y) - query(x-1, y) - query(x, y-1) + query(x-1, y-1);
        update(x, y, -value);
    }
}