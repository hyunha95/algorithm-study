package baekjoon.알고리즘책.탐색;

import java.util.*;

public class DFS와BFS프로그램 {

    static ArrayList<Integer>[] A;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int start = sc.nextInt();

        A = new ArrayList[N + 1];
        for (int i = 1; i < N + 1; i++) {
            A[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            int S = sc.nextInt();
            int E = sc.nextInt();
            A[S].add(E);
            A[E].add(S);
        }

        for (int i = 1; i < N + 1; i++) {
            Collections.sort(A[i]);
        }

        visited = new boolean[N + 1];
        DFS(start);
        System.out.println();
        visited = new boolean[N + 1];
        BFS(start);
    }

    static void BFS(int node) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(node);
        visited[node] = true;

        while (!queue.isEmpty()) {
            int nowNode = queue.poll();
            System.out.print(node + " ");
            for (int i : A[nowNode]) {
                if (!visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }

    static void DFS(int node) {
        if (visited[node]) {
            return;
        }

        visited[node] = true;
        System.out.print(node + " ");
        for (int i : A[node]) {
            if (!visited[i]) {
                DFS(i);
            }
        }
    }
}
