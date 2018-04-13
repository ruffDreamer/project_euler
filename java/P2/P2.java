import java.util.*;

public class P2{

	public static void main(String[] args){
		int fib1 = 1, fib2 = 2, fib3=3,sum=2;
		while(fib3 < 4000000){
			fib3 = fib1 + fib2;
			if(fib3%2==0){
				sum += fib3;
				System.out.println(fib3);
			}
			fib1 = fib2;
			fib2 = fib3;
			
		}

		System.out.println(sum);

	}



}