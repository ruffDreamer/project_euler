import java.util.*;

public class P7{
	
	public static void main(String[] args){
	int[] master = new int[10001];
	master[0]=2;
	int m = 3, j = 1;

		while(j < 10001){
			if(primeCheck(m,master,j)){
				master[j]=m;
				j++;
			}
			m++;
		}

	System.out.println(master[10000]);


	}


	public static boolean primeCheck(int n, int[] list,int l){
		boolean check=true;
		for(int i=0;i<l;i++){
			if(n % list[i]==0){
				check = false;
				break;
					}

			else check=true;

		}
		return check;
	}


}