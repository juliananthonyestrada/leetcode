class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # each acc begins in its own set - is its own representative
        representatives = {i : i for i in range(len(accounts))}
        rank = [1 for i in range(len(accounts))]

        # find representative of each set
        def find(acc1: int) -> int:
            while acc1 != representatives[acc1]:
                acc1 = representatives[acc1]
            return acc1

        # combine 2 sets 
        def union(acc1: int, acc2: int) -> None:
            par1, par2 = find(acc1), find(acc2)
            if par1 == par2:
                return
            elif rank[par1] < rank[par2]:
                representatives[par1] = par2
                rank[par2] += rank[par1]
            else:
                representatives[par2] = par1
                rank[par1] += rank[par2]


        # map each email to the acc it belongs to
        emailToAcc = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in emailToAcc:
                    emailToAcc[email] = i
                # email belongs to 2 accounts - connect them
                else:
                    union(i, emailToAcc[email])
                
        # representative : list of emails
        emailGroup = defaultdict(list)
        for email, i in emailToAcc.items():
            representative = find(i)
            emailGroup[representative].append(email)
    
        res = []
        for i, group in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + group)
        
        return res




