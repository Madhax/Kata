# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek
# https://www.youtube.com/watch?v=VLwVU3Bi0Ek

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = [row[:] for row in matrix]
        order = sorted([(matrix[i][j],i,j) for i in range(len(matrix)) for j in range(len(matrix[0]))])
        row,col=[0]*len(matrix),[0]*len(matrix[0])
        idx = 0
        def get_groups(lst):
            # take list of ij
            dic = defaultdict(list)
            # group by i
            i_dic = defaultdict(list)
            j_dic = defaultdict(list)
            for idx in range(len(lst)):
                i_dic[lst[idx][0]].append(idx)
            for idx in range(len(lst)):
                j_dic[lst[idx][1]].append(idx)
            for entry in i_dic.values():
                for idx in range(len(entry)-1):
                    dic[entry[idx]].append(entry[idx+1])
                    dic[entry[idx+1]].append(entry[idx])
            for entry in j_dic.values():
                for idx in range(len(entry)-1):
                    dic[entry[idx]].append(entry[idx+1])
                    dic[entry[idx+1]].append(entry[idx])
            # print(dic)
            ret = []
            seen = set()
            def dfs(idx):
                if idx in seen:
                    return
                seen.add(idx)
                ret[-1].append(lst[idx])
                for nxt in dic[idx]:
                    dfs(nxt)
            for idx in range(len(lst)):
                if idx in seen:
                    continue
                ret.append([])
                dfs(idx)
            return ret
            
                
        while idx < len(order):
            val = order[idx][0]
            # they all get the same shit
            locs = []
            
            while idx < len(order) and order[idx][0] == val:
                i,j=order[idx][1],order[idx][2]
                # new_val = max(new_val,row[i]+1,col[j]+1)
                locs.append([i,j])
                idx += 1
            # figure out new val for these by group
            groups = get_groups(locs)
            # print(groups)
            for grp in groups:
                new_val = 1
                for i,j in grp:
                    new_val = max(new_val,row[i]+1,col[j]+1)
                for i,j in grp:
                    ret[i][j] = new_val
                    row[i] = new_val
                    col[j] = new_val
        return ret
                
        # 1 2
        # 3 3
        
        # 1 2
        # 3 3