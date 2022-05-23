package application;
	
import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main10 extends Application {
	
	private Scene scene;
	private Label lbl;
	private Button btn;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main10.fxml"));
			scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			lbl = (Label) scene.lookup("#lbl");
			btn = (Button) scene.lookup("#btn");
			
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
		String time = lbl.getText();
		
		
		new Thread(new Runnable() {
			
			int a = Integer.parseInt(time);
			
			@Override
			public void run() {
				while(a < 10) {	
//					Platform.runLater(()-> lbl.setText(++a + ""));	
					
					Platform.runLater(new Runnable() {
						@Override
						public void run() {
							lbl.setText(a++ + "");
						}
					});	
						try {
							Thread.sleep(1000);
						} catch (Exception e) {}
				}				
			}
			
		}).start();
				
	
	}

	
	public static void main(String[] args) {
		launch(args);
	}
}
