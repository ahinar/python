# Starter code
# try:
#     items = [1,2,3,4,5]
#     item = items[6]
#     print(item)
# except:
#     print("El elemento no existe en la lista")

# # Starter code
def divide_by(a, b):
    return a / b

try:
  ans = divide_by(40, 0)
  print(ans)
except Exception as e:
  print("No se puede dividir por 0...",e)

  # Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except Exception as e:
    print("Error",e)