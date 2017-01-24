import sgmllib

class MyParser(sgmllib.SGMLParser):
    "A simple parser class."

    def parse(self, s):
        "Parse the given string 's'."
        self.feed(s)
        self.close()

    def __init__(self, verbose=0):
        "Initialise an object, passing 'verbose' to the superclass."

        sgmllib.SGMLParser.__init__(self, verbose)
        self.hyperlinks = []
        self.usefulldata = []
        self.d= []
        self.inside_a_element = 0
        

    def start_a(self, attributes):
        "Process a hyperlink and its 'attributes'."
        for name, value in attributes:
            if name == "href":
                self.hyperlinks.append(value)
                self.inside_a_element = 1

    def handle_data(self, data):
        "Handle the textual 'data'."
        
        #for k in range(len(data)):
        #data(k)=data(k)+ ' '

        #d=data.split(' ')
        #d=data+"AAA"
        self.usefulldata.append(data)
        self.usefulldata.append(" ")
        #if self.inside_a_element:
            #self.descriptions.append(s)
                
    def get_hyperlinks(self):
        "Return the list of hyperlinks."

        return self.hyperlinks

    def get_data(self):
        "Return the list of data."

        return ''.join(self.usefulldata)

    def end_a(self):
        "Record the end of a hyperlink."

        self.inside_a_element = 0

    def get_descriptions(self):
        "Return a list of descriptions."
        return self.d

        
