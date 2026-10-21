class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        if (nums2.size() < nums1.size()) swap(nums2, nums1);
        
        int m = nums1.size();
        int n = nums2.size();

        int total = m + n;
        int half = total / 2;

        int left = 0;
        int right = m - 1;

        while (true) {

            int mid1 = floor((left + right) / 2.0); 
            int mid2 = half - mid1 - 2;

            int left1 = mid1 >= 0 ? nums1[mid1] : INT_MIN;
            int left2 = mid2 >= 0 ? nums2[mid2] : INT_MIN;

            int right1 = (mid1 + 1) < m? nums1[mid1 + 1] : INT_MAX;
            int right2 = (mid2 + 1) < n? nums2[mid2 + 1] : INT_MAX;

            if (left1 > right2) right = mid1 - 1;
            else if (left2 > right1) left = mid1 + 1;
            else {
                if (total % 2 == 1) return min(right1, right2);
                else return (max(left1, left2) + min(right1, right2))/2.0;
            }
        }

        return -1;
    }
};