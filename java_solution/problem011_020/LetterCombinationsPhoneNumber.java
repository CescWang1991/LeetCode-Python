package problem011_020;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class LetterCombinationsPhoneNumber {

    private HashMap<Character, String> map = new HashMap<>();

    private List<String> result = new ArrayList<>();

    public List<String> letterCombinations(String digits) {
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");
        result = backtracking(digits, result);
        return result;
    }

    private List<String> backtracking(String digits, List<String> result) {
        if(digits.equals("")) {
            return result;
        }
        List<String> temp = new ArrayList<>();
        char digit = digits.charAt(0);
        for (int i = 0; i < map.get(digit).length(); i++) {
            if (result.isEmpty()) {
                temp.add(String.valueOf(map.get(digit).charAt(i)));
            } else {
                for (String item: result) {
                    temp.add(item + map.get(digit).charAt(i));
                }
            }
        }
        result = backtracking(digits.substring(1), temp);
        return result;
    }
}
