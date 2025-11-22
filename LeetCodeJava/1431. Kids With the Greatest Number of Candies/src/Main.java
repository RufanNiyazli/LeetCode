import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxCandy = 0;
        for (int candy : candies) {
            maxCandy = Math.max(maxCandy, candy);
        }
        List<Boolean> result = new ArrayList<>();
        for (int candy : candies) {
            if ((candy + extraCandies) > maxCandy) {
                result.add(true);
            } else {
                result.add(false);
            }
        }
        return result;
    }
}