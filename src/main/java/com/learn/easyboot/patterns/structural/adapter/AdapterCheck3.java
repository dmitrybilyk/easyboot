package com.learn.easyboot.patterns.structural.adapter;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class AdapterCheck3 {
	public static void main(String[] args) {
		SomeCoolService service = new SomeCoolService();
		SomeClientService clientService = new SomeClientService();

		List<String> listToPrint = clientService.returnsList();
		//service.coolPrint(listToPrint);

		ServiceAdapter adapter = new DoubleCoolServiceAdapter(service);
		adapter.printAdaptedList(listToPrint);
	}
}

class SomeCoolService {
	void coolPrint(String toPrint) {
		System.out.println(toPrint);
	}
}

class SomeClientService {
	List<String> returnsList() {
		return Arrays.asList("1", "2");
	}
}

interface ServiceAdapter {
	void printAdaptedList(List<String> listToPrint);
}

class CoolServiceAdapter implements ServiceAdapter {
	private SomeCoolService someCoolService;
	public CoolServiceAdapter(SomeCoolService someCoolService) {
		this.someCoolService = someCoolService;
	}
	public void printAdaptedList(List<String> listToPrint) {
		StringBuilder stringBuilder = new StringBuilder();
		for(String string: listToPrint) {
			stringBuilder.append(string);
		}
		someCoolService.coolPrint(stringBuilder.toString());
	}
}

class DoubleCoolServiceAdapter implements ServiceAdapter {
	private SomeCoolService someCoolService;
	public DoubleCoolServiceAdapter(SomeCoolService someCoolService) {
		this.someCoolService = someCoolService;
	}
	public void printAdaptedList(List<String> listToPrint) {
		StringBuilder stringBuilder = new StringBuilder();
		for(String string: listToPrint) {
			stringBuilder.append(string);
		}
		someCoolService.coolPrint(stringBuilder.toString());
		someCoolService.coolPrint(stringBuilder.toString());
	}
}