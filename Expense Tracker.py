def add_expense(expenses, amount, category): #Adicionar uma nova despesa
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses): #Imprimir as despesas salvas
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses): #Calcular e retornar o valor total de despesas
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category): #Filtrar as despesas por categoria
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main(): #Lista para salvar as despesas
    expenses = []
    while True: #Mostrar todas as opções do menu
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1': #Pegar o valor e a categoria que o usuário quer adicionar
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2': #Imprimir todas as despesas
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3': #Mostrar o total de gastos
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4': #Filtrar por categoria e mostrar
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5': #Fechar o programa
            print('Exiting the program.')
            break
if __name__ == "__main__":
    main()
