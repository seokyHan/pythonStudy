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



public class Main8 extends Application {
	private Scene scene;
	private TextField tFirst, tEnd;
	private TextArea ta;
	private Button btn;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main8.fxml"));
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
		
		String f = tFirst.getText();
		String e = tEnd.getText();
		String output = "";
		
		int first = Integer.parseInt(f);
		int end = Integer.parseInt(e);
		
		for(int i=first; i<=end; i++) {
			output += drawStar(i);
		}
		
		ta.setText(output);
		
	}
	
	public String drawStar(int cnt) {
		String ret = "";
		for(int i = 0; i < cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		
		return ret;
	}
	
	
	public void getId() {
		tFirst = (TextField) scene.lookup("#tFirst");
		tEnd = (TextField) scene.lookup("#tEnd");
		ta = (TextArea) scene.lookup("#ta");
		btn = (Button)scene.lookup("#btn");
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
