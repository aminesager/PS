for _ in range(int(input())):
    n = int(input())
    T=list(input())
    note = []
    
    for i in range(65,69):
        reponse = T.count(chr(i))
        note.append(min(n,reponse))

    print(sum(note))