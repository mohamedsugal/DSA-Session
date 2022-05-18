import java.util.ArrayList;

public class BinaryTree {

    public static void main(String[] args) {
        City seattle  =  new City("Seattle", 0);
        City denver  =  new City("denver", 1305);
        City miami  =  new City("miami", 2064);
        City LosAngelos  =  new City("Los Angelos", 1016);
        City dallas  =  new City("dallas", 1435);
        City minneapols  =  new City("minneapolis", 990);
        City newyork  =  new City("newyork", 2401);
        City boston  =  new City("boston", 216);

        Node root = new Node(seattle);

        // Left Childen

        root.left = new Node(denver);
        root.left.left = new Node(miami);
        root.left.right = new Node(LosAngelos);
        root.left.right.left = new Node(dallas);
        root.left.right.left.right = new Node(minneapols);

        // Right

        root.right = new Node(newyork);
        root.right.right = new Node(boston);

        BinaryTree.FindPath(root, "dallas");

    }


    public static void FindPath(Node root, String city){

    }


    public  static boolean CheckPath(Node root, ArrayList<Object> arr, String city){

        return false;


    }
}
