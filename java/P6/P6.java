import java.util.*;


public class P6{

	public static void main(String[] args){

		System.out.println(result(100));
	}

	public static int result(int n){
		return (n*(n+1)/2)*(n*(n+1)/2) - (n*(n+1)*(2*n+1))/6;
	}

}