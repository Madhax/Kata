class Solution {
public:
    long long int bestProduct = -1;
    vector<vector<int>> bestNegatives;
    vector<vector<int>> bestPositives;
    
    void recursive(vector<vector<int>>& grid, int row, int column, long long int product) {
        long long int currentProduct = grid[row][column] * product;
        //cout << row << " " << column << " " << product << "\n";
        if(row == grid.size()-1 && column == grid[0].size()-1 && currentProduct > bestProduct) {
            //cout << row << " " << column << "\n";
            //cout << currentProduct << "\n";
            bestProduct = currentProduct;
        }
        if(currentProduct <= 0 && bestNegatives[row][column] > currentProduct) {
            bestNegatives[row][column] = currentProduct;
        }
        else if(currentProduct >= 0 && bestPositives[row][column] < currentProduct) {
            bestPositives[row][column] = currentProduct;
        } else {
            return;
        }
        if(row < grid.size()-1) {
            recursive(grid, row+1, column, currentProduct);
        }
        if(column < grid[0].size()-1) {
            recursive(grid, row, column+1, currentProduct);
        }
    }
    
    int maxProductPath(vector<vector<int>>& grid) {
        int rows = grid.size();
        int columns = grid[0].size();
        vector<int> row1;
        vector<int> row2;
        for(int y = 0; y < rows; y++) {
            for(int x = 0; x < columns; x++) {
                row1.push_back(INT_MAX);
                row2.push_back(INT_MIN);
            }
            bestNegatives.push_back(row1);
            bestPositives.push_back(row2);
            row1.clear();
            row2.clear();
        }
        recursive(grid, 0, 0, 1);
        return bestProduct % (1000000007);
    }
};