package leetcode.two_pointers;

public class CheckIfAWordOccursAsAPrefixOfAnyWordInASentence {

    public int isPrefixOfWord(String sentence, String searchWord) {
        String[] words = sentence.split(" ");

        int answer = -1;
        for (int i = 0; i < words.length; i++) {
            if (words[i].startsWith(searchWord)) {
                answer = i + 1;
                break;
            }
        }

        return answer;
    }
}
