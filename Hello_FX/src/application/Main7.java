package application;
	

import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main7 extends Application {
	private Scene scene;
	private TextField tfMine, tfCom, tfResult;
	private Button btn;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main7.fxml"));
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
		String[] game = {"가위", "바위", "보"};
		tfCom.setText(game[new Random().nextInt(2)]);
		String mine = tfMine.getText();
		String com = tfCom.getText();
		String result = "";
		
		if(mine.equals(com)) {
			result = "비김";
		}else if(mine.equals("가위") && com.equals("바위")
				|| mine.equals("바위") && com.equals("보")
				|| mine.equals("보") && com.equals("가위")) {
			result = "컴퓨터 승리";
		}else {
			result = "내가 이김!";
		}
		
		tfResult.setText(result);
		
		
	}
	
	
	
	public void getId() {
		tfMine = (TextField) scene.lookup("#tfMine");
		tfCom = (TextField) scene.lookup("#tfCom");
		tfResult = (TextField) scene.lookup("#tfResult");
		btn = (Button)scene.lookup("#btn");
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
