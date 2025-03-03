art = '''                                                             
                                        _       _                
                                      (_)     | |               
   ___ __ _  ___  ___  ___ _ __    ___ _ _ __ | |__   ___ _ __  
  / __/ _` |/ _ \/ __|/ _ \ '__|  / __| | '_ \| '_ \ / _ \ '__| 
 | (_| (_| |  __/\__ \  __/ |    | (__| | |_) | | | |  __/ |    
  \___\__,_|\___||___/\___|_|     \___|_| .__/|_| |_|\___|_|    
                                        | |                     
                                        |_|                                                               

'''
print(art)





alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(given_text,given_shift,given_direction):
    caeser_text = ''
    text_str = [i for i in text]
    for i in range(len(text_str)):
        for j in range(len(alphabets)):
            
            if text_str[i] == alphabets [j]:
                if direction == 'encode':
                    caeser_text += alphabets[(j+shift)%26]
                elif direction == 'decode':
                    caeser_text += alphabets[(j-shift)%26]
                break
        else:
            caeser_text += text_str[i]
    print(f'The {direction}d text is :\n {caeser_text}')
caeser(text,shift,direction)

while True:
    ask = input("Type 'yes' to play again or 'no' to quit\n")
    if ask == 'yes':
        
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caeser(text,shift,direction)
        
    else:
        print('Thanks for Playing!')
        break
