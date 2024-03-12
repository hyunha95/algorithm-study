package baekjoon.greedy;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class P2828_사과담기게임 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nm = Stream.of(sc.nextLine().split(" ")).mapToInt(Integer::valueOf).toArray();
        int n = nm[0];
        int bucketLength = nm[1];
        int numberOfApples = sc.nextInt();

        List<Integer> apples = new ArrayList<>();

        for (int i = 0; i < numberOfApples; i++) {
            apples.add(sc.nextInt());
        }

        int start = 1;
        int end = bucketLength;
        int moveCount = 0;

        for (int i = 0; i < apples.size(); i++) {
            int position = apples.get(i);
            int currentMove;
            if (end < position) { // 마지막 값 보다 큰 경우 오른쪽에서 찾고
                currentMove = position - end;
                moveCount += currentMove;
                start += currentMove;
                end = position;

            } else { // 시작 값 보다 작은 경우 왼쪽에서 찾는다.
                currentMove = start - position;
                moveCount += currentMove;
                end -= currentMove;
                start = position;
            }
        }
        System.out.println(moveCount);
    }
}
