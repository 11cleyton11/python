class Category:
    
    def __init__(self, category):
        self.category = category
        self.catname = category
        self.ledger = []
        self.spending = 0
        self.total = 0

    def __str__(self):
        title = f'{self.category}'
        while len(title) < 30:
            title = '*' + title + '*'
        for i in range(0, len(self.ledger)):
            amt = f"{self.ledger[i]['amount']:.2f}"
            desc = self.ledger[i]['description'][:23]
            line = desc.ljust(0) + amt.rjust(30 - len(desc))
            title = title + '\n' + line
        title = title + '\nTotal: ' + f"{float(self.total):.2f}"
            
        return title

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        self.total += amount

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.total -= amount
            self.spending += amount
            return True
        return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.catname}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        if amount <= self.total:
            return True
        return False

def create_spend_chart(categories):
    total_spending = 0
    for i in list(categories):
        total_spending += int(i.spending)
    output = 'Percentage spent by category\n'
    for i in range(100, -10, -10):
        output += f"{str(i).rjust(3)}|"
        for j in list(categories):
            if int(j.spending) / total_spending * 100 >= i:
                output += ' o '
            else:
                output += '   '
        output += ' \n'
    output += '    '
    for i in list(categories):
        output += '---'
    output += '-\n     '

    max_length = max(len(i.catname) for i in categories)
    fit = [i.catname.ljust(max_length) for i in categories]
    for i in range(max_length):
        row = [fit[j][i] for j in range(len(categories))]
        if i == max_length - 1:
            output += '  '.join(row).rstrip() + '  '
        else:
            output += '  '.join(row).rstrip() + '  \n     '

    print(output)
    return output

food = Category('Food')
food.deposit(1000, 'paycheck')
print(food.ledger)
food.withdraw(400)
print(food.total)

working = Category('working')
working.deposit(500)
food.transfer(250, working)
print(food.total)
print(working.total)
print(food.ledger[1])
print(food)

secondjob = Category('SecondJob')
secondjob.deposit(5000, 'shift at second job')
secondjob.withdraw(350, 'needed rent')

listcats = [food, working, secondjob]
create_spend_chart(listcats)

