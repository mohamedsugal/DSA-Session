
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


        BinaryTree.FindPath(root, "minneapolis");;
        computeDistance();

//        FindPathIterativly(root);;




    }

      /*
        Recursive Solution
     */

    public static ArrayList<Object> RouteMiles = new ArrayList<>();

    public static void computeDistance(){
        int distance = 0;
        for(int i = 0; i < RouteMiles.size(); i++){
            int Mile = (int) RouteMiles.get(i);
            distance += Mile;
        }
        System.out.println();
        System.out.println("Distance - > "  + distance);
    }

    /*
        Prints the Path cities to the destination.
        FindPath : Stores Path using ArrayList Route
        Parameter : root -> Starting Location , City - > Destination.
     */


    public static void FindPath(Node root, String city){
        ArrayList<Object> Route = new ArrayList<>();
        if(!CheckPath(root, Route, city)) {
            System.out.println("No Path");
        }
        for (Object obj : Route){
            System.out.print(obj + " - > ");
        }
    }

    /*
        Returns Boolean:
        Parameter : root , ArrayList to Store Path and the destination.
        Static Method CheckPath : Check if
     */

    public static boolean CheckPath(Node root, ArrayList<Object> route, String city){

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

        if((CheckPath(root.left, route, city)) || (CheckPath(root.right, route, city))){
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
