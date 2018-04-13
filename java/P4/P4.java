import java.util.*;

public class P4{
	static int[] anArray = new int[405450];
	static int counter = 0;
	static int larpal = 0;

	public static void main(String[] args){
		for(int i=100;i < 1000; i++){
			for(int j = i; j < 1000; j++){
				anArray[counter] = i*j;
				if(palcheck(anArray[counter]) && anArray[counter] > larpal) 
					{larpal = anArray[counter];}
				counter++;
			}
		}

		System.out.println(larpal);
	}

	public static boolean palcheck(int number){
		String temp1,temp2;

		temp1 = Integer.toString(number);
		StringBuffer buffer = new StringBuffer(temp1);
       	temp2 = buffer.reverse().toString();

       	if(temp1.equals(temp2)){
       		return true;
       	}
       	else return false;
	}
}


