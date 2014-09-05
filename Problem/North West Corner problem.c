#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <windows.h>
int main()
{
int k,l;
    int a[6][6]= {0};
    int s[]= {25,35,105,20,15};
    int d[]= {50,70,30,50};
    int i,j,m,n,initial,temp3,temp=0,temp1=0,temp2=0;
    int cost;
    printf("\n\t\t\t Game Thoery : Transptation problem \n");
    printf("\n\t\t\t North west corner method \n\n");
    printf("enter the no of rows\n");
    scanf("%d",&m);
    printf("enter the no of columns\n");
    scanf("%d",&n);
    printf("enter the values for a matrix\n");
    for(i=0; i<m; i++)
        for(j=0; j<n; j++)
        {
            scanf("%d",&a[i][j]);
        }
         printf("\n");
        for(i=0; i<m; i++)
        printf("supply[%d] is :%d\n",i,s[i]);

        for(i=0; i<n; i++)
        printf("demand[%d] is :%d\n",i,d[i]);



    initial=a[0][0];/*the first  north west corner value*/
if(initial>0)
{
    i=0;j=0;
k=0,l=0;
    while(i<6&&j<5&&k<6&&l<5)
    {

        if(s[i]<d[j])
    {
        printf("----------------------------------------------\n\n");
printf("If supply is less than demand then\n\n");
   printf("Row %d completed\n\n",k);
        cost=a[k][l]*s[i];
        temp+=cost;
        k++;
        d[j]=d[j]-s[i];
        s[i]=s[i]-s[i];
        printf("cost:%d\n",cost);
        printf("supply:%d\n",s[i]);
        printf("demand:%d\n\n",d[j]);
        i++;
    }
else if(s[i]>d[j])
    {
         printf("----------------------------------------------\n\n");
        printf("If supply is more than demand then\n\n");
         printf("column %d completed\n\n",l);
        cost=a[k][l]*d[j];
        temp1+=cost;
        l++;
        s[i]=s[i]-d[j];
        d[j]=d[j]-d[j];
        printf("cost:%d\n",cost);
        printf("supply:%d\n",s[i]);
        printf("demand:%d\n\n",d[j]);
        j++;

    }
     else if(s[i]==d[j])
    {
         printf("----------------------------------------------\n\n");
        printf("If supply is equal to demand then\n\n");
        printf("row %d completed\n\n",k);
          printf("column %d completed\n\n",l);
        cost=a[k][l]*d[j];
        temp2+=cost;
        d[j]=d[j]-d[j];
        s[i]=s[i]-s[i];
        printf("cost:%d\n",cost);
        printf("supply:%d\n",s[i]);
        printf("demand:%d\n\n",d[j]);
        temp3=temp+temp1+temp2;
printf("the Total cost is:%d \n",temp3);
        return 0;
    }

    else
    {
        exit(0);
    }

}

}

return 0;
}



