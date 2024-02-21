from func.utils import load_operations_list
from func.utils import sorted_operations
from func.utils import last_operations



print("5 последних выполненных Вами операций:\n")
def main():
    data = load_operations_list('../operations.json')
    last_five_operations = sorted_operations(data)[:5]
    print(last_operations(last_five_operations))

if __name__ == "__main__":
    main()

