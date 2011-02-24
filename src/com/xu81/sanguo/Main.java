/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.xu81.sanguo;

import com.xu81.sanguo.view.TitleScreen;
import org.loon.framework.javase.game.GameScene;
import org.loon.framework.javase.game.core.graphics.Deploy;

/**
 *
 * @author xu
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        GameScene frame = new GameScene("三国霸天传", 800, 600);
        Deploy deploy = frame.getDeploy();
        deploy.setScreen(new TitleScreen());
        frame.setIconImage("res/images/icon.png");
        deploy.setShowFPS(true);
        deploy.setLogo(false);
        deploy.setFPS(100);
        deploy.mainLoop();
        frame.showFrame();
    }
}
