package application;
	
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;



public class Main5 extends Application {
	private Scene scene;
	private Label lbl1, lbl2, lbl3, lbl4, lbl5, lbl6;
	private Button btn;
	private List<Integer> lotto;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main5.fxml"));
			scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			getId();
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					
					lotto = makeNum();
					
					lbl1.setText(lotto.get(0) + "");
					lbl2.setText(lotto.get(1) + "");
					lbl3.setText(lotto.get(2) + "");
					lbl4.setText(lotto.get(3) + "");
					lbl5.setText(lotto.get(4) + "");
					lbl6.setText(lotto.get(5) + "");
				}
			});
			
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public List<Integer> makeNum(){
		Set<Integer> num = new HashSet<>();
		List<Integer> list = null;
		
		while(num.size() < 6) {
			num.add(new Random().nextInt(45)+1);
		}
		
		list = new ArrayList<>(num);
		Collections.sort(list);
		
		return list;
	}
	
	public void getId() {
		lbl1 = (Label) scene.lookup("#lbl1");
		lbl2 = (Label) scene.lookup("#lbl2");
		lbl3 = (Label) scene.lookup("#lbl3");
		lbl4 = (Label) scene.lookup("#lbl4");
		lbl5 = (Label) scene.lookup("#lbl5");
		lbl6 = (Label) scene.lookup("#lbl6");
		btn = (Button)scene.lookup("#btn");
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
