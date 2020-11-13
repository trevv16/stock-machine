# Stock Machine

##### By: Trevor Njeru


A basic python command line program to simulate the major functions of a individual brokerage account.


# Features
- View/Create transfers
- View/purchase stock
- View transaction and purchase history
- View portfolio


# Architecture

## Portfolio (Class)
 - name
 - age
 - cash balance
 - total equity
 - shares[]
    - ticker symbol
    - date []
        - num of shares
        - price
        - total
    - total spent
    - total stock equity

    ### Methods
    - make_transfer() - initiates transfer from user's bank to brokerage account
    - record_transfer() - saves transfer data to history
    - view_transfer_history() - displays tranfer history
    
    - make_purchase() - creates purchase of stock
    - record_purchase() - 
    - view_transaction_history()

    - view_portfolio()

## Stock (Class)
 - ticker symbol
 - company name
 - current price
 - day change
 - history []
    - date
    - price
    - day change

### Methods
- view_stock()
- view_stock_history()

