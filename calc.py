#https://github.com/HorvathhMilanAlex/Calculator.git

import tkinter as tk
"""
from szekrény import kotel

nyakam.append(kotel)

labamalol.pop(szék)

"""
#Számoló fuggvenyek
ops = ["^","√","×","/","+","-"]

def Count(lon):
    terms = []
    sequence = ""
    sq_n = None
    for each in lon:
        if each not in ops:
            sequence += each
            
        else:           
            if sequence == "":
                return "Syntax error"
            
            if each == "√" and terms[-1] in ops:
                sq_n == 2
                
            terms.append(float(sequence))
            
            #Gyök
            if sq_n != None:
                terms.append("×")
                terms.append(sq_n)
                sq_n = None
                
            terms.append(each)       
            sequence = ""
    
    if sequence != "":
        terms.append(float(sequence))
    
    if terms[-1] in ops:
        return "Syntax error"
    
    i = 0
    while(len(terms) != 1):
        i += 1
        if terms[i] == "^":
            terms[i] = terms[i-1]**terms[i+1]
            terms.pop(i+1),terms.pop(i-1)
            i = 0
        elif terms[i] == "√":
            terms[i] = terms[i+1]**(1/terms[i-1])
            terms.pop(i+1),terms.pop(i-1)
            i = 0
        elif terms[i] == "×":
            terms[i] = terms[i-1]*terms[i+1]
            terms.pop(i+1),terms.pop(i-1)
            i = 0
        elif terms[i] == "/":
            try:
                terms[i] = terms[i-1]/terms[i+1]
                terms.pop(i+1),terms.pop(i-1)
                i = 0
            except:
                return "Mathematical error"
        elif terms[i] == "+":
            terms[i] = terms[i-1]+terms[i+1]
            terms.pop(i+1),terms.pop(i-1)
            i = 0
        elif terms[i] == "-":
            terms[i] = terms[i-1]-terms[i+1]
            terms.pop(i+1),terms.pop(i-1)
            i = 0

    return ''.join(str(term) for term in terms)

#Logaritmus
def logarithm(base,arg,exp):
    if "yy" in base+arg+exp:
        return "Syntax error"
    
    if base == "y":
        pass
    
    elif arg == "y":
        pass
    
    elif exp == "y":
        pass
    
    else:
        return "Syntax error"


#Ablak
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

#Szám kiiro
mp_text = ""
main_panel = tk.Label(window, text=mp_text, font="Arial")
main_panel.grid(column=0,columnspan=10,row=0,sticky="nw")

#Grid - glhf




#Gombok

#Szam gombok
num1 = tk.Button(window, text="1", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "1"))
num1.grid(column=0,row=1,sticky="nw")
num2 = tk.Button(window, text="2", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "2"))
num2.grid(column=1,row=1,sticky="nw")
num3 = tk.Button(window, text="3", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "3"))
num3.grid(column=2,row=1,sticky="nw")
num4 = tk.Button(window, text="4", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "4"))
num4.grid(column=0,row=2,sticky="nw")
num5 = tk.Button(window, text="5", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "5"))
num5.grid(column=1,row=2,sticky="nw")
num6 = tk.Button(window, text="6", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "6"))
num6.grid(column=2,row=2,sticky="nw")
num7 = tk.Button(window, text="7", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "7"))
num7.grid(column=0,row=3,sticky="nw")
num8 = tk.Button(window, text="8", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "8"))
num8.grid(column=1,row=3,sticky="nw")
num9 = tk.Button(window, text="9", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "9"))
num9.grid(column=2,row=3,sticky="nw")
num0 = tk.Button(window, text="0", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "0"))
num0.grid(column=0,row=4,sticky="nw")
point = tk.Button(window, text=".", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "."))
point.grid(column=1,row=4,sticky="nw")

#Operátor gombok
plus = tk.Button(window, text="+", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "+"))
plus.grid(column=3,row=1,sticky="nw")
minus = tk.Button(window, text="-", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "-"))
minus.grid(column=3,row=2,sticky="nw")
mult = tk.Button(window, text="x", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "×"))
mult.grid(column=3,row=3,sticky="nw")
div = tk.Button(window, text="/", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "/"))
div.grid(column=3,row=4,sticky="nw")
pw = tk.Button(window, text="^", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "^"))
pw.grid(column=4,row=1,sticky="nw")
sq = tk.Button(window, text="√", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text") + "√"))
sq.grid(column=4,row=2,sticky="nw")
bs = tk.Button(window, text="⌫", font="Arial", command=lambda: main_panel.config(text=main_panel.cget("text")[0:-1]))
bs.grid(column=4,row=3,sticky="nw")
eq = tk.Button(window, background="green", text="=", font="Arial", command=lambda: main_panel.config(text=Count(main_panel.cget("text"))))
eq.grid(column=4,row=4,sticky="nw")
ac = tk.Button(window,background="red" ,text="AC", font="Arial", command=lambda: main_panel.config(text=""))
ac.grid(column=2,row=4,sticky="nw")
# ent = tk.Button(window,background="red" ,text="AC", font="Arial", command=lambda: main_panel.config(text=""))
# ent.grid(column=2,row=4,sticky="nw")

#App ciklus
window.mainloop() 