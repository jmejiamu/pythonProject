#Verb Application

from tkinter import *
IregularV = {
    "awake":
        {
            "Simple past:":"awoke","Past participle: ": "awoken"
        },

    "be":
        {
            "Simple past:":"was/were","Past participle: ": "been"
        },
    "beat":
        {

     	"Simple past: ":"beat","Past participle: ":"beaten"
        },
    "become":
        {

        "Simple past: ":"became","Past participle":"become"
        },
    "begin":
        {

     	"Simple past:":"began","Past participle":"begun"
        },

    "bend":
        {
            "Simple past: ":"bent","Past participle: ":"bent"
        },

    "bet":
        {
            "Simple past:" :"bet","Past participle: ":"bet"
        },
    "bid":
        {
            "Siple past:":"bid","Past participle: ":"bid"
        },
    "bite":
        {
            "Simple past:":"bit","Past participle: ":"bitten"
        },
    "blow":
        {
            "Simple past:":"blew","Past participle: ":"blown"
        },

    "break":
        {
            "Simple past:":"broke","Past participle:":"broken"
        },
    "bring":
        {
            "Simple past":"brought","Past participle:":"brought"
        },
    "broadcast":
        {
            "Simple past:":"broadcast","Past participle:":"broadcast"
        },
    "build":
        {
            "Simple past:":"built","Past participle:":"built"
        },
    "burn":
        {
            "Simple past:":"burned /burnt","Past participle:":"burned/burnt"
        },
    "buy":
        {
            "Simple past: ":"bought","Past participle:":"bought"
        },
    "catch":
        {
            "Simple past":"caught","Past participle":"caught"
        },
    "choose":
        {
            "Simple past:":"chose","Past participle:":"chosen"
        },
    "come":
        {
            "Simple past:":"came","Past participle: ":"come"
        },
    "cost":
        {
            "Simple past:":"cost","Past participle: ":"cost"
        },
    "cut":
        {
            "Simple past: ":"cut","Past participle: ":"cut"
        },
    "dig":
        {
            "Simple past:":"dug","Past participle: ":"dug"
        },
    "do":
        {
            "Simple past:":"did","Past participle: ":"done"
        },
    "draw":
        {
            "Simple past:":"drew","Past participle: ":"drawn"
        },
    "dream":
        {
            "Simple past":"dreamed/dreamt","Past participle":"dreamed/dreamt"
        },
    "drive":
        {
            "Simple past: ":"drove","Past participle":"driven"
        },
    "drink":
        {
            "Simple past:":"drank","Past participle:":"drunk"
        },
    "eat":
        {
            "Simple past:":"ate","Past participle: ":"eaten"
        },
    "fall":
        {
            "Simple past: ":"fell","Past participle: ":"fallen"
        },
    "feel":
        {
            "Simple past":"felt","Past participle:":"felt"
        },
    "fight":
        {
            "Simple past:":"fought","Past participle:":"fought"
        },
    "find":
        {
            "Simple past: ":"found","Past participle: ":"found"
        },
    "fly":
        {
            "Simple past":"flew","Past participle: ":"flown"
        },
    "forget":
        {
            "Simple past: ":"forgot",".Past participle: ":"forgotten"
        },
    "forgive":
        {
            "Simple past:":"forgave","Past pasrticiple: ":"forgiven"
        },
    "freeze":
        {
            "Simple past:":"froze","Past participle":"frozen"
        },
    "get":
        {
            "Simple past:":"got","Past participle: ":"got/gotten"
        },
    "give":
        {
            "Simple past:":"gave","Past participle: ":"given"
        },
    "go":
        {
            "Simple past:":"went","Past participle: ":"gone"
        },
    "grow":
        {
            "Simple past:":"grew","Past participle: ":"grown"
        },
    "hang":
        {
            "Simple past:":"hung","Past participle:":"hung"
        },
    "have":
        {
            "Simple past:":"had","Past participle: ":"had"
        },
    "hear":
        {
            "Simple past:":"heard","Past participle: ":"heard"
        },
    "hide":
        {
            "Simple past:":"hid","Past participle: ":"hidden"
        },
    "hit":
        {
            "Simple past:":"hit","Past participle: ":"hit"
        },
    "hold":
        {
            "Simple past:":"held","Past participle: ":"held"
        },
    "hurt":
        {
            "Simple past:":"hurt","Past participle: ":"hurt"
        },
    "keep":
        {
            "Simple past:":"kept","Past participle: ":"kept"
        },
    "know":
        {
            "Simple past:":"knew","Past participle: ":"known"
        },
    "lay":
        {
            "Simple past:":"laid","Past participle: ":"laid"
        },
    "lead":
        {
            "Simple past:":"led","Past participle: ":"led"
        },
    "learn":
        {
            "Simple past:":"learned/learnt","Past participle: ":"learned/learnt"
        },
    "leave":
        {
            "Simple past:":"left","Past participle: ":"left"
        },
    "lend":
        {
            "Simple past:":"lent","Past participle: ":"lent"
        },
    "let":
        {
            "Simple past:":"let","Past participle: ":"let"
        },
    "lie":
        {
            "Simple past:":"lay","Past participle: ":"lain"
        },
    "lose":
        {
            "Simple past:":"lost","Past participle: ":"lost"
        },
    "make":
        {
            "Simple past:":"made","Past participle: ":"made"
        },
    "mean":
        {
            "Simple past:":"meant","Past participle: ":"meant"
        },
    "meet":
        {
            "Simple past:":"met","Past participle: ":"met"
        },
    "pay":
        {
            "Simple past:":"paid","Past participle: ":"paid"
        },
    "put":
        {
            "Simple past:":"put","Past participle: ":"put"
        },
    "read":
        {
            "Simple past:":"read","Past participle: ":"read"
        },
    "ride":
        {
            "Simple past:":"rode","Past participle: ":"ridden"
        },
    "ring":
        {
            "Simple past:":"rang","Past participle: ":"rung"
        },
    "rise":
        {
            "Simple past:":"rose","Past participle: ":"risen"
        },
    "run":
        {
            "Simple past:":"ran","Past participle: ":"run"
        },
    "say":
        {
            "Simple past:":"said","Past participle: ":"said"
        },
    "see":
        {
            "Simple past:":"saw","Past participle: ":"seen"
        },
    "sell":
        {
            "Simple past:":"sold","Past participle: ":"sold"
        },
    "send":
        {
            "Simple past:":"sent","Past participle: ":"sent"
        },
    "show":
        {
            "Simple past:":"showed","Past participle: ":"showed/shown"
        },
    "shut":
        {
            "Simple past:":"shut","Past participle: ":"shut"
        },
    "sing":
        {
            "Simple past:":"sang","Past participle: ":"sung"
        },
    "sit":
        {
            "Simple past:":"sat","Past participle: ":"sat"
        },
    "sleep":
        {
            "Simple past:":"slept","Past participle: ":"slept"
        },
    "speak":
        {
            "Simple past:":"spoke","Past participle: ":"spoken"
        },
    "spend":
        {
            "Simple past:":"spent","Past participle: ":"spent"
        },
    "stand":
        {
            "Simple past:":"stood","Past participle: ":"stood"
        },
    "swim":
        {
            "Simple past:":"swam","Past participle: ": "swum"
        },
    "take":
        {
            "Simple past:":"took","Past participle: ":"taken"
        },
    "teach":
        {
            "Simple past:":"taught","Past participle: ":"taught"
        },
    "tear":
        {
            "Simple past:":"tore","Past participle: ":"torn"
        },
    "tell":
        {
            "Simple past:":"told","Past participle: ":"told"
        },
    "think":
        {
            "Simple past:":"thought","Past participle: ":"thought"
        },
    "throw":
        {
            "Simple past:":"threw","Past participle: ":"thrown"
        },
    "understand":
        {
            "Simple past:":"understood","Past participle: ":"understood"
        },
    "wake":
        {
            "Simple past:":"woke","Past participle: ":"woken"
        },
    "wear":
        {
            "Simple past:":"wore","Past participle: ":"worn"
        },
    "win":
        {
            "Simple past:":"won","Past participle: ":"won"
        },
    "write":
        {
            "Simple past:":"wrote","Past participle: ":"written"
        }
}

class Applicatio(Frame):
    def __init__(self, master):
        super(Applicatio,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #label welcome
        self.lbl = Label(self, text ="Verbs Convertion",fg = "red",font = ("Cambria",18))
        self.lbl.grid(row = 0 , column = 0, columnspan =2,sticky = W)

        #Label for verb entry
        self.lbl_vbr = Label(self,text = "Enter an irregular verb base form: ")
        self.lbl_vbr.grid(row = 1, column = 0, sticky = W)

        #entry's verb
        self.ent_vbr = Entry(self)
        self.ent_vbr.grid(row = 1, column = 1, sticky = W)


        #Ok button
        self.bttn = Button(self,text = "OK",command = self.reveal)
        self.bttn.grid(row = 2 , column = 0, sticky =W)

        #create a widgets to display the text
        self.vb_txt = Text(self, width = 35 , height =5, wrap = WORD)
        self.vb_txt.grid(row =3 , column = 0, columnspan= 2,sticky = W)

    def reveal(self):
        """Display the text based on the verb"""
        contents = self.ent_vbr.get().lower()

        if contents in IregularV:
            mess ='Base Form: '+contents+\
                  '\nSimple past: '+IregularV[contents]['Simple past:']+\
                  '\nPast participle: '+IregularV[contents]['Past participle: ']

        else:
            mess = "This is not a irregular verb"

        self.vb_txt.delete(0.0,END)
        self.vb_txt.insert(0.0,mess)

#create a window
root = Tk()
root.title("IRREGULAR VERB")
root.geometry("300x150")

app = Applicatio(root)

root.mainloop()
