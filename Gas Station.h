class Solution {
public:
	int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
		if(!gas.size())
			return -1;
		vector<int> diff(gas.size());
		int total=0;
		for(int i=0;i<diff.size();i++)
		{
			diff[i]=gas[i]-cost[i];
			total+=diff[i];
		}
		if(total<0)
			return -1;
		int cur_max=diff[0],cur_min=diff[0],max_sum=cur_max,min_sum=cur_min;
		int start_id=0,max_id=0,min_id=0;
		for(int i=1;i<diff.size();i++)
		{
			if(cur_max<0)
			{
				cur_max=diff[i];
				start_id=i;
			}
			else
				cur_max=cur_max+diff[i];
			if(cur_max>max_sum)
			{
				max_id=start_id;
				max_sum=cur_max;
			}
			if(cur_min>0)
				cur_min=diff[i];
			else
				cur_min+=diff[i];
			if(cur_min<min_sum)
			{
				min_sum=cur_min;
				min_id=i;
			}
		}
		if(max_sum>total-min_sum)
			return max_id;
		else
			return (min_id+1)%diff.size();
    }
};