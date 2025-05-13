import sys
import nltk

def ntlk_install(username, password, proxy, port):
    nltk.set_proxy(f'http://{username}:{password}@{proxy}:{port}')
    nltk.download('punkt_tab')
    nltk.download('averaged_perceptron_tagger_eng')
    nltk.download('stopwords')

if __name__ == "__main__":
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    proxy = str(sys.argv[3])
    port = str(sys.argv[4])
    ntlk_install(username, password, proxy, port)