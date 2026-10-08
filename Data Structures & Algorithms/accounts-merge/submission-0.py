class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # each acc begins in its own set
        parents = {i : i for i in range(len(accounts))}

        def find(acc1: int) -> int:
            # traverse to parent of group - rep of the set
            while acc1 != parents[acc1]:
                acc1 = parents[acc1]
            return acc1

        def union(acc1: int, acc2: int) -> None:
            par1, par2 = find(acc1), find(acc2)

            if par1 == par2:
                return
            else:
                # implement by rank
                parents[par1] = par2

        # map each email to the acc it belongs to
        emailToAcc = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in emailToAcc:
                    emailToAcc[email] = i
                else:
                    union(i, emailToAcc[email])
        
        emailGroup = defaultdict(list)
        for email, i in emailToAcc.items():
            parent = find(i)
            emailGroup[parent].append(email)
    
        res = []
        for i, group in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + group)
        
        return res




