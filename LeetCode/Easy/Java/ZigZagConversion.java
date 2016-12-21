package test;

public class Main {
	
	public static void main(String[] args) {
		System.out.println(convert("PAYPALISHIRING", 3));
	}
	
    public static String convert(String s, int numRows) {
    	
        if(numRows<=1)
        	return s;
        
        String sol = "";
        StringBuilder[] sb = new StringBuilder[numRows];
        for(int i = 0 ; i < sb.length; i++) {
        	sb[i] = new StringBuilder("");
        }
        
        int index = 0;
        int upOrDown = 1; // Positive for down, negative for going up
        
        for(int i = 0 ; i < s.length() ; i++) {
        	sb[index].append(s.charAt(i));
        	if(index==0) upOrDown = 1;
        	if(index==numRows-1) upOrDown = -1;
        	index+=upOrDown;
        }
  
        for(int i = 0 ; i < sb.length; i++) {
        	sol += sb[i];
        }
        return sol;
		
    }
        

}
