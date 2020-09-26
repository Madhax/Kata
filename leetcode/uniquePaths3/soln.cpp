class Solution {
public:
    int totalVisited = 0;
    map<pair<int, int>, bool> visitedEntries;
    int totalSpaces = 0;
    
    void DFS(vector<vector<int>>& grid, int y, int x) {
        //cout << y << " " << x << "\n";
        if(grid[y][x] == 2 && totalSpaces == visitedEntries.size()-1) {
            //cout << visitedEntries.size() << "\n";
            totalVisited++;
        }    
        visitedEntries[make_pair(y,x)] = true;
        if(y > 0 && grid[y-1][x] != -1 && visitedEntries.count(make_pair(y-1,x)) == 0) {
            DFS(grid, y-1, x);
        }
        if(x > 0 && grid[y][x-1] != -1 && visitedEntries.count(make_pair(y,x-1)) == 0) {
            DFS(grid, y, x-1);
        }
        if(y < grid.size()-1 && grid[y+1][x] != -1 && visitedEntries.count(make_pair(y+1,x)) == 0) {
            DFS(grid, y+1, x);
        }
        if(x < grid[0].size()-1 && grid[y][x+1] != -1 && visitedEntries.count(make_pair(y,x+1)) == 0) {
            DFS(grid, y, x+1);
        }
        visitedEntries.erase(make_pair(y,x));
    }
    
    int uniquePathsIII(vector<vector<int>>& grid) {
        int startx=0, starty=0;
        //cout << grid.size() << "\n";
        for(int y = 0; y < grid.size(); y++) {
            for(int x = 0; x < grid[0].size(); x++) {
                if(grid[y][x] == 0) {
                    totalSpaces++;
                    continue;
                }     
                if(grid[y][x] == 1) {
                    //cout << y << " " << x << "\n";
                    startx = x;
                    starty = y;
                }
            }
        }
        visitedEntries[make_pair(starty,startx)] = true;
        //cout << starty <<  " " << startx <<"\n";
        if(starty > 0 && grid[starty-1][startx] != -1) {
            DFS(grid, starty-1, startx);
        }
        if(startx > 0 && grid[starty][startx-1] != -1) {
            DFS(grid, starty, startx-1);
        }
        if(starty < grid.size()-1 && grid[starty+1][startx] != -1) {
            DFS(grid, starty+1, startx);
        }
        if(startx < grid[0].size()-1 && grid[starty][startx+1] != -1) {
            DFS(grid, starty, startx+1);
        }
        
        //cout << totalSpaces;
        return totalVisited;
    }
};