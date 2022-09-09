def intInput(question: str) -> int:
    while True:
        try:
            response = int(input(question + ' '))
            break
        except ValueError:
            print('Hiba! Kérlek egész számot adj meg.')
    return response

while True:
    operandCnt = intInput('Hány számot szeretnél összeadni?')
    if not operandCnt in range(2, 6):
        print('Hiba! Kérlek, egy 2 és 5 közötti számot adj meg.')
        continue
    break

sum = 0
for i in range(1, operandCnt+1):
    sum += intInput(f'{i}. szám:')

print(f'A megadott {operandCnt} szám összege: {sum}')
