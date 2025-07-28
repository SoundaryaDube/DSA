class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        int min = Integer.MAX_VALUE;
        List <String> result = new ArrayList <> ();
        for(int i = 0; i < list1.length; i++){
            for(int j = 0; j < list2.length; j++){
                if (list1[i].equals(list2[j])){
                    int current = i+j;
                    if (current < min){
                        min = current;
                        result.clear();
                        result.add(list1[i]);
                    }else if(current == min){
                        result.add(list1[i]);
                    }
                }
            }
        }
        return result.toArray(new String[0]);
    }
}