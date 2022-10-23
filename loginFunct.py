def login():
    username = (input("Masukkan Username: ").upper())
    while True:
        try:
            x = int(input("Please enter a number: "))
            if x == 6969:
                print(username, " Berhasil Login")
                break
        except ValueError:
            print("Oops! Pin yang dimasukkan bukan angka. Try again...")