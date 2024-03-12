package leetcode.easy;

public class AddBinary {

    public static void main(String[] args) {
        System.out.println(addBinary("11", "1"));
        System.out.println(addBinary("1010", "1011"));
    }

    public static String addBinary(String a, String b) {
        int p1 = a.length() - 1;
        int p2 = b.length() - 1;

        StringBuilder sb = new StringBuilder();

        int carry = 0;
        while (p1 >= 0 || p2 >= 0) {
            int sum = 0;
            sum += carry;

            sum += p1 >= 0 ? a.charAt(p1) - '0' : 0;
            sum += p2 >= 0 ? b.charAt(p2) - '0' : 0;

            if (sum == 2) {
                carry = 1;
                sum = 0;
            } else if (sum == 3) {
                carry = 1;
                sum = 1;
            } else if (sum == 1) {
                carry = 0;
                sum = 1;
            }

            sb.append(sum);
            p1--;
            p2--;
        }

        if (carry > 0) {
            sb.append(1);
        }

        return sb.reverse().toString();
    }

}
