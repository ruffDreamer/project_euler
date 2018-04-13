import java.util.*;

public class P3{
	static long[] anArray = new long[10];
	static int j=1;

	public static void main(String[] args){
		long test = 600851475143L;
		

		

		for(int k = 1; k<test; k++){
			divisor(test,j);
			test /= anArray[j];
			System.out.println(anArray[j]);
		}
		

		
		

	}

	public static void divisor(long number, int m){
		for(int i=2;i*i < number; i++){
			if(number%i ==0){
				anArray[m]=i;
				++m;
				break;
			}
		}
		anArray[m] = number;
	}
}