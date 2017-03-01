def splitTheBill(group):
    total = 0
    no_of_frnd = len(group)
    for frnd in group:
        total += group[frnd]
    ans = group
    avg_spend_money = round(total*1.0 / no_of_frnd,2) 
    for i in ans:
        ans[i] = group[i] - avg_spend_money
    return ans
group = input("Enter a dictionay of spending Money \n input formate {'A':10,'B':5,'C':15} \n")
print splitTheBill(group)
