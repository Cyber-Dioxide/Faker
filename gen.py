import faker
from files.colors import ran , g , lg , c ,w , y ,ly , r
red = r
from files.banner import banner , banner2 , clear
from files.sprint import sprint

clear()
banner()


def col(str , i=">"):
    print(f"{y}[{ran}{i}{y}] {w}{str}")


fake=faker.Faker()
def gen():
    print(fake.email())
    print(fake.job())
    print(fake.country())
    print(fake.name())
    print(fake.address())


def addr():
    addr = fake.address()
    col(addr)

def email():
    email = fake.email()
    return email

def country():
    con = fake.country()
    return con

def name():
    name = fake.name
    return name

def job():
    job = fake.job()
    return job

def profile():
    s = fake.profile()

    for k,v in s.items():
        return col(f"{red}{k} {c}: {w}{v}")

def menu():
    try:
        print("\n\n")
        col(i="1", str=f"{g}Fake {w}Address")
        col(i="2" , str=f"{g}Fake {w}Email")
        col(i="3" , str=f"{g}Fake {w}Job")
        col(i="4" , str=f"{g}Fake {w}Name")
        col(i="5" , str=f"{g}Fake {w}Random Gen")
        col(i="6" , str=f"{g}Fake {w}Country")
        col(i="7" , str=f"{g}Fake {w}Profile")

        choice = input(f"{y}root@gen ~> "+g)

        if choice > "7":
            col(i = "!" , str=f"{red}Invalid! {w}Therefore, more features will be added soon {ran}+_+")
            exit()

        ch_dic = {"1" : addr() , "2" : email(), "3" : job() , "4" : name() , "5" : gen() , "6" : country()
                  , "7" : profile()}


        col(str=ch_dic.get(choice))


    except KeyboardInterrupt:
        sprint(f"\n{g}Exiting...")
        exit()

    except ValueError:
        sprint(f"\n{r}Something went wrong! ")

no = ["n" , "no"]
yes = ["y" , "yes"]

cont = ""

while cont.lower() not in no:
    menu()

    cont = input(f"{r}[!]{w}Do you want to contine?{g}(y/n)")

    if cont in no:
        clear()
        col(str="\nDont forget to follow us...")
        banner2()




