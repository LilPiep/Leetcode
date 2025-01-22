public class Solution {
    public string DecodeString(string s) {
        Stack<string> strings = new Stack<string>();
        Stack<int> numbers = new Stack<int>();

        string currentString = "";
        int currentNumber = 0;

        foreach(char c in s){
             if (c == '['){
                strings.Push(currentString);
                numbers.Push(currentNumber);
                currentString = "";
                currentNumber = 0;
            }
            else if(c == ']'){        
                currentString = strings.Pop() + string.Join("", Enumerable.Repeat(currentString, numbers.Pop()));                    
            }
            else if ( c-'0'<=9 && c - '0' >= 0){              
                currentNumber = currentNumber * 10 + (c - '0');
            }                    
            else{
                currentString += c;
            }                 
        }

        return currentString;
    }
}