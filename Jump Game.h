class Solution {
public:
	bool canJump(vector<int>& nums) 
	{
		if(!nums.size())
			return false;
		int max_pos=-1;
		for(int i=0;i<nums.size();i++)
		{
			if(i==0)
				max_pos=nums[i];
			else
			{
				if(max_pos<i)
					return false;
				else
					max_pos=max(max_pos,i+nums[i]);
			}
		}
		return true;
	}
};