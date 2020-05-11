#include<bits/stdc++.h>
using namespace std;

#if DEBUG && !ONLINE_JUDGE
    #include "/home/raghukul/Competitive/templates/debug.h"
#else
    #define debug(args...)
    #define DBG(x...)
#endif

int main() {
    ios_base::sync_with_stdio(false),cin.tie(0),cout.precision(17);
    int t;
    cin >> t;
    while(t--) {
    	int n, k;
    	cin >> n >> k;
    	vector<pair<int,int>> arr1(n);
    	for(int i = 0;i < n;i++) {
    		cin >> arr1[i].first;
    		arr1[i].second = i;
    	}
    	sort(arr1.begin(), arr1.end());
    	vector<int> arr2(n, 0);
    	int cnt = 1;
    	vector<vector<int>> comb;
    	for(int i = 0;i < n;i++) {
    		if(arr1[i].second == i)
    			arr2[i] = -1;
    		else if(arr2[i] == 0) {
    			int pos = i;
    			vector<int> tmp;
    			while(arr2[pos] == 0) {
    				arr2[pos] = cnt;
    				tmp.push_back(pos);
    				pos = arr1[pos].second;
    			}
    			comb.push_back(tmp);
    			cnt++;
    		}
    	}
    	DBG(comb);
    	DBG(arr2);

    	bool can = true;

    	vector<vector<int>> sols;
    	vector<vector<int>> swapp;

    	for(auto current_go: comb) {
    		int m = (int)current_go.size();
    		while((m != 3) && (m != 2)) {
    			int f_new[3];
    			f_new[0] = current_go[m-1];
    			f_new[1] = current_go[m-2];
    			f_new[2] = current_go[m-3];
    			sols.push_back({f_new[0], f_new[1], f_new[2]});
    			current_go[m-3] = current_go[m-1];
    			m -= 2;
    		}
    		if(m == 3)
    			sols.push_back({current_go[2], current_go[1], current_go[0]});
    		else
    			swapp.push_back({current_go[0], current_go[1]});
    	}
    	if(swapp.size()%2)
    		can = false;
    	else 
    		for(int i = 0;i < (int)swapp.size(); i+=2) {
    			sols.push_back({swapp[i+1][1], swapp[i+1][0], swapp[i][1]});
    			sols.push_back({swapp[i][0], swapp[i][1], swapp[i+1][1]});
    		}
    	DBG(sols);
    	if((int)sols.size() > k)
    		can = false;
    	if(!can)
    		cout << "-1\n";
    	else {
    		cout << sols.size() << endl;
    		for(auto x: sols) {
    			cout << x[0]+1 << " " << x[1]+1 << " " << x[2]+1 << endl;
    		}
    	}
    }
    return 0;
}
