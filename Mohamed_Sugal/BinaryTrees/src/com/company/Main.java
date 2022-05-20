package com.company;

import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) {
	// write your code here
        TreeNode flights = new TreeNode("Seattle");
        flights.left = new TreeNode("Denver");
        flights.right = new TreeNode("New York");
        flights.right.right = new TreeNode("Boston");
        flights.left.left = new TreeNode("Miami");
        flights.left.right = new TreeNode("Los Angeles");
        flights.left.right.left = new TreeNode("Dallas");
        flights.left.right.left.right = new TreeNode("Minneapolis");

        System.out.println(findCityDestination(flights, "Dallas"));

        TreeNode flightsDistance = new TreeNode("Seattle", 0);
        flightsDistance.left = new TreeNode("Denver", 1305);
        flightsDistance.right = new TreeNode("New York", 2401);
        flightsDistance.right.right = new TreeNode("Boston", 216);
        flightsDistance.left.left = new TreeNode("Miami", 2064);
        flightsDistance.left.right = new TreeNode("Los Angles", 1016);
        flightsDistance.left.right.left = new TreeNode("Dallas", 1435);
        flightsDistance.left.right.left.right = new TreeNode("Minneapolis", 990);

        System.out.println(findTotalFlightDistance(flightsDistance, "Dallas"));
        System.out.println(findTotalDistance(flightsDistance, "Dallas"));
    }

    private static boolean findCityDestination(TreeNode startCity, String destinationCity) {
        if (startCity == null) {
            return false;
        }
        if (startCity.cityName.equals(destinationCity)) {
            return true;
        }
        return findCityDestination(startCity.left, destinationCity) ||
                findCityDestination(startCity.right, destinationCity);
    }

    private static int findTotalFlightDistance(TreeNode startCity, String endCity) {
        int[] totalDistance = {0};
        getDistance(startCity, endCity, totalDistance, 0);
        return totalDistance[0];
    }

    private static void getDistance(TreeNode currCity, String endCity, int[] totalDistance, int currDistance) {
        if (currCity == null) {
            return;
        }
        if (currCity.cityName.equals(endCity)) {
            totalDistance[0] = currDistance + currCity.distance;
            return;
        }
        getDistance(currCity.left, endCity, totalDistance, currDistance + currCity.distance);
        getDistance(currCity.right, endCity, totalDistance, currDistance + currCity.distance);
    }

    private static int findTotalDistance(TreeNode startCity, String endCity) {
        int totalDistance = 0;
        Deque<Pair> stack = new ArrayDeque<>();
        stack.offerLast(new Pair(startCity, 0));

        while (!stack.isEmpty()) {
            totalDistance = stack.peekLast().dist;
            TreeNode currCity = stack.pollLast().node;

            if (currCity.cityName.equals(endCity)) {
                return totalDistance + currCity.distance;
            }
            if (currCity.right != null) {
                stack.offerLast(new Pair(currCity.right, totalDistance + currCity.distance));
            }
            if (currCity.left != null) {
                stack.offerLast(new Pair(currCity.left, totalDistance + currCity.distance));
            }
        }
        return totalDistance;
    }

    static class Pair {
        TreeNode node;
        int dist;
        Pair(TreeNode node, int dist) {
            this.node = node;
            this.dist = dist;
        }
    }


    static class TreeNode {
        String cityName;
        int distance;
        TreeNode left, right;

        TreeNode(String cityName) { this.cityName = cityName; }

        TreeNode(String cityName, int distance) {
            this.cityName = cityName;
            this.distance = distance;
        }
    }
}
