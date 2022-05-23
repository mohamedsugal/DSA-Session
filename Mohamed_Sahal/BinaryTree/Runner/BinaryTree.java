
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
        //Node
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


        BinaryTree.findPath(root, "minneapolis");
        computeDistance();

//        FindPathIterativly(root);;




    }

      /*
        Recursive Solution
     */

    public static ArrayList<Integer> routeMile = new ArrayList<>();

    public static void computeDistance(Node root, City){
        int distance = 0;
        for(int i = 0; i < routeMile.size(); i++){
            int mile = (int) routeMile.get(i);
            distance += mile;
        }
        System.out.println();
        System.out.println("Distance - > "  + distance);
    }

    /*
        Prints the Path cities to the destination.
        FindPath : Stores Path using ArrayList Route
        Parameter : root -> Starting Location , City - > Destination.
     */


    public static void findPath(Node root, String city){
        ArrayList<String> route = new ArrayList<>();
        if(!checkPath(root, route, city)) {
            System.out.println("No Path");
        }
        for (String str : route){
            System.out.print(str + " - > ");
        }
    }

    /*
        Returns Boolean:
        Parameter : root , ArrayList to Store Path and the destination.
        Static Method CheckPath : Check if
     */

    public static boolean checkPath(Node root, ArrayList<String> route, String city){

        if(root == null) {  // Check if root is Empty
            return false;
        }
        route.add(root.city.getCityName());  // If not Empty add root to the Route List


        if(root.city.getCityName().equals(city) ) {
            RouteMiles.add(root.city.getMiles());
            return true;
            // If root city name is equal to city return true;
        }
        // We recursively Check Left and Right of the tree to Check if City Exists.

        if((checkPath(root.left, route, city)) || (checkPath(root.right, route, city))){
            RouteMiles.add(root.city.getMiles());
            return true;
        }


        route.remove(route.size()-1);
        return false;


    }


    /*
        Iteration Solution
     */


}
