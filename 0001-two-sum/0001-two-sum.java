class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hm=new HashMap<>();
        int idx1=-1,idx2=-1;
        for(int i=0;i<nums.length;i++)
        {
            hm.put(nums[i],i);
        }
        for(int i=0;i<nums.length;i++)
        {
            int val=target-nums[i];
            idx1=i;
            if(hm.containsKey(val)&&idx1!=hm.get(val))
            {
                idx2=hm.get(val);
                break;
            }
        }
        return new int[]{idx1,idx2};
    }
}