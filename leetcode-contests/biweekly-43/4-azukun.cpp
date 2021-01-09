public class Solution {
        private static T[] Init<T>(int size) where T : new() { var ret = new T[size]; for (int i = 0; i < size; i++) ret[i] = new T(); return ret; }

    HashSet<int>[] g;
    List<int>[] tree;
    bool Add(int x, int y)
    {
        foreach (int e in tree[x])
            if (g[y].Contains(e))
                return Add(e, y);
        tree[x].Add(y);
        return true;
    }

    int Check(int x, int top)
    {
        int s = 0;
        foreach (int e in tree[x])
        {
            int ret = Check(e, top + 1);
            if (ret == -1)
                return -1;
            s += ret;
        }
        if (s + top != g[x].Count)
            return -1;
        return s + 1;
    }
    
    bool Check2(int x)
    {
        foreach (int e in tree[x])
            if (g[x].Count == g[e].Count || Check2(e))
                return true;
        return false;
    }

    public int CheckWays(int[][] a)
    {
        var set = new HashSet<int>();
        int m = a.Length;
        for (int i = 0; i < m; i++)
        {
            set.Add(a[i][0]);
            set.Add(a[i][1]);
        }

        var list = set.ToList();
        list.Sort();
        int n = list.Count;
        g = Init<HashSet<int>>(n);
        for (int i = 0; i < m; i++)
        {
            a[i][0] = list.BinarySearch(a[i][0]);
            a[i][1] = list.BinarySearch(a[i][1]);
            g[a[i][0]].Add(a[i][1]);
            g[a[i][1]].Add(a[i][0]);
        }

        var b = Enumerable.Range(0, n).ToArray();
        Array.Sort(b, (b1, b2) => g[b2].Count.CompareTo(g[b1].Count));

        tree = Init<List<int>>(n);
        int root = b[0];
        for (int i = 1; i < n; i++)
        {
            if (!g[b[i]].Contains(root) || !Add(root, b[i]))
                return 0;
        }

        if (Check(root, 0) == -1)
            return 0;

        return Check2(root) ? 2 : 1;
    }
}
