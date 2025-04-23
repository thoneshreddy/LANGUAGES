class Clock {
    public static void main(String[] args) throws InterruptedException {
        int h = 3;
        int m = 59;
        int s = 2;

        while (true) {
            System.out.printf("\r%02d : %02d : %02d", h, m, s);
            System.out.flush();
            Thread.sleep(1000);
            s++;
            if (s == 60) {
                s = 0;
                m++;
                if (m == 60) {
                    m = 0;
                    h++;
                    if (h == 24) {
                        h = 0;
                    }
                }
            }
        }
    }
}
