def arithmetic_arranger(problems, option=None):
    if type(problems[0]) == list:
        pr = problems[0]
    else:
        pr = problems
    top_num = []
    op = []
    bottom_num = []
    ans = []
    m = []
    #Length Error:
    if len(pr) > 5:
        return 'Error: Too many problems.'
        
    for i in pr:
        i = i.split()
        if i[1] == '-':
            top_num.append(i[0])
            op.append(i[1])
            bottom_num.append(i[2])
        else:
            top_num.append(i[0])
            op.append(i[1])
            bottom_num.append(i[2])
        m.append(max(len(i[0]),len(i[2])))
        
    #Operator Error:
    for i in op:
        if i == '*' or i == '/':
            return "Error: Operator must be '+' or '-'."
    #Digit Error:    
    for i in top_num:
        if not i.isdigit():
            return "Error: Numbers must only contain digits."
    for i in bottom_num:
        if not i.isdigit():
            return "Error: Numbers must only contain digits." 
    #Number Error:
    for i in top_num:
        if len(i) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    for i in bottom_num:
        if len(i) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    opt = 3
    if option == True:
        opt = 4
        for i in pr:
            i = i.split()
            if i[1] == '-':
                res = int(i[0]) - int(i[2])
                ans.append(str(res))
            else:
                res = int(i[0]) + int(i[2])
                ans.append(res)
    arranged_nums = ''
    for row in range(opt):                                
        if row == 0:
            for i in range(len(op)):
                arranged_nums += top_num[i].rjust(m[i]+2)
                arranged_nums += (' '*4)
            arranged_nums = arranged_nums[:-4]
            arranged_nums +='\n'
        if row == 1:
            for i in range(len(op)):
                arranged_nums += op[i]
                arranged_nums += bottom_num[i].rjust(m[i]+1)
                arranged_nums += (' '*4)
            arranged_nums = arranged_nums[:-4]
            arranged_nums += '\n'
        if row == 2:
            for i in range(len(op)):
                arranged_nums += ('-'*(m[i]+2))
                arranged_nums += (' '*4)
            arranged_nums = arranged_nums[:-4]
            arranged_nums += '\n'
        if row == 3:
            for i in range(len(op)):
                arranged_nums += str(ans[i]).rjust(m[i]+2)
                arranged_nums += (' '*4)
            arranged_nums = arranged_nums[:-4]
            arranged_nums += '\n'
    arranged_nums = arranged_nums[:-1]
    return arranged_nums
