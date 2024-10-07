import scala.collection.mutable
 
class Database {
  private val data: mutable.Map[String, String] = mutable.Map()
 
  def insert(key: String, value: String): Unit = {
    data(key) = value
  }
 
  def retrieve(key: String): Option[String] = {
    data.get(key)
  }
 
  def delete(key: String): Unit = {
    data.remove(key)
  }
 
  def displayAll(): Unit = {
    data.foreach { case (key, value) => println(s"$key: $value") }
  }
}
 
object DatabaseApp extends App {
  val db = new Database()
  db.insert("name", "Alice")
  db.insert("age", "30")
  db.insert("city", "New York")
  
  println("All entries in the database:")
  db.displayAll()
 
  println(s"Retrieve 'name': ${db.retrieve("name").getOrElse("Not found")}")
  
  db.delete("age")
  println("After deleting 'age':")
  db.displayAll()
}
