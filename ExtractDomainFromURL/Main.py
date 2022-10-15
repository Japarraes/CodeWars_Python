from Domain_nameV2 import *


def main():

    print(domain_name("http://github.com/carbonfive/raygun")) # github
    print(domain_name("http://www.zombie-bites.com")) # zombie-bites
    print(domain_name("https://www.cnet.com")) # cnet
    print(domain_name("http://google.com")) # google
    print(domain_name("http://google.co.jp")) # google
    print(domain_name("www.xakep.ru")) # xakep
    print(domain_name("https://youtube.com")) # youtube


if __name__ == "__main__":
    main()
