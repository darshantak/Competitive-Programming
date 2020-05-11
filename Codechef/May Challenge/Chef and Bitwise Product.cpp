// Thu May 7 22:57:06 IST 2020
#include<bits/stdc++.h>
using namespace std;

#if DEBUG && !ONLINE_JUDGE
    #include "/home/raghukul/Competitive/templates/debug.h"
#else
    #define debug(args...)
    #define DBG(x...)
#endif

#define int long long
#define N 64

int l, r, mask;

vector<bool> Bin(int x) {
	vector<bool> a(N);
	for(int i = 0;i < N;i++) {
		a[i] = x%2;
		x /= 2;
	}
	reverse(a.begin(), a.end());
	return a;
}

void correct(vector<int> &values) {
	int v, exc_or, num;
	for(int i = 0;i < (int)values.size();i++) {
		v = values[i];
		exc_or = values[i]^mask;
		auto bit = Bin(exc_or);
		for(int i = 0;i < N;i++) {
			if(bit[i] && (v&(1LL << (N-i-1)))) {
				num = v & (~(1LL << (N-i-1)));
				if(num >= l && num <= r)
					v = num;
			}
		}
		values[i] = v;
	}
}

void debug_bin(vector<bool> a) {
	for(auto x: a)
		cout << x;
	cout << endl;
}

signed main() {
    ios_base::sync_with_stdio(false),cin.tie(0),cout.precision(17);
    int t;
    cin >> t;
    int x, y;
    while(t--)
	{
    	cin >> x >> y >> l >> r;
    	mask = (x | y);
    	auto l_bit = Bin(l);
    	auto r_bit = Bin(r);


    	int curr = 0;
    	int i;
    	vector<int> values;
    	for(i = 0;i < N;i++) {
    		curr *= 2;
    		if(l_bit[i] == r_bit[i]) {
    			curr += l_bit[i];
    		} else {
    			int left = N-1-i;
    			values.push_back((curr << left) + (1LL << left) - 1LL);
    			curr = (curr + 1);
    			break;
    		}
    	}
    	i++;
    	for(; i < N;i++) {
    		curr *= 2;
    		if(r_bit[i]) {
    			int left = N-1-i;
    			values.push_back((curr << left) + (1LL << left) - 1LL);
    			curr++;
    		}
    	}
    	values.push_back(curr);
    	correct(values);

    	int ans, mx = -1;
    	for(auto v: values) {
    		curr = (x&v) * (y&v);
    		if(curr > mx) {
    			mx = curr;
    			ans = v;
    		} else if(curr == mx) {
    			ans = min(ans,v);
    		}
    	}
    	if(x == 0 || y == 0 || mx == 0)
    		ans = l;
    	cout << ans << endl;
    }
    return 0;
}
