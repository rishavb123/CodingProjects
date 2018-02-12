package com.example.bhagat.mycalculator;

import java.util.ArrayList;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private ArrayList<Button> numButtons;
    private String fullEquation;
    private Button enter;
    private ArrayList<Button> operButtons;
    private TextView output;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        numButtons = new ArrayList<>();
        operButtons = new ArrayList<>();
        enter = (Button) findViewById(R.id.enter);
        output = (TextView) findViewById(R.id.output);
        fullEquation = "";

        numButtons.add((Button) findViewById(R.id.b0));
        numButtons.add((Button) findViewById(R.id.b1));
        numButtons.add((Button) findViewById(R.id.b2));
        numButtons.add((Button) findViewById(R.id.b3));
        numButtons.add((Button) findViewById(R.id.b4));
        numButtons.add((Button) findViewById(R.id.b5));
        numButtons.add((Button) findViewById(R.id.b6));
        numButtons.add((Button) findViewById(R.id.b7));
        numButtons.add((Button) findViewById(R.id.b8));
        numButtons.add((Button) findViewById(R.id.b9));

        operButtons.add((Button) findViewById(R.id.plus));
        operButtons.add((Button) findViewById(R.id.minus));
        operButtons.add((Button) findViewById(R.id.times));
        operButtons.add((Button) findViewById(R.id.divide));


        for (int x = 0; x < numButtons.size(); x++) {
            Button temp = numButtons.get(x);
            final String insideText = temp.getText().toString();
            temp.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    fullEquation += insideText;
                    output.setText(fullEquation.replace("!",""));
                }
            });

            numButtons.set(x, temp);
        }

        for (int x = 0; x < operButtons.size(); x++) {
            Button temp = operButtons.get(x);
            final String insideText = temp.getText().toString();
            temp.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (fullEquation.equals(""))
                        fullEquation += "0";
                    if(fullEquation.charAt(fullEquation.length()-1)=='+'||fullEquation.charAt(fullEquation.length()-1)=='-'||fullEquation.charAt(fullEquation.length()-1)=='x'||fullEquation.charAt(fullEquation.length()-1)=='÷')
                        fullEquation = fullEquation.substring(0,fullEquation.length())+"!"+insideText;
                    else
                        fullEquation += "!" + insideText;
                    output.setText(fullEquation.replace("!",""));
                    output.setText(Double.toString(doOperation(fullEquation.substring(0,fullEquation.length()-1))));
                }
            });

            operButtons.set(x, temp);
        }

        enter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                output.setText(Double.toString(doOperation(fullEquation)));
                fullEquation = "";
            }
        });

    }

    public double doOperation(String equation)
    {
        try {
            int i = Integer.parseInt(equation.substring(0,1));
            equation = "+" + equation;
        }
        catch(Exception e) {}
        String[] items = equation.split("!");

        double answer = 0.0;
        try {
            if(equation.indexOf("666")!=-1)
                throw new Exception("This is a sat on error");
            for (int x = 0; x < items.length; x++) {
                switch (items[x].charAt(0)) {
                    case '+':
                        answer += Double.parseDouble(items[x].substring(1));
                        break;
                    case '-':
                        answer -= Double.parseDouble(items[x].substring(1));
                        break;
                    case 'x':
                        answer *= Double.parseDouble(items[x].substring(1));
                        break;
                    case '÷':
                        answer /= Double.parseDouble(items[x].substring(1));
                        break;
                    default:
                        return 0.0;
                }
            }

        }
        catch(Exception e)
        {
            return 0.0;
        }

        return answer;
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
//        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
//        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
//        if (id == R.id.action_settings) {
//            return true;
//        }

        return super.onOptionsItemSelected(item);
    }
}
