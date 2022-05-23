package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;

import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;



public class Main3 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main3.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			TextField tf1 = (TextField) scene.lookup("#tf01");
			TextField tf2 = (TextField) scene.lookup("#tf02");
			TextField tf3 = (TextField) scene.lookup("#tf03");
			Button btn = (Button)scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String a = tf1.getText();
					String b = tf2.getText();
					int result = Integer.parseInt(a) + Integer.parseInt(b);
					
					tf3.setText(result + "");
					
					
				}
			});
			
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
