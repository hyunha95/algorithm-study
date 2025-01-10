package programmers.kakao.kakao_blind_recruitment_2023;

/**
 * chatgpt 풀이
 */
public class 택배배달과수거하기 {

    public static void main(String[] args) {
        int cap1 = 4, n1 = 5;
        int[] deliveries1 = {1, 0, 3, 1, 2};
        int[] pickups1 = {0, 3, 0, 4, 0};
        System.out.println(solution(cap1, n1, deliveries1, pickups1)); // Output: 16

        int cap2 = 2, n2 = 7;
        int[] deliveries2 = {1, 0, 2, 0, 1, 0, 2};
        int[] pickups2 = {0, 2, 0, 1, 0, 2, 0};
        System.out.println(solution(cap2, n2, deliveries2, pickups2)); // Output: 30
    }

    public static long solution(int cap, int n, int[] deliveries, int[] pickups) {
        int totalDistance = 0;
        int deliveryIndex = n - 1;
        int pickupIndex = n - 1;

        while (deliveryIndex >= 0 || pickupIndex >= 0) {
            int maxDistance = 0;
            int load = 0;

            // 배달
            while (deliveryIndex >= 0 && load < cap) {
                if (deliveries[deliveryIndex] > 0) {
                    int canDeliver = Math.min(cap - load, deliveries[deliveryIndex]);
                    deliveries[deliveryIndex] -= canDeliver;
                    load += canDeliver;
                    maxDistance = Math.max(maxDistance, deliveryIndex + 1);
                }
                if (deliveries[deliveryIndex] == 0) {
                    deliveryIndex--;
                }
            }

            // 수거
            load = 0;
            while (pickupIndex >= 0 && load < cap) {
                if (pickups[pickupIndex] > 0) {
                    int canPickup = Math.min(cap - load, pickups[pickupIndex]);
                    pickups[pickupIndex] -= canPickup;
                    load += canPickup;
                    maxDistance = Math.max(maxDistance, pickupIndex + 1);
                }
                if (pickups[pickupIndex] == 0) {
                    pickupIndex--;
                }
            }

            totalDistance += maxDistance * 2;
        }

        return totalDistance;
    }

//    public static long solution(int cap, int n, int[] deliveries, int[] pickups) {
//        long totalDistance = 0;
//
//        int deliveryIndex = n - 1;
//        int pickupIndex = n - 1;
//
//        while (deliveryIndex >= 0 || pickupIndex >= 0) {
//            int load = 0;
//            int maxDistance = 0;
//
//            // 배달
//            while (deliveryIndex >= 0 && load < cap) {
//                if (deliveries[deliveryIndex] > 0) {
//                    int canDeliver = Math.min(cap - load, deliveries[deliveryIndex]);
//                    deliveries[deliveryIndex] -= canDeliver;
//                    load += canDeliver;
//                    maxDistance = Math.max(maxDistance, deliveryIndex + 1);
//                }
//                if (deliveries[deliveryIndex] == 0) {
//                    deliveryIndex--;
//                }
//            }
//
//            // 수거
//            load = 0;
//            while (pickupIndex >= 0 && load < cap) {
//                if (pickups[pickupIndex] > 0) {
//                    int canPickup = Math.min(cap - load, pickups[pickupIndex]);
//                    pickups[pickupIndex] -= canPickup;
//                    load += canPickup;
//                    maxDistance = Math.max(maxDistance, pickupIndex + 1);
//                }
//                if (pickups[pickupIndex] == 0) {
//                    pickupIndex--;
//                }
//            }
//
//            // 왕복 거리 추가
//            totalDistance += maxDistance * 2;
//        }
//        return totalDistance;
//    }

}
