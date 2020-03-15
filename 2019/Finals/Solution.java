import java.io.*;
import java.util.*;

public class Solution {
    FastScanner in;
    PrintWriter out;

    enum Type{
        N,
        NO, 
        OK,
        M
    }

    class MyMatrix{
        public Cell[][] matrix;
        public Cell start;
        public Cell end;
        public MyMatrix(int rows, int cols){
            matrix = new Cell[rows][cols];
        }
        public void set(int i, int j, char c){
            switch(c){
                case 'N':
                    end = new Cell(i,j, Type.N);
                    matrix[i][j] = end;
                    break;
                case '#':
                    matrix[i][j] = new Cell(i,j,Type.NO);;
                    break;
                case '.':
                    matrix[i][j] = new Cell(i,j,Type.OK);
                    break;
                case 'M':
                    start = new Cell(i,j, Type.M);
                    matrix[i][j] = start;
                    break;
            }
        }

        public Cell getNorth(int i, int j){
            if (i - 1 < 0){
                return null;
            }
            return matrix[i - 1][j];
        }
        public Cell getSouth(int i, int j){
            if (i + 1 >= matrix.length){
                return null;
            }
            return matrix[i + 1][j];
        }
        public Cell getEast(int i, int j){
            if (j + 1 >= matrix[0].length){
                return null;
            }
            return matrix[i][j + 1];
        }
        public Cell getWest(int i, int j){
            if (j - 1 < 0){
                return null;
            }
            return matrix[i][j - 1];
        }
    }

    class Cell{
        public int row;
        public int col;
        public Type t;
        public Cell(int row, int col, Type t){
            this.row = row;
            this.col = col;
            this.t = t;
        }
    }

    boolean isN(Type t){
        return t == Type.N;
    }
    boolean isOk(Type t){
        return t == Type.OK;
    }
    boolean isM(Type t){
        return t == Type.M;
    }
    boolean isNo(Type t){
        return t == Type.NO;
    }

    List<Cell> getReachable(MyMatrix matrix){
        List<Cell> result = new ArrayList<>();
        boolean[][] reachable = new boolean[matrix.matrix.length][matrix.matrix[0].length];
        boolean[][] visited = new boolean[matrix.matrix.length][matrix.matrix[0].length];
        LinkedList<Cell> available = new LinkedList<>();   
        available.push(matrix.start);

        while(!available.isEmpty()){
            Cell el = available.pop();
            result.add(el);
            reachable[el.row][el.col] = true;
            visited[el.row][el.col] = true;
            Cell n = matrix.getNorth(el.row, el.col);
            Cell s = matrix.getSouth(el.row, el.col);
            Cell e = matrix.getEast(el.row, el.col);
            Cell w = matrix.getWest(el.row, el.col);
            if (n != null && !isNo(n.t) && !visited[n.row][n.col]){
                available.push(n);
            }

            if (s != null && !isNo(s.t) && !visited[s.row][s.col]){
                available.push(s);
            }

            if (e != null && !isNo(e.t) && !visited[e.row][e.col]){
                available.push(e);
            }
            if (w != null && !isNo(w.t) && !visited[w.row][w.col]){
                available.push(w);
            }
        }
        return result;
    }

    int solveCase(MyMatrix matrix){
        List<Cell> reachable = getReachable(matrix);
        if (!reachable.stream().anyMatch(t -> isN(t.t))){
            return 0;
        }

        out.println(reachable);
        return 1;
    }

    void solve() {
        int tc = in.nextInt();
        for (int t = 0; t < tc; t++) {
            int rows = in.nextInt();
            int cols = in.nextInt();
            MyMatrix matrix = new MyMatrix(rows, cols);
            Cell start = null;
            Cell end = null;
            for(int i = 0; i<rows; i++){
                String row = in.next();
                for(int j = 0; j<row.length(); j ++){
                    char c = row.charAt(j);
                    matrix.set(i, j, c);
                }
            }
            int sol = solveCase(matrix);
            out.println(String.format("Case #%d: %d", t + 1, sol));
        }
    }

    void run() {
        try {
            in = new FastScanner(new File("Solution.in"));
            out = new PrintWriter(new File("Solution.out"));

            solve();

            out.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    void runIO() {

        in = new FastScanner(System.in);
        out = new PrintWriter(System.out);

        solve();

        out.close();
    }

    class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(File f) {
            try {
                br = new BufferedReader(new FileReader(f));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        public FastScanner(InputStream f) {
            br = new BufferedReader(new InputStreamReader(f));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                String s = null;
                try {
                    s = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (s == null)
                    return null;
                st = new StringTokenizer(s);
            }
            return st.nextToken();
        }

        boolean hasMoreTokens() {
            while (st == null || !st.hasMoreTokens()) {
                String s = null;
                try {
                    s = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (s == null)
                    return false;
                st = new StringTokenizer(s);
            }
            return true;
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }
    }

    public static void main(String[] args) {
        new Solution().run();
    }
}