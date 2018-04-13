import java.util.*;

public class P9{

	public static void main(String[] args){
		int m =1;
		
		
		for(int r =1;r <10000;r++){
			if(striple(r)==1000){
				System.out.println(ptriple(r));
				break;
			}
		}



	}

	public static int striple(int n){
		for(int i = 1;i<n;i++){
			for(int j=1;j<n;j++){
				if(n*n==i*i+j*j){
					
					return n+i+j;
					
					
				}
				}
			}
		
			return 0;
		}

			public static int ptriple(int n){
		for(int i = 1;i<n;i++){
			for(int j=1;j<n;j++){
				if(n*n==i*i+j*j){
					
					return n*i*j;
					
					
				}
				}
			}
		
			return 0;
		}


		
}


