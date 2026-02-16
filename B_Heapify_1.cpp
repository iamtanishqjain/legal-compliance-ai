#include <bits/stdc++.h>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define allr(x) (x).rbegin(), (x).rend()
using ll = long long;
using ull = unsigned long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vb = vector<bool>;
using vc = vector<char>;
using vll = vector<ll>;
using mii = map<int,int>;
using unmii = unordered_map<int,int>;

const int MOD = 1e9 + 7;
const int MAXN = 1e6 + 5;

bool isPowerOfTwo(ll n) {
    return (n && !(n & (n - 1)));
}

ll modpow(ll base, ll exp) {
    ll result = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

ll modinv(ll a){
    return modpow(a,MOD-2);
}

vi fact(MAXN);
void precomputeFact(){
    fact[0] = 1;
    for(int i=1; i<MAXN; i++){
        fact[i] = (fact[i-1]*i) % MOD;
    }
}

ll nCr(int n,int r){
    if(r>n || r<0) return 0;
    ll denom = (fact[r] * fact[n-r]) % MOD;
    return (fact[n]*modinv(denom)) % MOD;
}

vi spf(MAXN+1);
vi primes;
void sieve() {
    for (int i = 2; i <= MAXN; i++) spf[i] = i;
    for (int i = 2; i * i <= MAXN; i++) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
    for (int i = 2; i <= MAXN; i++)
        if (spf[i] == i) primes.push_back(i);
}

vi getPrimeFactors(int v) {
    vi pf;
    while (v > 1) {
        if (pf.empty() || pf.back() != spf[v])
            pf.push_back(spf[v]);
        v /= spf[v];
    }
    return pf;
}

int root(int x){
    while(x%2==0)x/=2;return x;
}
void solve(){

        int n;cin>>n;
        vector<int>a(n),b,pos(n+1);
        for(int i=0;i<n;i++)cin>>a[i];
        b=a;
        sort(b.begin(),b.end());
        for(int i=0;i<n;i++)pos[a[i]]=i;
        bool ok=1;
        for(int i=0;i<n;i++){
            if(a[i]!=b[i]&&root(i+1)!=root(pos[b[i]]+1)){
                ok=0;
                break;
            }
        }
        cout<<(ok?"YES\n":"NO\n");

}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    sieve();
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}