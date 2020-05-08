#include<bits/stdc++.h>
using namespace std;
main()
{

    int test;
    cin>>test;
    while(test--)
    {
        int ss,arr1[3],count=0,sum=0;
        cin>>ss;
        cin>>arr1[0]>>arr1[1]>>arr1[2];


        if(arr1[0]<arr1[1]&&arr1[1]>arr1[0])
        {

            if(arr1[0]>arr1[2])
                swap(arr1[0],arr1[2]);
                for(int i=0;i<3;i++)
        {  sum+=arr1[i];
            if(sum>ss)
            {
                i--;
                sum=0;
                count++;
            }
            if(sum<=ss&&i==2)
                count++;

        }

        }
        else if((arr1[0]<arr1[1]&&arr1[1]<arr1[2])||arr1[2]>arr1[1]&&arr1[1]>arr1[0])
        {
        sort(arr1,arr1+3);
        for(int i=0;i<3;i++)
        {  sum+=arr1[i];
            if(sum>ss)
            {
                i--;
                sum=0;
                count++;
            }
            if(sum<=ss&&i==2)
                count++;

        }
        }
        else if(arr1[0]>arr1[1]&&arr1[1]<arr1[0])
        {
            if(arr1[2]<arr1[0])
                swap(arr1[2],arr1[0]);
                for(int i=0;i<3;i++)
        {  sum+=arr1[i];
            if(sum>ss)
            {
                i--;
                sum=0;
                count++;
            }
            if(sum<=ss&&i==2)
                count++;

        }

        }
        else
        {
             for(int i=0;i<3;i++)
        {      sum+=arr1[i];
            if(sum>ss)
            {
                i--;
                sum=0;
                count++;
            }
            if(sum<=ss&&i==2)
                count++;

        }
        }
        cout<<count<<endl;
    }
}
