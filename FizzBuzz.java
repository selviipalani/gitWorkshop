
/**
 * Prints numbers between 0 and 100.
 * 
 * If the number if divisible by both 3 and 5, print FizzBuzz
 * 
 * If it's just divisible by 3, print Fizz
 * 
 * If it's just divisible by 5, print Buzz
 * @author lev
 *
 */
public class FizzBuzz {
    public static void main(String args[]) {
        for (int i = 0; i <= 100; i++) {
           if (i % 15 == 0) {
               System.out.println("FizzBuzz" + " ");
           } else if (i % 3 == 0) {
               System.out.println("Fizz" + " ");
           } else if (i % 5 == 0) {
               System.out.println("Buzz" + " ");
           } else {
               System.out.println(i);
           }
        }
    }
}
