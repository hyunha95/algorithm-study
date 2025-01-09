package programmers.완전탐색;

public class 최소직사각형 {

    public static void main(String[] args) {
        System.out.println(solution(new int[][] {{60,50}, {30,70}, {60,30}, {80,40}}));
        System.out.println(solution(new int[][] {{10, 7}, {12,3}, {8,15}, {5,15}}));
    }

    public static int solution(int[][] sizes) {
        int width = 0;
        int height = 0;

        for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] < sizes[i][1]) {
                int temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
            }

            if (width < sizes[i][0]) {
                width = sizes[i][0];
            }

            if (height < sizes[i][1]) {
                height = sizes[i][1];
            }
        }

        return width * height;
    }
}
