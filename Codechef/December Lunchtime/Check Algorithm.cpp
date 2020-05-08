#include<bits/stdc++.h>
using namespace std;
#define int long long
string printRLE(string s)
{ string result="";
    for (int i = 0; s[i] != '\0'; i++)
    {

        int count = 1;
        while (s[i] == s[i + 1])
        {
            i++;
            count++;
        }
        string c=to_string(count);
        result+=s[i]+c;
    }
    return result;

}  main()
{

 int t;
 cin>>t;
 while(t--)
 {
     string s;
     cin>>s;
     if(printRLE(s).size()<s.size())
        cout<<"YES";
     else
        cout<<"NO";
     cout<<endl;
 }

}