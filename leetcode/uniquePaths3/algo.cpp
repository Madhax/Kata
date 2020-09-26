class Solution {

public:
  
int dfs(int r, int c, int count, vector<vector<int>>* grid) {

    if (r >= grid->size() || c >= (*grid)[0].size() || r < 0 || c < 0 || (*grid)[r][c] < 0)
        return 0;

    if ((*grid)[r][c] == 2 && count == 1) {
        return 1;
    }else if((*grid)[r][c] == 2)
        return 0;

    


    int temp = (*grid)[r][c];
    (*grid)[r][c] = -1;
    count--;
    int ans = dfs(r + 1, c, count, grid) +
    dfs(r - 1, c, count, grid) +
    dfs(r, c + 1, count, grid) +
    dfs(r, c - 1, count, grid);

    (*grid)[r][c] = temp;
  
    return ans;



}

int uniquePathsIII(vector<vector<int>>& grid) {
    pair<int, int> start;
    int count = 0;
    for (int i = 0; i < grid.size(); i++) {

        for (int j = 0; j < grid[0].size(); j++) {


            if (grid[i][j] == 1) {
                start.first = i;
                start.second = j;
                
            }
             if (grid[i][j] >= 0) {
                count++;

            }

        }
    }


  
    return dfs(start.first, start.second, count, &grid);
}
                 
                               
};