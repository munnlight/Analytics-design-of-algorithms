import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import mainer.Knapsack;

public class KnapsackTest {

  int[] profit = { 6, 10, 12 };
  int[] weight = { 1, 2, 3 };
  int W = 5;

  @Test
  public void test1() {
    assertEquals(30, Knapsack.knapSack(W, weight, profit, profit.length));
  }

  int[] profit2 = { 6, 10, 12, 11, 15 };
  int[] weight2 = { 2, 2, 3, 5, 7 };
  int W2 = 11;

  @Test
  public void test2() {
    assertEquals(52, Knapsack.knapSack(W2, weight2, profit2, profit2.length));
  }
}
