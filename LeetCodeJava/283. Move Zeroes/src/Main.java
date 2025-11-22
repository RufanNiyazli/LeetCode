import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = new int[]{1, 3, 3, 4, 5};
        arr[1] = arr[3];

        for (int i = 0; i < arr.length; i++) {
            if (arr[-1] == 0) {
                break;
            } else if (arr[i] == 0 && arr[i + 1] != 0) {

            }

        }

        System.out.println(Arrays.toString(arr));
    }
}
