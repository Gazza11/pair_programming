# Q 1
def get_name(person):
            return person['name']
#q2
def get_favourite_tv_show(person):
    return person['favourites']['tv_show']

#q3 
def likes_to_eat(person, snacks):
    for snack in person['favourites']['snacks']:
        if snacks == snack:
            return True
        
    return False
        # print(snack)
#q4
def add_friend(person, new_friend):
    person['friends'].append(new_friend)

# q5
def remove_friend(person, friend_gone):
    for friend in person['friends']:
        if friend == friend_gone:
            person['friends'].remove(friend)

#q6
def total_money(people_ls):
    total_money = 0
    for person in people_ls:
        total_money += person['monies']
    return total_money

#q7 
def l_money(lender, lendee, amount):
    lender['monies'] -= amount
    lendee['monies'] += amount

#q 8

def all_favourite_foods(person_ls):
    favourite_foods = []
    for person in person_ls:
        for snack in person['favourites']['snacks']:
            favourite_foods.append(snack)
    return favourite_foods

#q9

def find_no_friends(person_ls):
    no_friend_ls = []
    for person in person_ls:
        if len(person['friends']) == 0:
            no_friend_ls.append(person)
    return no_friend_ls
