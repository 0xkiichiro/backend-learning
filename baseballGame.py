ops = ["5", "-2", "4", "C", "D", "9", "+", "+"] 

def calculate_points(ops):
    points = []
    
    for op in ops:
        if op.isdigit() or "-" in op:
            points.append(int(op))
            print(points)
        else:
            if op == "C" and op != ops[0] and len(points) >= 1:
                points.pop()

            elif op == "D" and op != ops[0] and len(points) >= 1:
                points.append(points[-1]*2)

            elif op == "+" and op != ops[0] and len(points) >= 2:
                points.append(points[-1] + points[-2])

            print(points)
    return sum(points)





print(calculate_points(ops))
numb = "2"
print(numb.isdigit())
