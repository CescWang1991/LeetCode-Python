package problem001_010;

/**
 * 010. Regular Expression Matching
 */
public class RegularExpressionMatching {
    public boolean isMatch(String s, String p) {
        int m = s.isEmpty()? 1: s.length() + 1;
        int n = p.isEmpty()? 1: p.length() + 1;
        boolean[][] dp = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = true;
                } else if (i == 0) {
                    dp[i][j] = p.charAt(j-1) == '*' && dp[i][j - 2];
                } else if (j == 0) {
                    dp[i][j] = false;
                } else {
                    dp[i][j] = (dp[i-1][j-1] && (p.charAt(j-1) == s.charAt(i-1) || p.charAt(j-1) == '.')) ||
                            (dp[i][j-2] && p.charAt(j-1) == '*') ||
                            (dp[i-1][j] && p.charAt(j-1) == '*' && (s.charAt(i-1) == p.charAt(j-2) || p.charAt(j-2) == '.'));
                }
            }
        }
        return dp[m-1][n-1];
    }
}