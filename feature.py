def search_by_date_linear(transactions):
    date=input("enter search date: ")
    for transaction in transactions:
        if transaction ["date"]==date:
            return transaction
    return "transaction not found"

def sort_amount(transaction):
    n=len(transaction)
    for i in range(len(transaction)):
        for j in range (0,len(transaction)-1): 
            if int(transactions[j]["amount"])>transactions[j+1]["amount"]:
                transactions[j],transactions[j+1]=transactions[j+1],transactions[j]
    return transactions
# deleting the data of the particular date by taking the input
def delete_data(transactions):
    date=input("enter search date: ")
    for transaction in transactions:
        if transaction["date"]==date:
            transactions.remove(transaction)
        return transactions
#add the transaction
def add_data(transactions):
    date=input("enter the date ")
    amount=int(input("enter the amount"))
    description=input("enter the description")
    transaction={"date":date,"amount":amount,"description":description}
    transactions.append(transaction)
    return transactions
#sum the transaction
def sum_amount(transactions):
  year=input("enter the year: ") 
  s=0
  for dict in transactions:
    if dict['date'][0:4]==year:
      s+=dict['amount']
  return s


