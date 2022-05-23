package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main9 extends Application {
	
	private Scene scene;
	private TextField tf;
	private Button btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn0;
	private Button callBtn;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main9.fxml"));
			scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();

			btn1 = (Button) scene.lookup("#btn1");
			btn2 = (Button) scene.lookup("#btn2");
			btn3 = (Button) scene.lookup("#btn3");
			btn4 = (Button) scene.lookup("#btn4");
			btn5 = (Button) scene.lookup("#btn5");
			btn6 = (Button) scene.lookup("#btn6");
			btn7 = (Button) scene.lookup("#btn7");
			btn8 = (Button) scene.lookup("#btn8");
			btn9 = (Button) scene.lookup("#btn9");
			btn0 = (Button) scene.lookup("#btn0");
			callBtn = (Button) scene.lookup("#callBtn");
			tf = (TextField) scene.lookup("#tf");
			
			btn1.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btn2.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			btn3.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			btn4.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			btn5.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			btn6.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			btn7.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			btn8.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			btn9.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			btn0.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			callBtn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myCall();
					
				}
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void myCall(){
		String str_tel = tf.getText();
		Alert alert = new Alert(AlertType.INFORMATION, "Calling\n" + str_tel);
		alert.showAndWait();
	}
	
	public void myClick(Event event) {
		Button tmp = (Button) event.getSource();
		String str_new = tmp.getText();
		String str_old = tf.getText();
		tf.setText(str_old + str_new);
	}
	

	
	public static void main(String[] args) {
		launch(args);
	}
}
