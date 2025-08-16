import java.awt.*;
import java.sql.*;
import javax.swing.*;      
import javax.swing.table.DefaultTableModel; 

public class ContactSystem extends JFrame {

    Connection con;
    PreparedStatement pst;

    JTextField idBox, nameBox, phoneBox, ageBox;
    JButton saveBtn, viewBtn, updateBtn, deleteBtn;

    public ContactSystem() {
        setTitle("Contact Management System");

        connect();

        setLayout(new GridLayout(6, 2, 10, 10));

        add(new JLabel("ID (for Update/Delete):"));
        idBox = new JTextField();
        add(idBox);

        add(new JLabel("Name:"));
        nameBox = new JTextField();
        add(nameBox);

        add(new JLabel("Phone:"));
        phoneBox = new JTextField();
        add(phoneBox);

        add(new JLabel("Age:"));
        ageBox = new JTextField();
        add(ageBox);

        saveBtn = new JButton("Save");
        add(saveBtn);

        updateBtn = new JButton("Update");
        add(updateBtn);

        deleteBtn = new JButton("Delete");
        add(deleteBtn);

        viewBtn = new JButton("View Contacts");
        add(viewBtn);

        saveBtn.addActionListener(e -> saveContact());

        updateBtn.addActionListener(e -> updateContact());

        deleteBtn.addActionListener(e -> deleteContact());

        viewBtn.addActionListener(e -> viewContacts());

        setSize(600, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    public void connect() {
        try {
            Class.forName("oracle.jdbc.OracleDriver");
            con = DriverManager.getConnection(
                "jdbc:oracle:thin:@localhost:1521:XE",
                "system",
                "system"
            );
            System.out.println("✅ Database connected successfully!");
        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(null, "Database connection failed!");
        }
    }

    public void saveContact() {
        try {
            String name = nameBox.getText();
            String phone = phoneBox.getText();
            int age = Integer.parseInt(ageBox.getText());

            pst = con.prepareStatement("INSERT INTO contacts (id, name, phone, age) VALUES (contacts_seq.nextval, ?, ?, ?)");
            pst.setString(1, name);
            pst.setString(2, phone);
            pst.setInt(3, age);
            pst.executeUpdate();

            JOptionPane.showMessageDialog(this, "✅ Contact saved!");
            clearFields();

        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error: " + e.getMessage());
        }
    }

    public void updateContact() {
        try {
            int id = Integer.parseInt(idBox.getText());
            String name = nameBox.getText();
            String phone = phoneBox.getText();
            int age = Integer.parseInt(ageBox.getText());

            pst = con.prepareStatement("UPDATE contacts SET name=?, phone=?, age=? WHERE id=?");
            pst.setString(1, name);
            pst.setString(2, phone);
            pst.setInt(3, age);
            pst.setInt(4, id);

            int rows = pst.executeUpdate();
            if (rows > 0) {
                JOptionPane.showMessageDialog(this, "✅ Contact updated!");
            } else {
                JOptionPane.showMessageDialog(this, "⚠️ Contact ID not found!");
            }
            clearFields();

        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error: " + e.getMessage());
        }
    }

    public void deleteContact() {
        try {
            int id = Integer.parseInt(idBox.getText());

            pst = con.prepareStatement("DELETE FROM contacts WHERE id=?");
            pst.setInt(1, id);

            int rows = pst.executeUpdate();
            if (rows > 0) {
                JOptionPane.showMessageDialog(this, "🗑️ Contact deleted!");
            } else {
                JOptionPane.showMessageDialog(this, "⚠️ Contact ID not found!");
            }
            clearFields();

        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error: " + e.getMessage());
        }
    }

    public void viewContacts() {
        try {
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM contacts ORDER BY id");

            // Table model
            String[] columns = {"ID", "Name", "Phone", "Age"};
            DefaultTableModel model = new DefaultTableModel(columns, 0);

            while (rs.next()) {
                Object[] row = {
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getString("phone"),
                    rs.getInt("age")
                };
                model.addRow(row);
            }

            JTable table = new JTable(model);
            JScrollPane scroll = new JScrollPane(table);

            JOptionPane.showMessageDialog(this, scroll, "Contacts List", JOptionPane.INFORMATION_MESSAGE);

        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error: " + e.getMessage());
        }
    }

    public void clearFields() {
        idBox.setText("");
        nameBox.setText("");
        phoneBox.setText("");
        ageBox.setText("");
        nameBox.requestFocus();
    }

    public static void main(String[] args) {
        new ContactSystem();
    }
}
