from time import time #it will record the time


#function to check accuracy of the types text
def accuracy(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1] == words[i+1]) and (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors +=1
            else:
                errors += 1
    return errors 



def timeElapsed(stime,etime):
    time = etime - stime

    return time


def speedy (inprompt,stime,etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time

    return speed



if __name__ == "__main__":
    prompt = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. "

    print(f"Type this :- {prompt}")

    input("Press enter when you are ready to check your speed !!")

    stime = time()
    inprompt = input()
    etime = time()

    time = round(timeElapsed(stime,etime),2)
    speed = speedy(inprompt,stime,etime)*60
    # speed = speed*60
    error = accuracy(prompt)

    print(f"Total time taken : {time} seconds")
    print(f"Average typing speed : {speed} words per minute ")
    print(f"Errors made while typing : {error}")


     



    
