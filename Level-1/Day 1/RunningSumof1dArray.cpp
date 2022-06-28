class Solution
{
public:
    vector<int> runningSum(vector<int> &nums)
    {

        vector<int> res;

        int cs = 0;

        for (auto i : nums)
        {
            cs += i;
            res.emplace_back(cs);
        }
        return res;
    }
};
