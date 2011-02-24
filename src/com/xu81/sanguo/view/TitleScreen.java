/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.xu81.sanguo.view;

import com.xu81.sanguo.util.PropertiesLoad;
import java.awt.Color;
import java.awt.event.KeyEvent;
import java.awt.event.MouseEvent;
import org.loon.framework.javase.game.action.sprite.Label;
import org.loon.framework.javase.game.core.graphics.Screen;
import org.loon.framework.javase.game.core.graphics.device.LGraphics;
import org.loon.framework.javase.game.core.graphics.window.LButton;

/**
 *
 * @author xu
 */
public class TitleScreen extends Screen {

    LButton startMenu, continueMenu, aboutMenu, exitMenu;

    public TitleScreen() {
        // 变更背景
        setBackground("res/images/title.png");

        startMenu = new LButton("res/images/menu_newstart.png", null, 122, 36, 0, 0) {

            public void doClick() {
                System.out.println("it's start!");
                setScreen(new NewGameScreen());
            }
        };
        startMenu.setLocation(338, 367);
        add(startMenu);

        continueMenu = new LButton("res/images/menu_continue.png", null, 122, 36, 0, 0) {

            public void doClick() {
                System.out.println("it's continue");
            }
        };
        continueMenu.setLocation(338, startMenu.getY() + startMenu.getHeight() + 15);
        add(continueMenu);

        aboutMenu = new LButton("res/images/menu_about.png", null, 122, 36, 0, 0) {

            public void doClick() {
                System.out.println("it's about");
            }
        };
        aboutMenu.setLocation(338, continueMenu.getY() + continueMenu.getHeight() + 15);
        add(aboutMenu);

        exitMenu = new LButton("res/images/menu_exit.png", null, 122, 36, 0, 0) {

            public void doClick() {
                System.exit(0);
            }
        };
        exitMenu.setLocation(338, aboutMenu.getY() + aboutMenu.getHeight() + 15);
        add(exitMenu);

        Label version = new Label(PropertiesLoad.getProp("version"), getWidth()-30, getHeight()-10);
        version.setColor(Color.WHITE);
        add(version);
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
