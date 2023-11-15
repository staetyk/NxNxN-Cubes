import NxN


algNames = {}


def convert(n: int = NxN.n, alg: str = "") -> str:
    alg = alg.upper().strip(" ")\
    .replace("(", "( ").replace(")", " )")
    

    global algNames
    if "=" in alg:
        alg = alg.split(" = ")
        if alg[0][0] not in "0123456789UDFBRLXYZ()'":
            alg[1] = f" {alg[1]} "
            for x, y in algNames.items():
                alg[1] = alg[1].replace(f" {x} ", f" {y} ")
            alg[1] = alg[1].strip(" ")
            algNames.update({alg[0] : alg[1]})
            
        else:
            raise Exception(f"'{alg[0]}' is not a valid alg name")
            
            
    elif alg[0] == "?":
        alg = alg.lstrip("?", "").strip(" ")
                print(f"\u001b[2J\u001b[H\u001b[m{alg} = {algNames[alg]}")
        input()
        return "NxN.display()"
            
    
    else:
        alg = f" {alg} "
        for x, y in algNames.items():
            alg.replace(f" {x} ", f" {y} ")
        alg = alg.strip(" ").split(" ")
        

    iterator = 0
    code = ""
    for step in alg:
        if step == "":
            continue

        elif step == "(":
            iterator += 1
            code += f"i{iterator} = 0\n{'  ' * (iterator - 1)}while True:\n{'  ' * iterator}i{iterator} += 1\n{'  ' * iterator}pass; "
            continue

        elif step[0] == ")":
            if not step[-1].isdigit():
                step += "1"
            code += f"pass\n{'  ' * iterator}if i{iterator} == {step[1:]}: break\n"
            iterator -= 1
            code += f"{'  ' * iterator}pass; "
            continue
            
        elif step[0] in "XYZ":
            if not step[-1].isalnum():
                step = step[:-1] + "3"
            elif step[-1].isalpha():
                step += "1"
            step += "(); "

        else:
            wide = "W" in step
            step = step.replace("W", "")
            
            if not step[-1].isalnum():
                step = step[:-1] + "3"
            elif step[-1].isalpha():
                step += "1"
            if step[0].isalpha():
                step = ("2" if wide else "1") + step

            layers = ""
            while step[0].isdigit():
                layers += step[0]
                step = step[1:]
            layers = int(layers)

            face = step[0]
            turns = int(step[1:])
            
            if layers > 1 and not wide:
                if face in "DBR":
                    layers = n - layers + 1
                    turns = 4 - turns
                if face in "UD":
                    face = "E"
                elif face in "FB":
                    face = "S"
                else:
                    face = "M"

            step = f"{face}{turns}({layers}); "

        code += "NxN." + step
        
    return code + "NxN.display()"


help = """• \u001b[1mHELP: \u001b[22;3mShows list of commands.\u001b[23m
• \u001b[1mRESET: \u001b[22;3mResets cube to solved state.\u001b[23m
• \u001b[1mEXIT: \u001b[22;3mTerminates program.\u001b[23m
• \u001b[1mRESIZE: \u001b[22;3mChanges size of cube.\u001b[23m
• \u001b[1mHISTORY: \u001b[22;3mShows past moves.\u001b[23m
• \u001b[1mCLEAR: \u001b[22;3mClears past moves.\u001b[23m

• \u001b[1mU: \u001b[22;3mTurns top layer 90° clockwise.\u001b[23m
• \u001b[1mD: \u001b[22;3mTurns bottom layer 90° clockwise.\u001b[23m
• \u001b[1mF: \u001b[22;3mTurns front layer 90° clockwise.\u001b[23m
• \u001b[1mB: \u001b[22;3mTurns back layer 90° clockwise.\u001b[23m
• \u001b[1mL: \u001b[22;3mTurns left layer 90° clockwise.\u001b[23m
• \u001b[1mR: \u001b[22;3mTurns right layer 90° clockwise.\u001b[23m
• \u001b[1mU': \u001b[22;3mTurns top layer 90° counterclockwise.\u001b[23m
• \u001b[1mU2: \u001b[22;3mTurns top layer 180°.\u001b[23m
• \u001b[1;4m#\u001b[24mU: \u001b[22;3mTurns \u001b[4m#\u001b[24mᵗʰ layer from the top 90° clockwise.\u001b[23m
• \u001b[1mUw: \u001b[22;3mTurns second layer from the top 90° clockwise.\u001b[23m
• \u001b[1;4m#\u001b[24mUw: \u001b[22;3mTurns top \u001b[4m#\u001b[24m layers 90° clockwise.\u001b[23m

• \u001b[1mX: \u001b[22;3mTurns entire cube 90° clockwise, relative to left layer.\u001b[23m
• \u001b[1mY: \u001b[22;3mTurns entire cube 90° clockwise, relative to top layer.\u001b[23m
• \u001b[1mZ: \u001b[22;3mTurns entire cube 90° clockwise, relative to front layer.\u001b[23m
• \u001b[1mX': \u001b[22;3mTurns entire cube 90° counterclockwise, relative to left layer.\u001b[23m
• \u001b[1mX2: \u001b[22;3mTurns entire cube 180°, relative to left layer.\u001b[23m

• \u001b[1mU F: \u001b[22;3mTurns top layer 90° clockwise, then turns front layer 90° clockwise.\u001b[23m
• \u001b[1m(\u001b[4m…\u001b[24m): \u001b[22;3Same as \u001b[4m…\u001b[24m.\u001b[23m
• \u001b[1m(\u001b[4m…\u001b[24m)\u001b[4m#\u001b[24m: \u001b[22;3mRuns through \u001b[4m…\u001b[24m a total of \u001b[4m#\u001b[24m times.\u001b[23m
• \u001b[1m: \u001b[22;3mRuns most recent moves again.\u001b[23m
• \u001b[1;4mname\u001b[24m = \u001b[4m…\u001b[24m: \u001b[22;3mDefines \u001b[4mname\u001b[24m as alias for \u001b[4m…\u001b[24m.\u001b[23m
• \u001b[1;4mname\u001b[24m: \u001b[22;3mRuns the algorithm that \u001b[4mname\u001b[24m is alias of.\u001b[23m
• \u001b[1m? \u001b[4mname\u001b[24m: \u001b[22;3mShows algorithm that \u001b[4mname\u001b[24m is alias of.\u001b[23m"""