package baekjoon.알고리즘책.탐색;

import java.util.*;

public class 트리의지름구하기 {

    static ArrayList<Edge>[] A;
    static boolean[] visited;
    static int[] distance;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        A = new ArrayList[N + 1];

        for (int i = 1; i < N + 1; i++) {
            A[i] = new ArrayList<>();
        }

        for (int i = 1; i < N + 1; i++) {
            int S = sc.nextInt();
            while (true) {
                int E = sc.nextInt();
                if (E == -1) break;
                int V = sc.nextInt();
                A[S].add(new Edge(E, V));
            }
        }

        visited = new boolean[N + 1];
        distance = new int[N + 1];
        BFS(1);
        int max = 1;
        for (int i = 2; i < N + 1; i++) {
            if (distance[max] < distance[i]) {
                max = i;
            }
        }
        visited = new boolean[N + 1];
        distance = new int[N + 1];
        BFS(max);
        Arrays.sort(distance);
        System.out.println(distance[N]);
    }

    static void BFS(int node) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(node);
        visited[node] = true;

        while (!queue.isEmpty()) {
            int nowNode = queue.poll();
            for (Edge edge : A[nowNode]) {
                int e = edge.e;
                int v = edge.value;
                if (!visited[e]) {
                    queue.add(e);
                    visited[e] = true;
                    distance[e] = distance[nowNode] + v;
                }
            }
        }
    }

    static class Edge {
        int e;
        int value;

        public Edge(int e, int value) {
            this.e = e;
            this.value = value;
        }
    }
}
