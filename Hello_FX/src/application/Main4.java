package application;
	
import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main4 extends Application {
	private Scene scene;
	private TextField tf1, tf2, tf3;
	private Button btn;
	private String result = "";
	private String mine = "";
	private String computer = "";
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main4.fxml"));
			scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			getId();
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					
					tf3.setText(game());
					
				}
			});
			
			tf1.setOnKeyPressed(new EventHandler<KeyEvent>() {

				@Override
				public void handle(KeyEvent k) {
					
					 if (k.getCode().equals(KeyCode.ENTER)) {
						 tf3.setText(game());
			         }
					
				}
				
			});
						
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public String game() {
		String[] game = {"È¦","Â¦"};
		tf2.setText(game[new Random().nextInt(2)]);
		mine = tf1.getText();
		computer = tf2.getText();
		
		if(mine.equals(computer)) {
			result = "³»°¡ÀÌ±è";
		}else {						
			result = "ÄÄÇ»ÅÍ°¡ ÀÌ±è";						
		}
		
		return result;
	}
	
	public void getId() {
		
		tf1 = (TextField) scene.lookup("#tfMine");
		tf2 = (TextField) scene.lookup("#tfCom");
		tf3 = (TextField) scene.lookup("#tfResult");
		btn = (Button)scene.lookup("#btn");
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
