import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class InsertionSortTest {

  private static List<double[]> toSolve = new ArrayList<>();
  private static List<double[]> solved = new ArrayList<>();

  private static double[] parseJsonArray(String json) {
    json = json.trim().replace("[", "").replace("]", "");
    String[] numbers = json.split(",");
    double[] array = new double[numbers.length];
    for (int i = 0; i < numbers.length; i++) {
      array[i] = Double.parseDouble(numbers[i].trim());
    }

    return array;
  }

  public static double[] insertionSort(double[] nums) {
    for (int i = 1; i < nums.length; i++) {
      double key = nums[i];
      int j = i - 1;
      while (j >= 0 && nums[j] > key) {
        nums[j + 1] = nums[j];
        j--;
      }
      nums[j + 1] = key;
    }
    return nums;
  }

  public static void main(String[] args) {
    InsertionSortTest sort = new InsertionSortTest();

    String path = "test_cases.txt";
    try (BufferedReader br = new BufferedReader(new FileReader(path))) {
      String line;
      while ((line = br.readLine()) != null) {
        String[] parts = line.split("\\?");
        for (String part : parts) {
          String[] caseParts = part.split(";");
          double[] input = parseJsonArray(caseParts[0]);
          double[] output = parseJsonArray(caseParts[1]);
          toSolve.add(input);
          solved.add(output);
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

    int correct = 0;
    int failed = 0;

    for (int i = 0; i < toSolve.size(); i++) {
      double[] sorted = sort.insertionSort(toSolve.get(i));

      if (Arrays.toString(sorted).equals(Arrays.toString(solved.get(i).clone()))) {
        correct++;
      } else {
        failed++;
      }
    }

    System.out.println("Correct: " + correct + "\nFailed: " + failed);
  }
}
