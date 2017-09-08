class Solution {
public:
	int maxProfit(vector<int>& prices) 
	{
		int max_profit=0;
		int cur_stock=-1;
		for(int i=0;i<prices.size();i++)
		{
			if(i==0)
				cur_stock=0;
			else
			{
				if(prices[i]<prices[cur_stock])
					cur_stock=i;
				else if(prices[i]>prices[cur_stock])
				{
					max_profit+=(prices[i]-prices[cur_stock]);
					cur_stock=i;
				}
			}
		}
		return max_profit;
	}
};