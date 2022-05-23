package application;

public class MyNoThread01 {
	public static void showNum() {
		for(int i=0; i<100000; i++) {
			System.out.print(i);
			
			if(i%100 == 0) {
				System.out.println();
			}
		}
	}
	
	public static void showAscii() {
		int cnt = 1;
		for(char i='A'; i<'Z'; i++) {
			System.out.print(i);
			++cnt;
			if(i%100 == 0) {
				System.out.println();
			}			
		}
		System.out.println(cnt + "��");
	}
	
	public static void main(String[] args) {
//		showNum();
		showAscii();
	}

}
