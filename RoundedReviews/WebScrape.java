//import java.io.IOException;
import java.net.URLEncoder;
import java.lang.String;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class WebScrape {
   public static String Rating(String website, String restaurant, String area) {
      String site = website;
      String rating = "";
      try {
	Document doc;
	switch(site){
	 case "Yelp": 
		doc = Jsoup.connect("https://www.google.com/search?q=" + 
			 URLEncoder.encode(site + " " + restaurant + " " + area,  "UTF-8")).get();
      	 	 //rating = dot.select("img.offscreen").attr("alt");
		 Element b = doc.select("div.g").first();
		 rating = b.select("div.slp.f").first().text();
		 break;
	 case "Google":
		String encoding = "UTF-8";
		 doc = Jsoup.connect("https://www.google.com/search?q=" + 
			 URLEncoder.encode(restaurant + " " + area + "google maps" , encoding)).get();
		 Element box = doc.select("div#rhs_block").first();
		 rating = box.select("span.Aq14fc").first().text();
		 break;
	 case "TripAdvisor":
		 break;
	}
     } catch(Exception e) {
     
     }
     return rating;
   }

   public static void main(String[] args) {
//String x = "oto sushi redmond";
//	String u = search(x, "Google");		
	String site = args[0];	
	String rest = args[1];
	String loc = args[2];
	String review = Rating(site, rest, loc);
	if(site.equals("Yelp")) {
		if(review.contains(".")){
			System.out.println(review.substring(8,11));
		} else {
			System.out.println(review.substring(8,9));
		}
	} else{
	System.out.println(review);
	}
   }
}
