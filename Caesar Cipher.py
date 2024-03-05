'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
 
 '''
 

import string


def action():
    global act_ion
    act_ion=input('Do you want to (e)ncrypt or (d)ecrypt?')
    if act_ion!='e' and act_ion!='d':
        print('please enter "e" or "d" here')
        action()

def key():
    global key_value
    try:
        key_value=int(input('Please enter the key (0 to 25) to use.'))
        if key_value<0 or key_value>25:
            print('please enter integer within range 0 to 25 here')
            key()
    except ValueError:
        print('Error! please enter integer here.')
        key()       
 
           
def Caesar():
    action()
    key()
    
    alphabet=list(string.ascii_uppercase)
    alphabet_double=alphabet+alphabet
    
    # encryption
    e_mes_cha=[]
    if act_ion=='e':   
        message=input('Enter the message to encrypt')
        mes_cha=list(message.upper())
        for cha in mes_cha:
            try:
                # method 1: double the alphabet
                e_cha=alphabet_double[alphabet.index(cha)+key_value]
                # method 2: 
                # cha==alphabet[alphabet.index(cha)+key_value-26]
                e_mes_cha.append(e_cha)
            except ValueError:
                e_mes_cha.append(cha)
    e_message=''.join(e_mes_cha) 
    print(e_message)
    
    
    # decryption
    d_mes_cha=[]
    if act_ion=='d':
        message=input('Enter the message to decrypt')
        mes_cha=list(message.upper())
        for cha in mes_cha:
            try:
                d_cha=alphabet[alphabet.index(cha)-key_value]
                d_mes_cha.append(d_cha)     
            except ValueError:
                d_mes_cha.append(cha)
    d_message=''.join(d_mes_cha) 
    print(d_message)
    

   
Caesar()   


