package BasicJava;

public class P003_2 {
	public static void main(String[] args) {
		P003_1 date1 = new P003_1(30, 2, 2000);
		System.out.println(date1.isValid());

		P003_1 date2 = new P003_1(2, 10, 2006);
		System.out.println(date2.isValid());
	}

}
