''' this program allows a user to :
    1.take input
    2.store values in variables
    2.break down the input
    3.Extract the key elements i.e. brackets , variables and boolean instructions
    4.Performs boolean operation
    '''

'''This funcion takes the input from the user and and breaks it into individual units of information
    in a list'''
variableStore={"Name" : [],
                  "Value": []}
def Input_breakdown():
    inputx = input("Enter : \n")
    temp_position = 0
    values =[]

    for i in range(len(inputx)) :
        temp_value = inputx[temp_position]
        values.append(temp_value)
        temp_position = temp_position + 1

    return(values)
    
    
    
    ''' the function below  scans through and notes the position of key eleMents which are the brackets, and the boolean operands
        that are in use, it then stores their positions in variables for the booleans and in lists for the brackets both square 
        and regular brackets '''

def element_detectionAndBreakdown(list):
    elements = Input_breakdown()
    brackets = []
    sbrackets = []
    A = []
    O = []
    N = []
    assign = 0

    for i in range(len(elements)):
        if elements[i]== "(":
            brackets.append(i)
        if elements[i]== ")":
            brackets.append(i)
        if elements[i]== "[":
            sbrackets.append(i)
        if elements[i] == "]":
            sbrackets.append(i)
        if elements[i] == "A":
            A.append(i)
        if elements[i] == "O":
            O.append(i)
        if elements[i] == "N":
            N.append(i)
        if elements[i] == "=":
            assign = i
        
    return [brackets , sbrackets , O , A ,  N , assign ,elements]


''' The function below  uses the broken down input and the positional information of all operands and brackets in the brockendown input to 
    perform boolean operations.'''
def the_merge():
    
    if len(sbrackets) != 0 :
        
        variable_store(sbrackets)
        elements = []
        #print(elements)
        print(variableStore["Name"])

    
    '''Dealing with input that is in brackets '''
    
    if len(brackets) != 0 :
       sub_list_brackets =elements[brackets[0]+1:brackets[1]-1]
       sub_list_brackets = the_Value_changer(sub_list_brackets)
       sub_list_brackets= boolean_solve(sub_list_brackets)
       if 1 in sub_list_brackets:
        sub_list_brackets = 1
       elif 0 in sub_list_brackets:
        sub_list_brackets = 0
        print( sub_list_brackets)
       
    

    return(print(elements))
    
   
def the_Value_changer(list):
    '''Changinging every T value to 1 and every F value to 0 '''
   
    elements=list
    for i in range(len(elements)):
        if elements[i]=="T":
            elements[i]=1
        if elements[i]=="F":
            elements[i]=0

    return (elements)   


    
def boolean_solve(list,list2):
    N=list[4]
    A=list[3]
    O=list[2]
    elements=list2

    for i in range(len(N)):
        elements[N[i]]= not_OP(elements[N[i]+1])
        elements[N[i]+1]=None
        elements = [ x for x in elements if x != None]
        print(elements)
        
        
      
    for i in range(len(A)):
        print(A)
        print(range(len(A)))
        print(elements[A[i]-1])
        print(elements[A[i]+1])
        print( (elements[A[i]]))
        elements[A[i]]= and_Op(elements[A[i]-1], elements[A[i]+1])
        print(elements[A[i]])
        elements[A[i]-1] = None
        elements[A[i]+1] = None
        elements = [ x for x in elements if x != None]
        
        
        print(elements)
    

    


    for i in range(len(O)):
            elements[O[i]]= or_Op(elements[O[i]-1], elements[O[i]+1])
            print(elements[O[i]])
            elements[O[i]-1] = None
            elements[O[i]+1] = None
            elements = [ x for x in elements if x != None]
            print(elements)
            
    
    return(elements)
        

    
def and_Op(condition1, condition2):
    Tcounter=0
    Fcounter=0
    if condition1 == 1:
        Tcounter = Tcounter+1
    elif condition1 == 0:
        Fcounter = Fcounter + 1
    if condition2 == 1:
        Tcounter = Tcounter+1
    elif condition2 == 0:
        Fcounter = Fcounter + 1
    print(Tcounter)
    print(Fcounter)
    if (Tcounter or Fcounter != 2):
        return 1 
    else : 
        return 0

def or_Op(condition1, condition2):
    Tcounter=0
    Fcounter=0
    if condition1 == 1:
        Tcounter = Tcounter+1
    elif condition1 == 0:
        Fcounter = Fcounter + 1
    if condition2 == 1:
        Tcounter = Tcounter+1
    elif condition2 == 0:
        Fcounter + 1
    
    if Tcounter or Fcounter == 1:
        return 1
    else:
        return 0

def not_OP(condition):
    if condition == 1:
        return 0
    elif condition == 0:
        return 1


    







## this function allows the user to store variables into the program
## we will use a dictionary for this case
def variable_store(list):
    '''variable extraction and assignment, here we use the values in Sbrackets to direct us to the variable since we know
        the the position of the first square bracket we therefore know that the next value is the variable name,then we get 
        the total length of the characters inbetween the square brackets, we then join  every terms to form the name.then we relate it to the term that comes after the "=" sign'''
    #brackets,sbrackets,O,A,N,assign, elements= element_detectionAndBreakdown()
    '''variableStore={"Name" : [],
                  "Value": []}'''
     
    if len(sbrackets) != 0 :
        #print(sbrackets)
        var_length = len(sbrackets)
        var_name = ''.join(elements[(sbrackets[0]+1):sbrackets[1]])
        if var_name  not in variableStore ["Name"]:

            variableStore["Name"].append(var_name)
            value_pos = sbrackets[1]
            #print(value_pos)
            new_value_pos = value_pos+2
            value = elements[new_value_pos]
            #print(value)
            #print(var_name)
            variableStore["Value"].append(value)
        else:
            return(variableStore[value])
    
    #if variable_store["Value"]==T:
def evaluate(expression):
    # Extract tokens from the input string
    tokens = element_detectionAndBreakdown(expression)
    
    # Convert tokens to boolean values
    boolean_values = the_Value_changer(tokens[-1])
    
    # Evaluate the boolean expression
    result = boolean_solve(tokens,boolean_values)
    
    # Return the result
    return result



#element_detectionAndBreakdown()
while 1/2 !=3:
    evaluate(Input_breakdown())
    
