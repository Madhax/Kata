class Solution {
public:
    set<long long int> numbers;
    
    long long int removeLast(long long int number)
    {
        return (number - (number%10))/10;
        
    }
    
    long long int removeFirst(long long int number, int level) {
        return number % (long long int) pow((double)10, (double)level);
    }
    
    void seedNumbers(long long int number, int length) {
        if(length==0) return;
        numbers.insert(number);
        seedNumbers(removeLast(number), length-1);
        seedNumbers(removeFirst(number, length), length-1);
    }
    
    vector<int> sequentialDigits(int low, int high) {
        vector<int> output;
        long long int seed = 123456789;
        seedNumbers(seed, 9);
        for (auto iter : numbers)
        {
            if(iter >= low && iter <= high) {
                output.push_back(iter);
            }
        }
        
        std::sort (output.begin(), output.end());  
        return output;
    }
};