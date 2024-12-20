pin = "1234"
balance = 1000.0

# Language dictionaries
languages = {
    "en": {
        "enter_pin": "Enter your PIN: ",
        "wrong_pin": "Incorrect PIN. Access denied.",
        "menu": "\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit",
        "choose_option": "Choose an operation (1-4): ",
        "balance": "Your balance is ${:.2f}",
        "enter_withdraw": "Enter amount to withdraw: ",
        "insufficient_balance": "Insufficient balance.",
        "withdraw_success": "Withdrawal successful. New balance: ${:.2f}",
        "enter_deposit": "Enter amount to deposit: ",
        "deposit_success": "Deposit successful. New balance: ${:.2f}",
        "thank_you": "Thank you for using the ATM. Goodbye!",
        "invalid_choice": "Invalid choice. Please try again."
    },
    "az": {
        "enter_pin": "PIN kodunuzu daxil edin: ",
        "wrong_pin": "Yanlış PIN. Giriş rədd edildi.",
        "menu": "\n1. Balansı yoxlayın\n2. Pul çıxarmaq\n3. Pul yatırmaq\n4. Çıxış",
        "choose_option": "Bir əməliyyat seçin (1-4): ",
        "balance": "Balansınız ${:.2f}",
        "enter_withdraw": "Çıxarılacaq məbləği daxil edin: ",
        "insufficient_balance": "Balans kifayət deyil.",
        "withdraw_success": "Çıxarma uğurlu oldu. Yeni balans: ${:.2f}",
        "enter_deposit": "Yatırılacaq məbləği daxil edin: ",
        "deposit_success": "Yatırma uğurlu oldu. Yeni balans: ${:.2f}",
        "thank_you": "ATM-dən istifadə etdiyiniz üçün təşəkkürlər. Sağ olun!",
        "invalid_choice": "Yanlış seçim. Zəhmət olmasa yenidən cəhd edin."
    },
    "ru": {
        "enter_pin": "Введите ваш PIN: ",
        "wrong_pin": "Неверный PIN. Доступ запрещён.",
        "menu": "\n1. Проверить баланс\n2. Снять деньги\n3. Пополнить\n4. Выход",
        "choose_option": "Выберите операцию (1-4): ",
        "balance": "Ваш баланс: ${:.2f}",
        "enter_withdraw": "Введите сумму для снятия: ",
        "insufficient_balance": "Недостаточно средств.",
        "withdraw_success": "Снятие успешно. Новый баланс: ${:.2f}",
        "enter_deposit": "Введите сумму для пополнения: ",
        "deposit_success": "Пополнение успешно. Новый баланс: ${:.2f}",
        "thank_you": "Спасибо за использование банкомата. До свидания!",
        "invalid_choice": "Неверный выбор. Попробуйте ещё раз."
    }
}

# Select language
print("Select your language / Dilinizi seçin / Выберите язык")
print("1. English\n2. Azərbaycan dili\n3. Русский")
language_choice = input("Enter choice (1-3): ")

if language_choice == "1":
    lang = "en"
elif language_choice == "2":
    lang = "az"
elif language_choice == "3":
    lang = "ru"
else:
    print("Invalid choice. Defaulting to English.")
    lang = "en"

# Main ATM functionality
texts = languages[lang]
entered_pin = input(texts["enter_pin"])
if entered_pin != pin:
    print(texts["wrong_pin"])
else:
    while True:
        print(texts["menu"])
        choice = input(texts["choose_option"])

        if choice == "1":
            print(texts["balance"].format(balance))
        elif choice == "2":
            amount = float(input(texts["enter_withdraw"]))
            if amount > balance:
                print(texts["insufficient_balance"])
            else:
                balance -= amount
                print(texts["withdraw_success"].format(balance))
        elif choice == "3":
            amount = float(input(texts["enter_deposit"]))
            balance += amount
            print(texts["deposit_success"].format(balance))
        elif choice == "4":
            print(texts["thank_you"])
            break
        else:
            print(texts["invalid_choice"])
