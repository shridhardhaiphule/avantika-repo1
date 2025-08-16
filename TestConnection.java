import java.sql.Connection;
import java.sql.DriverManager;

public class TestConnection {
    public static void main(String[] args) {
        try {

            Class.forName("oracle.jdbc.OracleDriver");

            String url = "jdbc:oracle:thin:@localhost:1521:xe";
            String user = "system";
            String password = "system";

            Connection conn = DriverManager.getConnection(url, user, password);

            if (conn != null) {
                System.out.println("✅ Connected successfully!");
                conn.close();
            } else {
                System.out.println("❌ Connection failed!");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
