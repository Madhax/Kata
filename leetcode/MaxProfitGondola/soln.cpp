class Solution {
public:
    int minOperationsMaxProfit(vector<int>& customers, int boardingCost, int runningCost) {
        int maxProfit = 0;
        int pendingCustomers = 0;
        int customerIteration = 0;
        int bestRotation = -1;
        int currentProfit = 0;
        int currentRotation = 1;
        int totalCustomers = 0;
        while(customerIteration != customers.size() || pendingCustomers) {
            if(customerIteration < customers.size()) {
                pendingCustomers += customers[customerIteration];
                customerIteration++;
            }
            int currentGondola = min(pendingCustomers, 4);
            pendingCustomers -= currentGondola;
            totalCustomers += currentGondola;
            //cout << totalCustomers << " " << boardingCost << " " << currentRotation << " " << runningCost << "\n";
            currentProfit = (totalCustomers*boardingCost) - (currentRotation*runningCost);
            
            
            //cout << currentProfit << "\n";
            if(currentProfit > maxProfit) {
                bestRotation = currentRotation;
                maxProfit = currentProfit;
            }
            
            currentRotation++;
            
        }
        
        return bestRotation;
    }
};
