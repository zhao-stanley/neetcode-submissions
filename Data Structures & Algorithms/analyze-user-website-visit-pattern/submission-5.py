class Solution:
    def getSubseqs(self, arr: List[str], k: int):
        if k == 0:
            return [[]]
        if len(arr) < k:
            return []

        take = [[arr[0]] + tail for tail in self.getSubseqs(arr[1:], k-1)]
        skip = self.getSubseqs(arr[1:], k)

        return take + skip

    
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patterns = {}

        data = sorted(zip(timestamp, username, website))
        user_sites = {}
        

        for _, u, w in data:
            if u in user_sites:
                user_sites[u].append(w)
            else:
                user_sites[u] = [w]

            
        for sites in user_sites.values():
            user_subseqs = set(tuple(seq) for seq in self.getSubseqs(sites, 3))
            for subseq in user_subseqs:
                key = tuple(subseq)
                if key not in patterns:
                    patterns[key] = 1
                else:
                    patterns[key] += 1
        best_pattern, max_score = [], 0

        for pattern, score in patterns.items():
            if score > max_score or (score == max_score and pattern < best_pattern):
                best_pattern = pattern
                max_score = score
        
        return list(best_pattern)
        

