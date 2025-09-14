class llms:

    def __init__(self, query):
        self.query = query
        self.token_size = 100

    def openai(self):
        print(f'I am openai. You asked {self.query}')

    def claude(self):
        print('I am claude')

    def llama(self):
        print('I am llama')
    
def main():
    bot = llms('How many points did the montreal canadiens have last season')
    bot.openai()
    bot.claude()


if __name__ == '__main__':
    main()