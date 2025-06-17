class Solution {
    public int minimumCoins(int[] arr, int k) {
        // code here
        Arrays.sort(arr);
        int n = arr.length;
        int[] prefix = new int[n+1];
        for(int i=0;i<n;i++){
            prefix[i+1] = prefix[i]+arr[i];
        }
        int ans = Integer.MAX_VALUE;
        for(int i=0;i<n;i++){
            int remLeft = prefix[i];
            int upper = upperBound(arr, arr[i]+k);
            int remRight = prefix[n]-prefix[upper] - (n-upper)*(arr[i]+k);
            ans=Math.min(ans, remLeft + remRight);
        }
        return ans;
    }
    static int upperBound(int[] arr, int v){
        int lo=0,hi = arr.length-1, ans=-1;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(arr[mid]<=v){
                lo=mid+1;
                ans=mid+1;
            }
            else {
                hi=mid-1;
            }
        }
        return ans;
    }
}