
class GenericContainer<T, V, C> {

    public static void main(String[] args) {


        GenericContainer<String, Integer, String> stringContainer = new GenericContainer<>();
        stringContainer.setValue("Some String");
        stringContainer.setValue2(4);
        stringContainer.printValue();
        stringContainer.printValue2(7, "TTT");


        GenericContainer<Integer, String, Integer> integerContainer = new GenericContainer<>();
        integerContainer.setValue(3);
        integerContainer.setValue2("string");
        integerContainer.printValue();
        integerContainer.printValue2("Some stringggg", 4);
    }

    private T value;
    private V value2;
    
    public void setValue(T value) {
	   this.value = value;
	}


    public void setValue2(V value2) {
       this.value2 = value2;
    }

    public T getValue() {
        return this.value;
    }

    public void printValue() {
        System.out.println(value);
    }


    public <M> void printValue2(M m, C c) {
        System.out.println(value2);
        System.out.println(m instanceof String);
        System.out.println(c instanceof String);
    }





}


class Fruit {}
class Apple extends Fruit {}