import java.util.Scanner;

public class P5585_거스름돈 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int[] coins = new int[]{500,100,50,10,5,1};

        int money = 1000 - sc.nextInt();
        int count = 0;

        for (int i = 0; i < coins.length; i++) {
            if(coins[i] <= money){
                count += money / coins[i];
                money %= coins[i];
            }
        }

        System.out.println(count);
    }
}
