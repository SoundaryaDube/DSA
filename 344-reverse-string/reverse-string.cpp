class Solution {
public:
    void reverseString(vector<char>& s) {
        int i = 0, j;
        char temp;
        j = s.size() - 1;
        while(i<j){
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++;
            j--;
        }     
    }
};