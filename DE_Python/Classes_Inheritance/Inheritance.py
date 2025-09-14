from FirstClass import llms 

class ChatBot(llms):

    def __init__(self, model, query):
        self.model = model 
        llms.__init__(self, query)

    def ShowMe(self):
        print(f'I am calling {self.model}')
        llms.openai()

def main():
    obj_inherit = ChatBot('openai', "I am louis")
    obj_inherit.openai()

if __name__ == '__main__':
    main()
