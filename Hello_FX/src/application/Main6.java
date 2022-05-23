package application;
	

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main6 extends Application {
	private Scene scene;
	private TextField tf;
	private TextArea ta;
	private Button btn;
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main6.fxml"));
			scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			getId();
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					
					myClick();
				
				}
			});
			
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void myClick() {
		String val = tf.getText();
		int dan = Integer.parseInt(val);
		String text = ""; 
		
		for(int i = 1; i < 10; i++) {
			text += dan + " X " + i + " = " + (dan * i) + "\n";
		}
		
		ta.setText(text);
	}
	
	
	
	public void getId() {
		tf = (TextField) scene.lookup("#tf");
		ta = (TextArea) scene.lookup("#ta");
		btn = (Button)scene.lookup("#btn");
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
