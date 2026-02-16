#include<bits/stdc++.h>
using namespace std;

int root(int x){while(x%2==0)x/=2;return x;}

void solve(){
    int t;cin>>t;
    while(t--){
        int n;cin>>n;
        vector<int>a(n),b,pos(n+1);
        for(int i=0;i<n;i++)cin>>a[i];
        b=a;sort(b.begin(),b.end());
        for(int i=0;i<n;i++)pos[a[i]]=i;
        bool ok=1;
        for(int i=0;i<n;i++){
            if(a[i]!=b[i]&&root(i+1)!=root(pos[b[i]]+1)){
                ok=0;break;
            }
        }
        cout<<(ok?"YES\n":"NO\n");
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
