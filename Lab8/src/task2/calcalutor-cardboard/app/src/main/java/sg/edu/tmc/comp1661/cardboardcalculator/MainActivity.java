package sg.edu.tmc.comp1661.cardboardcalculator;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText editTextLength = (EditText) findViewById(R.id.editTextLength);
        final EditText editTextBreadth = (EditText) findViewById(R.id.editTextBreadth);
        final EditText editTextPrice = (EditText) findViewById(R.id.editTextPrice);
        Button button = (Button) findViewById(R.id.button);
        final TextView textViewDisplay = (TextView) findViewById(R.id.textViewDisplay);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                double length = Double.parseDouble(editTextLength.getText().toString());
                double breadth = Double.parseDouble(editTextBreadth.getText().toString());
                double price = Double.parseDouble(editTextPrice.getText().toString());
                double area = length * breadth;
                double cost = area * price;
                String display = "Area: " + area + "\nCost: " + cost;
                textViewDisplay.setText(display);
            }
        });
    }


}
