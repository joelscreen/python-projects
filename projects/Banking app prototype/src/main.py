import customtkinter as ctk
from PIL import Image, ImageTk
import datetime
import random

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("My Application")
app.geometry("400x300")

canvas = ctk.CTkCanvas(app, width=2048, height=1024, bg="#2b2b2b", highlightthickness=0)
canvas.pack()

username = ""
password = ""
loanHistory = []

def clearWidgets(exclude=[]):
    for widget in app.winfo_children():
        if widget not in exclude:
            widget.destroy()

def enableFullscreen(event=None):
    app.attributes("-fullscreen", True)

def disableFullscreen(event=None):
    app.attributes("-fullscreen", False)

enableFullscreen()

def mainPageSetup():
    global balance, timesLoan

    timesLoan = 0

    balance = round(random.uniform(1000, 10000), 2)

    mainPage()

def fixedDepositInterestRates():
    global amountToBeDepositedSlider, amountToBeDepositedEntry, amountToBeDeposited

    moneyTransfer1_label.destroy()
    transferAmount.destroy()
    AEDLabel.destroy()
    checkRates.destroy()
    creditCardBalance.destroy()
    loanButton_label.destroy()
    loanContinue1.destroy()
    destination.destroy()
    creditCard_label.destroy()
    loanRequest1.destroy()
    welcomeLabel.destroy()
    fixedDepositInterestCalculator.destroy()

    amountToBeDeposited = 0

    ctk.CTkLabel(app, text="Fixed Deposit Interest Rates Calculator:", font=("Arial", 24)).place(x=700, y=100)

    amountToBeDepositedSlider = ctk.CTkSlider(app, width=800, from_=25000, to=10000000, command=lambda value: amountToBeDeposited==value)
    amountToBeDepositedSlider.place(x=1000, y=205)

    amountToBeDepositedSlider.set(1000)

    amountToBeDepositedEntry_var = ctk.StringVar(value=str(amountToBeDepositedSlider.get()))
    amountToBeDepositedEntry = ctk.CTkEntry(app, font=("Arial", 17), textvariable=amountToBeDepositedEntry_var, width=200)
    amountToBeDepositedEntry.place(x=700, y=250)

    amountToBeDeposited_label = ctk.CTkLabel(app, text=f"Amount to be deposited: {amountToBeDepositedSlider.get()} AED", font=("Arial", 17))
    amountToBeDeposited_label.place(x=700, y=200)

    interestPayout = ctk.CTkLabel(app, text="Interest Payout: ", font=("Arial", 17))
    interestPayout.place(x=700, y=310)

    interestRatesCalculatorDropDown = ctk.CTkComboBox(app, font=("Arial", 14), values=["On Maturity", "Monthly", "Quarterly"])
    interestRatesCalculatorDropDown.place(x=840, y=310)

    interestRateEntry = ctk.CTkEntry(app, placeholder_text="Interest Rates... ( Please Enter a float eg:- 2.3, 5.0, etc. )", width=350)
    interestRateEntry.place(x=840, y=400)

    ctk.CTkLabel(app, font=("Arial", 17), text="Interest:").place(x=700, y=400)

    def showInterestRates():
        if interestRateEntry.get() and amountToBeDepositedEntry.get() != "":
            interestRate = float(interestRateEntry.get())
            amountToBeDeposited = float(amountToBeDepositedEntry.get())

            ctk.CTkLabel(app, font=("Arial", 24), text="Interest Rates").place(x=1400, y=300)
            ctk.CTkLabel(app, font=("Arial", 24), text=f"{interestRate}% Per Annum").place(x=1400, y=350)
            ctk.CTkLabel(app, font=("Arial", 24), text=f"Total Amount: {interestRate/100*amountToBeDeposited+amountToBeDeposited}").place(x=1400, y=400)

        else:
            ctk.CTkLabel(app, font=("Arial", 14), text="Invalid Input", fg_color="#ff0000", corner_radius=8).place(x=1400, y=350)

    def update_entry_from_slider(value):
        amountToBeDepositedEntry_var.set(str(int(value)))
        amountToBeDeposited_label.configure(text=f"Amount to be deposited: {int(value)} AED")

    def update_slider_from_entry(*args):
        try:
            val = float(amountToBeDepositedEntry_var.get())
            amountToBeDepositedSlider.set(val)
            amountToBeDeposited_label.configure(text=f"Amount to be deposited: {int(val)} AED")
        except ValueError:
            pass

    amountToBeDepositedSlider.configure(command=update_entry_from_slider)
    amountToBeDepositedEntry_var.trace_add("write", update_slider_from_entry)

    continue_button = ctk.CTkButton(app, text="Calculate", font=("Arial", 14), command=showInterestRates)
    continue_button.place(x=1060, y=1000)

def quitApp():
    ctk.CTkLabel(app, font=("Arial", 14), text="Thank you for using the TKinter Banking App", fg_color="#00FF00", corner_radius=8).place(x=790, y=900)
    app.after(5000, lambda: app.destroy())

def mainPage():
    global welcomeLabel, destination, transferAmount, balance, username, password, message_label, main_details_label
    global creditCard_label, moneyTransfer1_label, user_icon_label, currentDate, chances, checkRates, AEDLabel, creditCardBalance
    global loanButton_label, loanRequest1, user_icon_label, loanContinue1, initialLoanAmount, fixedDepositInterestCalculator

    balance = round(balance, 2)

    quitAppButton = ctk.CTkButton(app, text="Quit App", font=("Arial", 14), command=quitApp)
    quitAppButton.place(x=880, y=1000)

    mainPage_button = ctk.CTkButton(app, text="Main Page", font=("Arial", 14), command=mainPage)
    mainPage_button.place(x=700, y=1000)

    clearWidgets(exclude=[canvas, mainPage_button, quitAppButton])
    
    welcomeLabel = ctk.CTkLabel(app, text="Welcome to the TKinter Banking App", font=("Arial", 24), fg_color="transparent")
    welcomeLabel.place(x=700, y=100)
    
    ctk.CTkButton(app, text="Login", font=("Arial", 14), command=login, fg_color="#0042A5").place(x=1800, y=100)

    main_details = Image.open("assets/main_details.png")
    main_details = main_details.resize((600, 1400))
    main_details_photo = ImageTk.PhotoImage(main_details)

    main_details_label = ctk.CTkLabel(app, image=main_details_photo, text="")
    main_details_label.place(x=0, y=0)

    currentDate = datetime.datetime.now().strftime("Account created: %Y-%m-%d %H:%M")

    user_icon = Image.open("assets/user_icon.png")
    user_icon = user_icon.resize((50, 50))
    user_icon_photo = ImageTk.PhotoImage(user_icon)

    user_icon_label = ctk.CTkLabel(app, image=user_icon_photo, text="")
    user_icon_label.place(x=50, y=100)
    ctk.CTkLabel(app, text=f"{username}", font=("Arial", 30), fg_color="#353535", text_color="#FFFFFF").place(x=130, y=80)

    ctk.CTkLabel(app, text=currentDate, font=("Arial", 14), fg_color="#353535", text_color="#FFFFFF").place(x=130, y=120)
    ctk.CTkLabel(app, text=f"AED {balance}", font=("Arial", 40), fg_color="#353535", text_color="#FFFFFF").place(x=50, y=200)

    creditCard = Image.open("assets/credit_card.png")
    creditCard = creditCard.resize((400, 250))
    creditCard_photo = ImageTk.PhotoImage(creditCard)

    creditCard_label = ctk.CTkLabel(app, image=creditCard_photo, text="")
    creditCard_label.place(x=680, y=170)

    loanButton = Image.open("assets/loan_button.png")
    loanButton = loanButton.resize((400, 250))
    loanButton_photo = ImageTk.PhotoImage(loanButton)

    loanButton_label = ctk.CTkLabel(app, image=loanButton_photo, text="")
    loanButton_label.place(x=680, y=440)

    loanRequest1 = ctk.CTkEntry(app, font=("Arial", 14), placeholder_text="Enter loan amount...", width=250, height=33)
    loanRequest1.place(x=700, y=540)

    loanContinue1 = ctk.CTkButton(app, text="Continue", font=("Arial", 14), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=loanSetup)
    loanContinue1.place(x=730, y=600)

    creditCardBalance = ctk.CTkLabel(app, text=f"AED {balance}", font=("Arial", 40), fg_color="#000000", text_color="#FFFFFF")
    creditCardBalance.place(x=710, y=365)

    moneyTransfer1 = Image.open("assets/money_transfer_1.png")
    moneyTransfer1 = moneyTransfer1.resize((400, 250))
    moneyTransfer1_photo = ImageTk.PhotoImage(moneyTransfer1)

    moneyTransfer1_label = ctk.CTkLabel(app, image=moneyTransfer1_photo, text="")
    moneyTransfer1_label.place(x=1100, y=170)

    transferAmount = ctk.CTkEntry(app, font=("Arial", 14), placeholder_text="Enter amount")
    transferAmount.place(x=1130, y=330)
    
    AEDLabel = ctk.CTkLabel(app, text="AED", font=("Arial", 20), fg_color="#d8d4d4")
    AEDLabel.place(x=1400, y=330)

    destination = ctk.CTkComboBox(app, values=["India", "Australia", "USA"], font=("Arial", 14), width=250)
    destination.place(x=1130, y=250)

    checkRates = ctk.CTkButton(app, text="                              Check Rates                              ", font=("Arial", 14), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=transferDetails)
    checkRates.place(x=1130, y=375)

    fixedDepositInterestCalculator = ctk.CTkButton(app,
                                                    text="Fixed Deposit Interest Calculator",
                                                    font=("Arial", 14), text_color="#000000",
                                                    corner_radius=10,
                                                    height=50,
                                                    command=fixedDepositInterestRates
                                                    )
    fixedDepositInterestCalculator.place(x=1600, y=1000)

    def repay_loan(amount, total_returned):
        global balance, loanHistory
        if balance < total_returned:
            insufficientBalanceLoan = ctk.CTkLabel(app, text="Insufficient balance to repay loan!", font=("Arial", 14), fg_color="#FF0000", corner_radius=8)
            insufficientBalanceLoan.place(x=700, y=800)
            app.after(1000, lambda: insufficientBalanceLoan.destroy())
            return
        balance -= total_returned
        loanHistory.remove(total_returned)
        mainPage()

    y_offset = 700
    for loan_total in loanHistory:
        loan_btn = ctk.CTkButton(app,
            text=f"Repay Loan: AED {loan_total}",
            font=("Arial", 14),
            fg_color="#FFAA00",
            text_color="#000000",
            corner_radius=10,
            command=lambda amt=loan_total: repay_loan(amt, amt)
        )
        loan_btn.place(x=700, y=y_offset)
        y_offset += 50

def loanSetup():
    global initialLoanAmount

    initialLoanAmount = ctk.StringVar(value=loanRequest1.get())

    moneyTransfer1_label.destroy()
    transferAmount.destroy()
    AEDLabel.destroy()
    checkRates.destroy()
    creditCardBalance.destroy()
    loanButton_label.destroy()
    loanContinue1.destroy()
    destination.destroy()
    creditCard_label.destroy()
    loanRequest1.destroy()
    welcomeLabel.destroy()

    loan1()

def loan1():
    global loanAmount_label, loanAmount, loanType_Label, loanType, loanContinue2

    loanAmount_label = ctk.CTkLabel(app, font=("Arial", 24), text="Loan Amount")
    loanAmount_label.place(x=700, y=100)

    loanAmount = ctk.CTkEntry(app, font=("Arial", 14), textvariable=initialLoanAmount)
    loanAmount.place(x=700, y=140)

    loanType_Label = ctk.CTkLabel(app, font=("Arial", 24), text="Loan Type")
    loanType_Label.place(x=700, y=200)

    loanType = ctk.CTkComboBox(app, width=200, values=["Personal: 10-12% interest", "Property: 8-10% interest", "Vehicle: 4-5% interest"])
    loanType.place(x=700, y=240)

    loanContinue2 = ctk.CTkButton(app, font=("Arial", 14), command=loan2, text="Continue")
    loanContinue2.place(x=700, y=300)

def loan2():
    global proceedToRequest, interest, interest_label, loanAmount, totalMoneyReturned_Label, totalMoneyReturned, amountLoan

    if loanAmount == "":
        loanAmount = 0

    amountLoan = float(loanAmount.get())

    typeOfLoan = loanType.get()

    loanAmount.destroy()
    loanAmount_label.destroy()
    loanType_Label.destroy()
    loanType.destroy()
    loanContinue2.destroy()

    if typeOfLoan == "Personal: 10-12% interest":
        interest = round(random.uniform(10, 12), 2)
        totalMoneyReturned = round(interest/100*amountLoan+amountLoan, 2)

        interest_label = ctk.CTkLabel(app, font=("Arial", 24), text=f"Interest: {interest}%")
        interest_label.place(x=700, y=80)

        totalMoneyReturned_Label = ctk.CTkLabel(app, font=("Arial", 24), text=f"Total Money to be returned: {totalMoneyReturned}")
        totalMoneyReturned_Label.place(x=700, y=150)

        proceedToRequest = ctk.CTkButton(app, font=("Arial", 20), text="Proceed to Request Loan", command=finalLoan)
        proceedToRequest.place(x=700, y=220)

    elif typeOfLoan == "Property: 8-10% interest":
        interest = round(random.uniform(10, 12), 2)
        totalMoneyReturned = round(interest/100*amountLoan+amountLoan, 2)

        interest_label = ctk.CTkLabel(app, font=("Arial", 24), text=f"Interest: {interest}")
        interest_label.place(x=700, y=80)

        totalMoneyReturned_Label = ctk.CTkLabel(app, font=("Arial", 24), text=f"Total Money to be returned: {totalMoneyReturned}")
        totalMoneyReturned_Label.place(x=700, y=120)

        proceedToRequest = ctk.CTkButton(app, font=("Arial", 20), text="Proceed to Request Loan", command=finalLoan)
        proceedToRequest.place(x=700, y=220)
    else:
        interest = round(random.uniform(10, 12), 2)
        totalMoneyReturned = round(interest/100*amountLoan+amountLoan, 2)

        interest_label = ctk.CTkLabel(app, font=("Arial", 24), text=f"Interest: {interest}")
        interest_label.place(x=700, y=160)

        totalMoneyReturned_Label = ctk.CTkLabel(app, font=("Arial", 24), text=f"Total Money to be returned: {totalMoneyReturned}")
        totalMoneyReturned_Label.place(x=700, y=120)

        proceedToRequest = ctk.CTkButton(app, font=("Arial", 20), text="Proceed to Request Loan", command=finalLoan)
        proceedToRequest.place(x=700, y=220)

def finalLoan():
    global balance, timesLoan

    loanRequestDone = ctk.CTkLabel(app, text="Your loan has been requested", font=("Arial", 14), fg_color="#09FF00", corner_radius=8)
    loanRequestDone.place(x=710, y=280)

    timesLoan += 1

    balance += amountLoan

    loanHistory.append(totalMoneyReturned)

    app.after(2000, mainPage)
    
def goBack():
    backButton.destroy()
    proceedButton.destroy()
    sendingToLabel.destroy()
    areSending.destroy()
    receiverGets.destroy()
    exchangeRate.destroy()

    transfer()

def finalTransfer():
    global balance, sendingMoney

    if balance < float(sendingAmount):
        insufficientBalanceLabel = ctk.CTkLabel(app, text="Insufficient Balance!", font=("Arial", 14), fg_color="#FF0000", text_color="#000000", corner_radius=8)
        insufficientBalanceLabel.place(x=900, y=400)
    else:
        balance -= float(sendingAmount)

        mainPage()

def reviewTransfer():
    global confirmTransfer, backButton, proceedButton, sendingToLabel, areSending, receiverGets, exchangeRate

    receiverBankInfo.destroy()
    continue2.destroy()
    selectBank.destroy()
    accountNumber.destroy()
    IFSCCode.destroy()

    confirmTransfer = ctk.CTkLabel(app, text="Review transfer", font=("Arial", 24), fg_color="transparent", text_color="#000000")
    confirmTransfer.place(x=700, y=100)

    sendingToLabel = ctk.CTkLabel(app, text=f"Sending to: {country}", font=("Arial", 17), fg_color="transparent", text_color="#000000")
    sendingToLabel.place(x=730, y=150)

    areSending = ctk.CTkLabel(app, text=f"You are sending: AED {sendingAmount}", font=("Arial", 17), fg_color="transparent", text_color="#000000")
    areSending.place(x=730, y=200)

    receiverGets = ctk.CTkLabel(app, text=f"Receiver gets: {finalAmount} in {country}", font=("Arial", 17), fg_color="transparent", text_color="#000000")
    receiverGets.place(x=730, y=250)

    exchangeRate = ctk.CTkLabel(app, text=f"Exchange Rate: {rate}", font=("Arial", 17), fg_color="transparent", text_color="#000000")
    exchangeRate.place(x=730, y=300)

    backButton = ctk.CTkButton(app, text="                              Back                              ",
                                font=("Arial", 14),
                                fg_color="#FF0000",
                                text_color="#000000",
                                corner_radius=10,
                                command=goBack
    )
    backButton.place(x=730, y=350)

    proceedButton = ctk.CTkButton(app, text="                              Send money                              ",
                                  font=("Arial", 14),
                                  fg_color="#00FF00",
                                  text_color="#000000",
                                  corner_radius=10,
                                  command=finalTransfer
    )
    proceedButton.place(x=1070, y=350)

def transfer():
    creditCard_label.destroy()
    moneyTransfer1_label.destroy()
    destination.destroy()
    transferAmount.destroy()
    checkRates.destroy()
    AEDLabel.destroy()
    creditCardBalance.destroy()
    welcomeLabel.destroy()
    loanRequest1.destroy()
    loanButton_label.destroy()
    loanContinue1.destroy()

    global country, amount, rate, sendMoney, willSend, willSendEntry, willGet, willGetLabel, continue1, sendVar, finalAmount

    if country == "India":
        rate = 24.0

        finalAmount = float(amount) * rate

        sendMoney = ctk.CTkLabel(app, text="Send money to India", font=("Arial", 24), fg_color="transparent", text_color="#000000")
        sendMoney.place(x=700, y=100)

        willSend = ctk.CTkLabel(app, text="I will send", font=("Arial", 17), fg_color="transparent", text_color="#000000")
        willSend.place(x=730, y=150)

        sendVar = ctk.StringVar(value=str(amount))

        willSendEntry = ctk.CTkEntry(app, font=("Arial", 17), textvariable=sendVar)
        willSendEntry.place(x=730, y=200)

        willGet = ctk.CTkLabel(app, text="My receiver gets", font=("Arial", 17), fg_color="transparent", text_color="#000000")
        willGet.place(x=1080, y=150)

        willGetLabel = ctk.CTkLabel(app, text=f"{float(amount) * rate}", font=("Arial", 17), fg_color="#FFFFFF", text_color="#000000")
        willGetLabel.place(x=1080, y=200)

        continue1 = ctk.CTkButton(app, text="                              Continue                              ",
                                   font=("Arial", 14),
                                   fg_color="#FFFF00",
                                   text_color="#000000",
                                   corner_radius=10,
                                   command=receiverDetails)
        continue1.place(x=900, y=300)

        def update_receiver(*args):
            try:
                typed_amount = float(sendVar.get())
                willGetLabel.configure(text=f"{typed_amount * rate:.2f}")
            except ValueError:
                willGetLabel.configure(text="0.00")

        sendVar.trace_add("write", update_receiver)

    if country == "Australia":
        rate = 0.42

        finalAmount = float(amount) * rate

        sendMoney = ctk.CTkLabel(app, text="Send money to Australia", font=("Arial", 24), fg_color="transparent", text_color="#000000")
        sendMoney.place(x=700, y=100)

        willSend = ctk.CTkLabel(app, text="I will send", font=("Arial", 17), fg_color="transparent", text_color="#000000")
        willSend.place(x=730, y=150)

        sendVar = ctk.StringVar(value=str(amount))

        willSendEntry = ctk.CTkEntry(app, font=("Arial", 17), textvariable=sendVar)
        willSendEntry.place(x=730, y=200)

        willGet = ctk.CTkLabel(app, text="My receiver gets", font=("Arial", 17), fg_color="transparent", text_color="#000000")
        willGet.place(x=1080, y=150)

        willGetLabel = ctk.CTkLabel(app, text=f"{float(amount) * rate}", font=("Arial", 17), fg_color="#FFFFFF", text_color="#000000")
        willGetLabel.place(x=1080, y=200)
        
        continue1 = ctk.CTkButton(app, text="                              Continue                              ",
                                   font=("Arial", 14),
                                   fg_color="#FFFF00",
                                   text_color="#000000",
                                   corner_radius=10,
                                   command=receiverDetails)
        continue1.place(x=900, y=300)

        def update_receiver(*args):
            try:
                typed_amount = float(sendVar.get())
                willGetLabel.configure(text=f"{typed_amount * rate:.2f}")
            except ValueError:
                willGetLabel.configure(text="0.00")

        sendVar.trace_add("write", update_receiver)

    if country == "USA":
        rate = 0.27

        finalAmount = float(amount) * rate

        sendMoney = ctk.CTkLabel(app, text="Send money to USA", font=("Arial", 24), fg_color="transparent", text_color="#000000")
        sendMoney.place(x=700, y=100)

        willSend = ctk.CTkLabel(app, text="I will send", font=("Arial", 17), fg_color="transparent", text_color="#000000")
        willSend.place(x=730, y=150)

        sendVar = ctk.StringVar(value=str(amount))

        willSendEntry = ctk.CTkEntry(app, font=("Arial", 17), textvariable=sendVar)
        willSendEntry.place(x=730, y=200)

        willGet = ctk.CTkLabel(app, text="My receiver gets", font=("Arial", 17), fg_color="transparent", text_color="#000000")
        willGet.place(x=1080, y=150)

        willGetLabel = ctk.CTkLabel(app, text=f"{float(amount) * rate}", font=("Arial", 17), fg_color="#FFFFFF", text_color="#000000")
        willGetLabel.place(x=1080, y=200)

        continue1 = ctk.CTkButton(app, text="                              Continue                              ",
                                   font=("Arial", 14),
                                   fg_color="#FFFF00",
                                   text_color="#000000",
                                   corner_radius=10,
                                   command=receiverDetails)
        continue1.place(x=900, y=300)

        def update_receiver(*args):
            try:
                typed_amount = float(sendVar.get())
                willGetLabel.configure(text=f"{typed_amount * rate:.2f}")
            except ValueError:
                willGetLabel.configure(text="0.00")

        sendVar.trace_add("write", update_receiver)

def transferDetails():
    global country, amount

    country = destination.get()
    amount = transferAmount.get()

    if amount == "":
        amount = 0

    transfer()

def receiverDetails():
    global receiverBankInfo, continue2, recievingMoney, selectBank, accountNumber, IFSCCode, sendingAmount
    
    sendingAmount = willSendEntry.get()

    sendMoney.destroy()
    willSend.destroy()
    willSendEntry.destroy()
    willGet.destroy()
    willGetLabel.destroy()
    continue1.destroy()

    receiverBankInfo = ctk.CTkLabel(app, text="Receiver Bank Information", font=("Arial", 24), fg_color="transparent", text_color="#000000")
    receiverBankInfo.place(x=700, y=100)

    if country == "India":
        ctk.CTkLabel(app, text="Bank Name:", font=("Arial", 17), fg_color="transparent", text_color="#000000").place(x=730, y=150)

        selectBank = ctk.CTkComboBox(app, values=["State Bank of India", "Bank of Baroda", "HDFC Bank", "ICICI Bank", "Axis Bank"], font=("Arial", 14), width=250)
        selectBank.place(x=870, y=150)

        ctk.CTkLabel(app, text="Account Number:", font=("Arial", 17), fg_color="transparent", text_color="#000000").place(x=730, y=200)

        accountNumber = ctk.CTkEntry(app, font=("Arial", 17), placeholder_text="Eg: 123456789012")
        accountNumber.place(x=870, y=200)

        ctk.CTkLabel(app, text="IFSC Code:", font=("Arial", 17), fg_color="transparent", text_color="#000000").place(x=730, y=250)

        IFSCCode = ctk.CTkEntry(app, font=("Arial", 17), placeholder_text="Eg: SBIN0001234")
        IFSCCode.place(x=870, y=250)

        continue2 = ctk.CTkButton(app, text="                              Continue                              ",
                                   font=("Arial", 14),
                                   fg_color="#FFFF00",
                                   text_color="#000000",
                                   corner_radius=10,
                                   command=reviewTransfer
        )
        continue2.place(x=900, y=300)

    if country == "USA":
        ctk.CTkLabel(app, text="Bank Name:", font=("Arial", 17), fg_color="transparent", text_color="#000000").place(x=730, y=150)

        selectBank = ctk.CTkComboBox(app, values=["Bank of America", "U.S. Bank", "PNC Bank", "Capital One", "TD Bank"], font=("Arial", 14), width=250)
        selectBank.place(x=870, y=150)

        ctk.CTkLabel(app, text="Account Number:", font=("Arial", 17), fg_color="transparent", text_color="#000000").place(x=730, y=200)

        accountNumber = ctk.CTkEntry(app, font=("Arial", 17), placeholder_text="Eg: 123456789012")
        accountNumber.place(x=870, y=200)

        ctk.CTkLabel(app, text="IFSC Code:", font=("Arial", 17), fg_color="transparent", text_color="#000000").place(x=730, y=250)

        IFSCCode = ctk.CTkEntry(app, font=("Arial", 17), placeholder_text="Eg: SBIN0001234")
        IFSCCode.place(x=870, y=250)

        continue2 = ctk.CTkButton(app, text="                              Continue                              ",
                                   font=("Arial", 14),
                                   fg_color="#FFFF00",
                                   text_color="#000000",
                                   corner_radius=10,
                                   command=reviewTransfer
        )
        continue2.place(x=900, y=300)

    if country == "Australia":
        ctk.CTkLabel(app, text="Bank Name:", font=("Arial", 17), fg_color="transparent", text_color="#000000").place(x=730, y=150)

        selectBank = ctk.CTkComboBox(app, values=["CommonWealth Bank", "National Australia Bank", "ING Australia", "Macquarie Bank"], font=("Arial", 14), width=250)
        selectBank.place(x=870, y=150)

        ctk.CTkLabel(app, text="Account Number:", font=("Arial", 17), fg_color="transparent", text_color="#000000").place(x=730, y=200)

        accountNumber = ctk.CTkEntry(app, font=("Arial", 17), placeholder_text="Eg: 123456789012")
        accountNumber.place(x=870, y=200)

        ctk.CTkLabel(app, text="IFSC Code:", font=("Arial", 17), fg_color="transparent", text_color="#000000").place(x=730, y=250)

        IFSCCode = ctk.CTkEntry(app, font=("Arial", 17), placeholder_text="Eg: INGA0001234")
        IFSCCode.place(x=870, y=250)

        continue2 = ctk.CTkButton(app, text="                              Continue                              ",
                                   font=("Arial", 14),
                                   fg_color="#FFFF00",
                                   text_color="#000000",
                                   corner_radius=10,
                                   command=reviewTransfer
        )
        continue2.place(x=900, y=300)


def guestMode():
    global username, password
    username = "Guest"
    password = "guest123"
    mainPageSetup()

def createAccount():
    for widget in app.winfo_children():
        widget.destroy()

    login_signup = Image.open("assets/login_signup_bg.png")
    login_signup = login_signup.resize((1000, 1200))
    login_signup_photo = ImageTk.PhotoImage(login_signup)
    label = ctk.CTkLabel(app, image=login_signup_photo, text="")
    label.place(x=950, y=0)

    ctk.CTkLabel(app, text="Username:", font=("Arial", 14), bg_color="transparent").place(x=680, y=479)
    ctk.CTkLabel(app, text="Password:", font=("Arial", 14), bg_color="transparent").place(x=680, y=514)
    ctk.CTkLabel(app, text="Confirm Password:", font=("Arial", 14), bg_color="transparent").place(x=630, y=544)

    ctk.CTkLabel(app, text="Please Signup to proceed", font=("Arial", 60), bg_color="transparent").place(x=100, y=380)

    usernameregister = ctk.CTkEntry(app, font=("Arial", 14))
    usernameregister.place(x=800, y=480)

    passwordregister = ctk.CTkEntry(app, font=("Arial", 14), show="*")
    passwordregister.place(x=800, y=512)

    confpasswordregister = ctk.CTkEntry(app, font=("Arial", 14), show="*")
    confpasswordregister.place(x=800, y=544)

    def requirements():
        global message_label, username, password

        message_label = None

        if message_label is not None:
            message_label.destroy()

        reg_u = usernameregister.get()
        reg_p = passwordregister.get()
        conf_reg_p = confpasswordregister.get()

        if reg_u == "" or reg_p == "" or conf_reg_p == "":
            text = "⚠️ Please fill in all details"
        elif reg_p != conf_reg_p:
            text = "⚠️ Passwords do not match"
        elif len(reg_p) < 8:
            text = "⚠️ Password must be at least 8 characters long"
        elif len(reg_u) < 5:
            text = "⚠️ Username must be at least 5 characters long"
        else:
            username = reg_u
            password = reg_p
            text = "✓ Account Created Successfully! Redirecting to Main Page..."

        if text != "✓ Account Created Successfully! Redirecting to Main Page...":
            message_label = ctk.CTkLabel(app, text=text, font=("Arial", 14), fg_color="#FF0000", corner_radius=8)
            message_label.place(x=630, y=620)
        else:
            message_label = ctk.CTkLabel(app, text=text, font=("Arial", 14), bg_color="#005c00", corner_radius=8)
            message_label.place(x=630, y=620)
            app.after(2000, mainPageSetup)

    register_button = ctk.CTkButton(app, text="Register", font=("Arial", 14), command=requirements)
    register_button.place(x=800, y=580)

    tempButton = ctk.CTkButton(app, text="Guest mode (for testing)", font=("Arial", 14), command=guestMode)
    tempButton.place(x=50, y=700)

def login():
    for widget in app.winfo_children():
        widget.destroy()

    login_signup = Image.open("assets/login_signup_bg.png")
    login_signup = login_signup.resize((1000, 1200))
    login_signup_photo = ImageTk.PhotoImage(login_signup)
    label = ctk.CTkLabel(app, image=login_signup_photo, text="")
    label.place(x=950, y=0)
        
    ctk.CTkLabel(app, text="Username:", font=("Arial", 14), fg_color="transparent").place(x=680, y=467)
    ctk.CTkLabel(app, text="Password:", font=("Arial", 14), fg_color="transparent").place(x=680, y=514)

    usernameregister = ctk.CTkEntry(app, font=("Arial", 14))
    usernameregister.place(x=800, y=480)

    passwordregister = ctk.CTkEntry(app, font=("Arial", 14), show="*")
    passwordregister.place(x=800, y=512)

    def logineErrors():

        message_label = None

        if message_label is not None:
            message_label.destroy()

        log_u = usernameregister.get()
        log_p = passwordregister.get()

        if log_u == "" or log_p == "":
            text = "⚠️ Please enter in all the details!!"
        elif log_u != username or log_p != password:
            text = "⚠️ Invalid username or password!! Please try again."
        else:
            text = "✓ Logged in Successfully! Redirecting to the main page..."

        if text != "✓ Logged in Successfully! Redirecting to the main page...":
            message_label = ctk.CTkLabel(app, text=text, font=("Arial", 14), fg_color="#ff0000")
            message_label.place(x=608, y=800)
        else:
            message_label = ctk.CTkLabel(app, text=text, font=("Arial", 14), fg_color="#005c00")
            message_label.place(x=608, y=800)
            app.after(2000, mainPage)

    register_button = ctk.CTkButton(app, text="Login", font=("Arial", 14), command=logineErrors)
    register_button.place(x=800, y=580)

createAccount()

app.bind("<Escape>", disableFullscreen)
app.bind("<F11>", enableFullscreen)

app.mainloop()

