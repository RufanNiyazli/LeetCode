import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public void sortColors(int[] nums) {
        int length = nums.length;
        while (length > 0) {
            for (int i = 0; i < length - 1; i++) {
                if (nums[i] > nums[i + 1]) {

                    int temp = nums[i];
                    nums[i] = nums[i + 1];
                    nums[i + 1] = temp;
                }
            }
            length--;
        }
    }
}