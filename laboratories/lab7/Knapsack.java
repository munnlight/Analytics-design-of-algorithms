import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Knapsack {
  public static double fracKnapsack(int bagSize, int[] values, int[] weights) {
    List<Double> portion = new ArrayList<>();

    for (int i = 0; i < values.length; i++) {
      portion.add(Double.valueOf(values[i] / weights[i]));
    }

    int index = portion.indexOf(Collections.max(portion));
    int value = values[index];
    int weight = weights[index];

    if (bagSize >= weight) {
      values[index] = 0;
      weights[index] = 1;
      return value + fracKnapsack(bagSize - weight, values, weights);
    } else {
      return portion.get(index) * bagSize;
    }
  }

  public static void main(String[] args) {
    int size = 10;
    int[] values = { 10, 12, 15, 20 };
    int[] weights = { 5, 3, 5, 4 };

    System.out.println(fracKnapsack(size, values, weights));
  }
}