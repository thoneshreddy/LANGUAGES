class Clock {
    public static void main(String[] args)throws InterruptedException{
        int h=3;
        int m=59;
        int s=02;
        while(true)
        {
        	System.out.printf("\r %2d : %2d : %2d ",h,m,s);
		System.out.flush();
		Thread.sleep(1000);
		s+=1;
		if(s==60)
		{
			s=0;
			m+=1;
			if(m==60)
			{
				m=0;
				h+=1;
				if(h==24)
				{
					h=0;
				}
			}
		}

  	}      
    }
}
