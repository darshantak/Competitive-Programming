#include<bits/stdc++.h>
using namespace std;
#define int long long
main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int n;
        cin>>n;
        string ss;
    cin>>ss;
    int count=0;
    int Max=0;
    int i;
    for( i=0;i<ss.size();i++)
    {
        if(ss[i]=='A')
            break;
    }
       for(int j=i+1;j<ss.size();j++)
       {    if(ss[j]=='P')
          {  count=0;
               int k;
              for( k=j;k<ss.size();k++)
           {
               if(ss[k]=='P')
                count++;
               else
                break;
           }
           if(count>Max)
            Max=count;
            i=k;
          }


       }
       cout<<Max<<endl;
    }
}