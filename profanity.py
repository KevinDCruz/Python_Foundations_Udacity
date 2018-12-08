import urllib
def read_text():
    quotes = open(r"C:\Users\Kevin D'Cruz\PycharmProjects\Python_Foundations_Udacity\movie_quotes.txt")
    file_content = quotes.read()
    quotes.close()
    check_profanity(file_content)

def check_profanity(text_to_check):
    connection = urllib.urlopen(r"http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()