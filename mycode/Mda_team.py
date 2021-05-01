def main():
    N = int(input())
    A = []
    B  = []
    C = []
    D = []
    E = []
    for i in range(N):
        a,b,c,d,e = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
        E.append(e)
    init_team = [max(A[:3]),max(B[:3]),max(C[:3]),max(D[:3]),max(E[:3])]
    if N == 3:
        print(min(init_team))
    else:
        init_team_stack = [0,1,2]
        special_team_stack = init_team_stack
        power = min(init_team)
        for j in range(3,N):
            for s in range(len(special_team_stack)):
                this_team_power = [0]*3
                if s == 0:
                    this_team_power[0] = min([max(A[special_team_stack[1]],A[special_team_stack[2]],A[j]),max(B[special_team_stack[1]],B[special_team_stack[2]],B[j]),max(C[special_team_stack[1]],C[special_team_stack[2]],C[j]),max(D[special_team_stack[1]],D[special_team_stack[2]],D[j]),max(E[special_team_stack[1]],E[special_team_stack[2]],E[j])])
                elif s == 1:
                    this_team_power[1] = min([max(A[special_team_stack[0]],A[special_team_stack[2]],A[j]),max(B[special_team_stack[0]],B[special_team_stack[2]],B[j]),max(C[special_team_stack[0]],C[special_team_stack[2]],C[j]),max(D[special_team_stack[0]],D[special_team_stack[2]],D[j]),max(E[special_team_stack[0]],E[special_team_stack[2]],E[j])])
                elif s == 2:
                    this_team_power[2] = min([max(A[special_team_stack[0]],A[special_team_stack[1]],A[j]),max(B[special_team_stack[1]],B[special_team_stack[0]],B[j]),max(C[special_team_stack[1]],C[special_team_stack[0]],C[j]),max(D[special_team_stack[1]],D[special_team_stack[0]],D[j]),max(E[special_team_stack[1]],E[special_team_stack[0]],E[j])])
                if max(this_team_power) >= power:
                    power = max(this_team_power)
                    del special_team_stack[this_team_power.index(max(this_team_power))]
                    special_team_stack.append(j)
        print(power)

if(__name__ == '__main__'):
    main()