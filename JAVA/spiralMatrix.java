import java.util.*;
class Solution {
    public static void main(String args[]) {
        int matrix[][] = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12}
        };
        ArrayList<Integer> l = new ArrayList<>();
        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                l.add(matrix[top][i]);
            }
            top++;
            for (int j = top; j <= bottom; j++) {
                l.add(matrix[j][right]);
            }
            right--;
            if (top <= bottom) {
                for (int k = right; k >= left; k--) {
                    l.add(matrix[bottom][k]);
                }
                bottom--;
            }
            if (left <= right) {
                for (int m = bottom; m >= top; m--) {
                    l.add(matrix[m][left]);
                }
                left++;
            }
        }

        for (int val : l) {
            System.out.print(val + " ");
        }
    }
}
