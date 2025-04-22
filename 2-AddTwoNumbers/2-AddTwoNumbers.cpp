// Last updated: 22/04/2025 16:53:58
class Solution {
public:
    bool isPalindrome(int x){
        int moitie = 0;
        int i =0;

        if(x<0 || x%10 == 0 && x != 0){
            return false;
        }

        while(x > moitie){
            moitie = moitie*10 + x%10;
            x/= 10;
            i++;
        }

        if(x == moitie){
             return true;
        }
        if(x == moitie/10){
            return true;
        }
        return false;
    }
};