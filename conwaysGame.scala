object ConwaysGame {
  type initState = (Int, Int) => Boolean

  def live (init:initState, time:Int, x:Int, y:Int):Boolean = {
    if (time == 0) init(x,y)
    else { val resultCount = countNeighbors(init, time - 1, x, y);

    if (live(init, time - 1, x,y)) { 
      resultCount == 2 || resultCount == 3 
    }

    else resultCount == 3
      
    }
} 

val deltas = List((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
  def countNeighbors (init:initState, time:Int, x:Int, y:Int):Int = {
    deltas.map { case(dx,dy) => if (live(init, time, x+dx, y+dy)) 1 else 0 }.sum

  }

  def show (init: initState, time: Int, topY: Int, height: Int, leftX: Int, width: Int): String =
    Range(topY,topY - height,-1).map { y =>
      (leftX to (leftX + width)).map { x =>
         if (live(init,time,x,y)) "x" else " "
      }.mkString("")
    }.mkString("\n")

    val firstState: Map[(Int,Int),Boolean] = (0 to 10).flatMap { x => (0 to 10).map { case y => (x,y) -> scala.util.Random.nextBoolean }}.toMap
    def state1 (x: Int, y: Int): Boolean = firstState.get((x,y)).getOrElse(false)

    def first10 = (0 to 10).foreach { t => println(show(state1,t,15,20,-5,20)); println }
}

ConwaysGame.first10

