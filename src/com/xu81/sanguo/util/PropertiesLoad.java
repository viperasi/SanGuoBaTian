/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.xu81.sanguo.util;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Administrator
 */
public class PropertiesLoad {
    static Properties props = null;

    static{
        props = new Properties();
        try {
            props.load(new FileInputStream(PropertiesLoad.class.getResource("/").getPath()+"res/config/application.properties"));
        } catch (IOException ex) {
//            new MessageUtil("程序文件不完整，请重新下载。","错误",MessageUtil.ERROR).show();
            Logger.getLogger(PropertiesLoad.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public static String getProp(String key){
        return props.getProperty(key);
    }
}
