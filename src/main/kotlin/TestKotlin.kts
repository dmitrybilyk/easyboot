//import java.io.File
//import java.math.BigDecimal
//import java.util.Date
//
////    val readOnlyShapes = listOf("triangle", "square", "circle")
////    println("This list has ${readOnlyShapes.count()} items")
//
////val fruits = listOf("banana", "avocado", "apple", "kiwifruit")
////fruits
////    .filter { it.startsWith("a") }
////    .sortedBy { it }
////    .map { it.uppercase() }
////    .forEach { println(it) }
//
//val map = mapOf("a" to 1, "b" to 2, "c" to 3)
//
//for ((k, v) in map) {
//    println("$k -> $v")
//}
//
//fun testDeault(a: Int = 7, b: Int = 8) {
//    print(a + b)
//}
//
//testDeault()
//
//val catName: String by lazy{ getName() }
//
//println(catName)
//
//fun getName(): String {
//    return "my name"
//}
//println(catName)
//
//lateinit var dogName: String
//dogName = "ddd"
//println(dogName)
//
//var bd = BigDecimal.ONE
//
//fun Date.oneHundred(): BigDecimal {
//    return BigDecimal("100")
//}
//
//println(Date().oneHundred())
//
//infix fun Int.isGreater(value: Int): Boolean {
//    return this > value
//}
//
//println(12 isGreater 9)
//
//val files = File("Test").listFiles()
//
//println(files?.size ?: "no files")
//
//class Turtle {
//    fun penDown() = println("pen down")
//    fun penUp() = println("pen up")
//    fun turn(degrees: Double) = println("turn")
//    fun forward(pixels: Double) = println("forward")
//}
//
//val myTurtle = Turtle()
//with(myTurtle) { //draw a 100 pix square
//    penDown()
//    for (i in 1..4) {
//        forward(100.0)
//        turn(90.0)
//    }
//    penUp()
//}
//
////var b: Boolean? = getBoolean()
//
//fun getBoolean(): Boolean? = TODO("later")
//
//var e: Int = 10  // 1
//println(e)  // 2
//
////
////open class Tiger(val origin: String) {
////    fun sayHello() {
////        println("A tiger from $origin says: grrhhh!")
////    }
////}
////
////class SiberianTiger : Tiger("Siberia")                  // 1
////
////
////    val tiger: Tiger = SiberianTiger()
////    tiger.sayHello()
////
//
//
//open class Tiger(val origin: String) {
//    fun sayHello() {
//        println("A tiger from $origin says: grrhhh!")
//    }
//}
//
//class SiberianTiger : Tiger("Siberia")                  // 1
//
//    val tiger: Tiger = SiberianTiger()
//    tiger.sayHello()
//
//val empty = "test".let {               // 1
//    customPrint(it)                    // 2
//    it.isEmpty()                       // 3
//    println("last")
//    false
//}
//println(" is empty: $empty")
//
//fun customPrint(any: Any) {
//    println(any)
//}
//
//
//fun printNonNull(str: String?) {
//    println("Printing \"$str\":")
//
//    str?.let {                         // 4
//        print("\t")
//        customPrint(it)
//        println()
//    }
//}
//
//printNonNull(null)
//
//
//var v = "some object".run {
//    println("$length")
//    true
//}
//println(v)
//
//
//class Person(val name: String)
//
//val person = Person("Dmytro")
//
//with(person) {
//    println(name)
//}
//
