package programmers.kakao.kako_winter_internship_2024;

import java.util.*;

public class 도넛과막대그래프1 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[][] {{2, 3}, {4,3}, {1,1}, {2,1}})));
    }

    static int nodeCount;
    static List<List<Integer>> graph = new ArrayList<>();
    static List<Integer> entranceCount = new ArrayList<>();
    static boolean[] visited;

    public static int[] solution(int[][] edges) {

        // 1. 노드 개수 파악
        for (int[] edge : edges) {
            nodeCount = Math.max(nodeCount, Math.max(edge[0], edge[1]));
        }

        // 2. 그래프 초기화
        for (int i = 0; i <= nodeCount; i++) {
            graph.add(new ArrayList<>());
            entranceCount.add(0);
        }

        // 3. 간선 정보 입력
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            entranceCount.set(edge[1], entranceCount.get(edge[1]) + 1);
        }

        // 4. 임의 정점 찾기
        int startNum = findStart();
        List<Integer> startWay = graph.get(startNum);

        // 5. 임의의 정점에서 오는 간선 삭제
        for (int node : startWay) {
            entranceCount.set(node, entranceCount.get(node) - 1);
        }

        visited = new boolean[nodeCount + 1];
        int donut = 0, stick = 0, eight = 0;
        for (int startNode : startWay) {
            if (!visited[startNode]) {
                Type type = exploreGraph(startNode);
                if (type == Type.DONUT) donut++;
                else if (type == Type.STICK) stick++;
                else eight++;
            }
        }

        int[] answer = {startNum, donut, stick, eight};
        return answer;
    }

    static Type exploreGraph(int startNode) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(startNode);
        visited[startNode] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            if (graph.get(node).size() == 2 && entranceCount.get(node) == 2) {
                return Type.EIGHT;
            } else if (graph.get(node).isEmpty()) {
                return Type.STICK;
            } else {
                for (int neighbor : graph.get(node)) {
                    if (!visited[neighbor]) {
                        queue.add(neighbor);
                        visited[neighbor] = true;
                    }
                }
            }
        }
        return Type.DONUT;
    }

    static int findStart() {
        for (int i = 1; i <= nodeCount; i++) {
            if (graph.get(i).size() >= 2 && entranceCount.get(i) == 0) {
                return i;
            }
        }
        return -1;
    }

    enum Type {
        DONUT, STICK, EIGHT;
    }
}
