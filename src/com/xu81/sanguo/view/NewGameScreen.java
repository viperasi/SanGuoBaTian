/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.xu81.sanguo.view;

import java.awt.Color;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import javax.swing.ImageIcon;
import org.loon.framework.javase.game.action.sprite.Label;
import org.loon.framework.javase.game.core.graphics.GameFont;
import org.loon.framework.javase.game.core.graphics.Screen;
import org.loon.framework.javase.game.core.graphics.device.LGraphics;
import org.loon.framework.javase.game.core.graphics.window.LButton;
import org.loon.framework.javase.game.core.graphics.window.LSelect;
import org.loon.framework.javase.game.core.graphics.window.LText;

/**
 *
 * @author Administrator
 */
public class NewGameScreen extends Screen {

    public NewGameScreen() {
        Label lblFirstName = new Label("姓:", 50, 50);
        lblFirstName.setColor(Color.WHITE);
        lblFirstName.setFont("黑体", Font.BOLD, 20);
        add(lblFirstName);

        Label lblMiddleName = new Label("名:", 50, (int) (lblFirstName.getY() + lblFirstName.getHeight() + 30));
        lblMiddleName.setColor(Color.WHITE);
        lblMiddleName.setFont("黑体", Font.BOLD, 20);
        add(lblMiddleName);

        Label lblLastName = new Label("字:", 50, (int) (lblMiddleName.getY() + lblMiddleName.getHeight() + 30));
        lblLastName.setColor(Color.WHITE);
        lblLastName.setFont("黑体", Font.BOLD, 20);
        add(lblLastName);

        LText txtFirstName = new LText("", (int) (lblFirstName.getX() + 35), 35, 100, 20);
        add(txtFirstName);

        LText txtMiddleName = new LText("", (int) (lblMiddleName.getX() + 35), 65, 100, 20);
        add(txtMiddleName);

        LText txtLastName = new LText("", (int) (lblLastName.getX() + 35), 95, 100, 20);
        add(txtLastName);

        Label lblSex = new Label("性别:",50,(int)(lblLastName.getY()+lblLastName.getHeight()+30));
        lblSex.setColor(Color.WHITE);
        lblSex.setFont("黑体",Font.BOLD,20);
        add(lblSex);

        final Label lblSexChoosen = new Label("",(int)(lblSex.getX()+50),140);
        lblSexChoosen.setColor(Color.WHITE);
        lblSexChoosen.setFont("黑体",Font.BOLD,20);
        add(lblSexChoosen);

        LButton sexFemale = new LButton("res/images/female.png",null,30,30,0,0){
            public void doClick(){
                lblSexChoosen.setLabel("女");
            }
        };
        sexFemale.setLocation((int)(lblSexChoosen.getX()+40), 120);
        add(sexFemale);

        LButton sexMale = new LButton("res/images/male.png",null,30,30,0,0){
            public void doClick(){
                lblSexChoosen.setLabel("男");
            }
        };
        sexMale.setLocation(sexFemale.getX()+40, sexFemale.getY());
        add(sexMale);

    }

    public void draw(LGraphics lg) {
    }

    public void onKey(KeyEvent ke) {
    }

    public void onKeyUp(KeyEvent ke) {
    }

    public void leftClick(MouseEvent me) {
    }

    public void middleClick(MouseEvent me) {
    }

    public void rightClick(MouseEvent me) {
    }
}
