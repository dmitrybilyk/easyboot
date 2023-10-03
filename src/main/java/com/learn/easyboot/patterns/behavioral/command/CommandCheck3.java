package com.learn.easyboot.patterns.behavioral.command;

import java.math.BigDecimal;

public class CommandCheck3 {
    public static void main(String[] args) {
        Bank bank = new InternationalBank();
//        bank.transferMoney("from account number", "to account number", BigDecimal.ONE);
        MoneyTransferCommand moneyTransferCommand = new InternationalMoneyTransfer(bank);
//        moneyTransferCommand.execute("fromAccountNumber", "toAccountNumber", BigDecimal.ONE);

        TransferInvoker transferInvoker = new TransferInvokerImpl(moneyTransferCommand);
//
//        TransferInvokerImpl transferInvoker =
//                new TransferInvokerImpl((fromAccount, toAccount, amount) ->
//                        System.out.println("executing " + fromAccount + toAccount + amount));

        boolean isTransferringAllowedNow = true;

        if (isTransferringAllowedNow) {
            transferInvoker.invokeTransfer("fromAccountNumber", "toAccountNumber", BigDecimal.ONE);
        } else {
            System.out.println("Not allowed to transfer money now");
        }
    }
}

interface MoneyTransferCommand {
    void execute(String fromAccount, String toAccount, BigDecimal amount);
}

class InternationalMoneyTransfer implements MoneyTransferCommand {
    Bank bank;
    public InternationalMoneyTransfer(Bank bank) {
        this.bank = bank;
    }

    @Override
    public void execute(String fromAccount, String toAccount, BigDecimal amount) {
        System.out.println("International transfer is in progress");
        bank.transferMoney(fromAccount, toAccount, amount);
    }
}

class LocalMoneyTransfer implements MoneyTransferCommand {
    Bank bank;
    public LocalMoneyTransfer(Bank bank) {
        this.bank = bank;
    }

    @Override
    public void execute(String fromAccount, String toAccount, BigDecimal amount) {
        System.out.println("Local transfer is in progress");
        bank.transferMoney(fromAccount, toAccount, amount);
    }
}

interface Bank {
    void transferMoney(String fromAccount, String toAccount, BigDecimal amount);
}

class InternationalBank implements Bank {

    @Override
    public void transferMoney(String fromAccount, String toAccount, BigDecimal amount) {
        System.out.println("Transferring money in the Private Bank from " + fromAccount + " to " + toAccount + " , amount is " + amount);
    }
}
class LocalBank implements Bank {

    @Override
    public void transferMoney(String fromAccount, String toAccount, BigDecimal amount) {
        System.out.println("Transferring money in the State Bank from " + fromAccount + " to " + toAccount + " , amount is " + amount);
    }
}

interface TransferInvoker {
    void invokeTransfer(String fromAccount, String toAccount, BigDecimal amount);
}

class TransferInvokerImpl implements TransferInvoker {
    MoneyTransferCommand moneyTransferCommand;

    public TransferInvokerImpl(MoneyTransferCommand moneyTransferCommand) {
        this.moneyTransferCommand = moneyTransferCommand;
    }

    public TransferInvokerImpl() {

    }

    @Override
    public void invokeTransfer(String fromAccount, String toAccount, BigDecimal amount) {
        moneyTransferCommand.execute(fromAccount, toAccount, amount);
    }
}