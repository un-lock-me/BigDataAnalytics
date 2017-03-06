
import java.io.{File, ByteArrayInputStream}
import java.net.InetSocketAddress
import javax.imageio.ImageIO

import com.sun.net.httpserver.{HttpExchange, HttpHandler, HttpServer}
import sun.misc.BASE64Decoder

object SimpleHttpServer extends App{
    val server = HttpServer.create(new InetSocketAddress(8088), 0)
    server.createContext("/get_custom", new RootHandler())
    server.setExecutor(null)
    server.start()
  println("------ waiting for Request ------")
}

class RootHandler extends HttpHandler {
  def handle(httpExchange: HttpExchange) {
    val data = httpExchange.getRequestBody
    val imageByte = (new BASE64Decoder()).decodeBuffer(data);
    val bytes = new ByteArrayInputStream(imageByte)
    val image = ImageIO.read(bytes)
    ImageIO.write(image, "png", new File("image.png"))
    println("------ Image receiving complete ------")

    val response = IPApp.testImage("image.png")

    httpExchange.getResponseHeaders().add("Access-Control-Allow-Origin", "*")
    httpExchange.sendResponseHeaders(200, response.length())
    val outStream = httpExchange.getResponseBody
    outStream.write(response.getBytes)
    outStream.close()
    }
}
