def function() -> None :
    with open('C:/Users/MrYep/Desktop/Book-SocialMediaMiningPython/MyLearning/IO/text02.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(line.strip())
            '''
            1.with usage: 
                replace try-finally
                this is equals to:
                     try:
                         f = open('text01.txt', 'r', encoding='utf-8')
                         for line in f.readlines():
                             print(line.strip())
                     finally:
                         f.close()
                         
            2.line.strip() usage:
                remove whitespace
            '''

if __name__ == '__main__':
    function()
