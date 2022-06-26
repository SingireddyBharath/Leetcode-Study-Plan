class Solution
{
public:
    int pivotIndex(vector<int> &nums)
    {
        int n = nums.size();

        int total_sum = accumulate(nums.begin(), nums.end(), 0);

        vector<int> presum(n);

        int currsum = 0;
        for (int i = 0; i < n; i++)
        {
            currsum += nums[i];
            presum[i] = currsum;
        }

        for (int i = 0; i < n; i++)
        {
            int lsum = presum[i] - nums[i];
            int rsum = total_sum - presum[i];
            if (lsum == rsum)
                return i;
        }
        return -1;
    }
};