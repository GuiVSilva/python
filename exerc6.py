from smtpd import MailmanProxy


primeiro = int(input("Primeiro numero: "))
segundo = int(input("Segundo numero: "))
terceiro = int(input("Terceiro numero: "))
quarto = int(input("Quarto numero: "))
quinto = int(input("Quinto numero: "))

primeiro = 5
maior = primeiro

if segundo > maior:
  maior = segundo
if terceiro > maior:
  maior = terceiro
if quarto > maior:
  maior = quarto
if quinto > maior:
  maior = quinto

print("Maior: ", maior)        