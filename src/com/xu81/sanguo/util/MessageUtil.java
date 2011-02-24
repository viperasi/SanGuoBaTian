/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.xu81.sanguo.util;

import java.awt.Toolkit;
import javax.swing.JOptionPane;

/**
 *
 * @author Administrator
 */
public class MessageUtil{
    private String msg;
    private String title;
    private int type;

    public static final int ERROR = -1;
    public static final int INFO = 0;
    
    public MessageUtil(){
        this("","",0);
    }

    public MessageUtil(String msg,String title,int type){
        this.msg = msg;
        this.title = title;
        this.type = type;
    }

    public void show(){
        JOptionPane.showInternalMessageDialog(null, this.msg, this.title, type);
    }
}
