#include<bits/stdc++.h>
using namespace std;
#define int long long
main()
{

    int test;
    cin>>test;
    while(test--)
    {
     int numb;
     cin>>numb;
     int arr[numb];
     for(int i=0;i<numb;i++)
        cin>>arr[i];
     int i=0;
     int answer=0;
     while(i<numb)
     {   int maximum=INT_MIN,minimum=INT_MIN;
         while(arr[i]>0&&i<numb)
         {
             maximum=max(maximum,arr[i]);
             i++;

         }
         if(maximum!=INT_MIN)
         answer+=maximum;

         while(arr[i]<0&&i<numb)
         {
             minimum=max(minimum,arr[i]);
             i++;

         }
          if(minimum!=INT_MIN)
         answer+=minimum;

     }
     cout<<answer<<endl;

    }
}