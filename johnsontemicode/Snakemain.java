package johnsontemicode;

import java.awt.EventQueue;
import javax.swing.JFrame;

public class Snakemain extends JFrame {

    public Snakemain() {
        
        initUI();
    }
    
    private void initUI() {
        
        add(new Board());
        
        setResizable(false);
        pack();
        
        setTitle("Snake Game");
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    public static void main(String[] args) {
        
        EventQueue.invokeLater(() -> {
            JFrame ex = new Snakemain();
            ex.setVisible(true);
        });
    }
}