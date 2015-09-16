
//Program to show all the combinations Rs 3 can be made from 2p, 5p, 10p, 20p, 50p coins

#include<stdio.h>


int for_total_combination(int *coins,int incr,int total,int size);
int for_3s_combination(int *coins,int incr,int total,int size);


int main()
{
    int totalall,total3s,total,incr=0,incr1=0;
    int size = 5;
    int coins[]= {2,5,10,20,50};		//2p, 5p, 10p, 20p, 50p Coins
    total=300;


    totalall=for_total_combination(coins,incr,total,size);
    total3s=for_3s_combination(coins,incr1,total,size);

    printf("The Total combinations are %d\n\n",totalall);
    printf("The Total 3's combinations are %d\n\n",total3s);

    return 0;
}

int for_total_combination(int *coins,int incr,int total,int size)
{


    int set1,set2,set3,set4,set5,i,j,k,l,m,newtotal5;

    for(i=size-1; i<size; i++)		//initially 50p coin
    {
        for(j=size-2; j<size; j++)		//initially 20p coin
        {
            for(k=size-3; k<size; k++)			//initially 10p coin
            {
                for(l=size-4; l<size; l++)			//initially 5p coin
                {
                    for(m=size-5; m<size; m++)				//initially 2p coin
                    {
                        set1=0;
                        while(set1<=total/coins[size-1])
                        {
                            set2=0;
                            while(set2<=total/coins[size-2])
                            {
                                set3=0;
                                while(set3<=total/coins[size-3])
                                {
                                    set4=0;
                                    while(set4<=total/coins[size-4])
                                    {
                                        set5=0;
                                        while(set5<=total/coins[size-5])
                                        {
                                            newtotal5=(*(coins+m)*set5)+(*(coins+l)*set4)+(*(coins+k)*set3)+(*(coins+j)*set2)+(*(coins+i)*set1);

                                            if(newtotal5==total)	//if the combination is equal to 300
                                            {
//printf("%dx%d +	%dx%d +	%dx%d +	%dx%d +	%dx%d\n",coins[m],set5,coins[l],set4,coins[k],set3,coins[j],set2,coins[i],set1);
                                                incr++;

                                            }
                                            set5++;
                                        }
                                        set4++;
                                    }
                                    set3++;
                                }
                                set2++;
                            }
                            set1++;
                        }
                    }
                }
            }
        }
    }

    return incr;
}


int for_3s_combination(int *coins,int incr,int total,int size)
{
    int set1,set2,set3,i,j,k,newtotal5;

    for(i=size-3; i<size; i++)			//initially 10p coin
    {
        for(j=size-4; j<size; j++)			//initially 5p coin
        {
            for(k=size-5; k<size; k++)				//initially 2p coin
            {
                set1=0;
                while(set1<=total/coins[size-5])
                {
                    set2=0;
                    while(set2<=total/coins[size-5])
                    {
                        set3=0;
                        while(set3<=total/coins[size-5])
                        {
                            newtotal5= (*(coins+k)*set3)+(*(coins+j)*set2)+(*(coins+i)*set1);

                            if(newtotal5==total)	//if the combination is equal to 300
                            {
//printf("%dx%d +	%dx%d +	%dx%d\n",coins[k],set3,coins[j],set2,coins[i],set1);
                                incr++;

                            }

                            set3++;
                        }
                        set2++;
                    }
                    set1++;
                }
            }
        }
    }
    return incr;

}


