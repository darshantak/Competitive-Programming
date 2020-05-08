#include<bits/stdc++.h>
using namespace std;
#define int long long
  main()
{
 
 
    int no;
    cin>>no;
     int a[no],b[no];
     deque<int> qu;
     unordered_map<int,int> m1;
     for(int i=0;i<no;i++)
        {
            cin>>a[i];
            m1[a[i]]=1;
 
}
  for(int i=1;i<=no;i++)
  {
      if(m1[i]==0)
        qu.push_back(i);
  }
 
for(int i =0;i<=no;i++)
{
 
    if(a[i]==0)
    {
        if(qu.back()!=i+1)
        {
            a[i]=qu.back();
            qu.pop_back();
        }
       else if(qu.front()!=i+1)
        {
            a[i]=qu.front();
            qu.pop_front();
        }
 
    }
    if(qu.empty())
       break;
}
for(int i=0;i<no;i++)
    cout<<a[i]<<" ";
    
}