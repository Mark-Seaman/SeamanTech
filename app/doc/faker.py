from random import randrange

first = '''Mark
Stacie
Christine
Josiah
Rachel
Jennifer
Jessica
Sarah
Eric
Mike
Brad''' .split('\n')

last  = '''Watkins
Prill
Seaman
Smith
Johnson
Obama
Putin
Watt
Williams''' .split('\n')

adjectives  = '''
Selected
First
Strategic
Federal
State
Major
'''  .split('\n')

nouns = '''Supplies
Insurance
Systems
Partnership
Bank
Hospital
Consortium''' .split('\n')

streets = '''Maple
Oak
Olive
Mullberry
Pine
Aspen
Cherry''' .split('\n')


# Select from a list of choices
def pick(selections):
    return selections[randrange(len(selections))]

# Pick a few random digits
def pick_digits(digits=4):
    return ''.join([ str(randrange(10)) for i in range(digits) ])


# Fake names
def fake_name():
    return pick(first) +' '+ pick(last)

# Fake ID numbers
def fake_ID_number():
    return  pick_digits()

# Fake ID numbers
def fake_phone_number():
    return  pick_digits(3) +'-'+ pick_digits(3) +'-'+ pick_digits()

# Fake address
def fake_address():
    return fake_ID_number() +' '+ pick(streets) + ' Ave'

# Company names
def fake_company():
    return pick(adjectives) +' '+  pick(adjectives) +' '+  pick(nouns)


# Create random employees and companies
def test_code():
    for i in range(100):
        print '#%s, %s, %s (%s)'%(fake_ID_number(), fake_name(), fake_address(),fake_company())
