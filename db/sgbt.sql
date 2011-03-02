DROP TABLE IF EXISTS `tbl_cities`;
CREATE TABLE `tbl_cities` (
`city_id` INTEGER PRIMARY KEY  AUTO_INCREMENT   NOT NULL , 
`city_name` VARCHAR DEFAULT ``, 
`city_cityname` VARCHAR DEFAULT ``, 
`city_x` INTEGER DEFAULT 0, 
`city_y` INTEGER DEFAULT 0, 
`city_ownner` INTEGER DEFAULT 0, 
`city_legion` INTEGER DEFAULT 0, 
`city_cownner` INTEGER DEFAULT 0, 
`city_clegion` INTEGER DEFAULT 0, 
`released` INTEGER DEFAULT 1, 
`city_issp` INTEGER DEFAULT 0
);
DROP TABLE IF EXISTS `tbl_disps`;
CREATE TABLE `tbl_disps` (`disp_id` INTEGER PRIMARY KEY  NOT NULL ,`disp_name` VARCHAR DEFAULT (``) ,`released` INTEGER DEFAULT (1) ,`disp_iscmd` INTEGER DEFAULT (0) ,`disp_isdual` INTEGER DEFAULT (0) ,`disp_ispol` INTEGER DEFAULT (0) ,`disp_ispop` INTEGER DEFAULT (0) , `disp_cmd_adjust` INTEGER DEFAULT 0, `disp_dual_adjust` INTEGER DEFAULT 0, `disp_pol_adjust` INTEGER DEFAULT 0, `disp_pop_adjust` INTEGER DEFAULT 0);
DROP TABLE IF EXISTS `tbl_hero_disps_mid`;
CREATE TABLE `tbl_hero_disps_mid` (`mid_id` INTEGER PRIMARY KEY  AUTO_INCREMENT   NOT NULL , `mid_heroid` INTEGER, `mid_dispid` INTEGER, `released` INTEGER DEFAULT 1);
DROP TABLE IF EXISTS `tbl_hero_ops_mid`;
CREATE TABLE `tbl_hero_ops_mid` (`mid_id` INTEGER PRIMARY KEY  AUTO_INCREMENT   NOT NULL , `mid_heroid` INTEGER, `mid_opid` INTEGER, `released` INTEGER DEFAULT 1);
DROP TABLE IF EXISTS `tbl_hero_res_mid`;
CREATE TABLE `tbl_hero_res_mid` (`mid_id` INTEGER PRIMARY KEY  AUTO_INCREMENT   NOT NULL , `mid_heroid` INTEGER, `mid_resid` INTEGER, `mid_maxvalue` INTEGER DEFAULT 0, `released` INTEGER DEFAULT 1);
DROP TABLE IF EXISTS `tbl_hero_skills_mid`;
CREATE TABLE `tbl_hero_skills_mid` (`mid_id` INTEGER PRIMARY KEY  NOT NULL ,`mid_heroid` INTEGER,`mid_skillid` INTEGER,`mid_maxlv` INTEGER DEFAULT (0) ,`mid_adjust` INTEGER DEFAULT (0) ,`released` INTEGER DEFAULT (1) , `mid_currlv` INTEGER DEFAULT 0);
DROP TABLE IF EXISTS `tbl_heros`;
CREATE TABLE `tbl_heros` (`hero_id` INTEGER PRIMARY KEY  AUTO_INCREMENT   NOT NULL  UNIQUE , `hero_name` VARCHAR DEFAULT ``, `hero_sex` VARCHAR DEFAULT ``, `hero_birth` INTEGER DEFAULT 0, `hero_death` INTEGER DEFAULT 0, `hero_power` INTEGER DEFAULT 0, `hero_intellect` INTEGER DEFAULT 0, `hero_pop` INTEGER DEFAULT 0, `released` INTEGER DEFAULT 1, `hero_command` INTEGER DEFAULT 0);
DROP TABLE IF EXISTS `tbl_ops`;
CREATE TABLE `tbl_ops` (`op_id` INTEGER PRIMARY KEY  AUTO_INCREMENT   NOT NULL , `op_name` VARCHAR DEFAULT ``, `op_opname` VARCHAR DEFAULT ``, `op_iscmd` INTEGER DEFAULT 0, `op_isdual` INTEGER DEFAULT 0, `op_ispol` INTEGER DEFAULT 0, `op_ispop` INTEGER DEFAULT 0, `op_req` INTEGER DEFAULT 0, `op_isonlysex` INTEGER DEFAULT 0, `op_isonlyhero` INTEGER DEFAULT 0, `released` INTEGER DEFAULT 1);
DROP TABLE IF EXISTS `tbl_resources`;
CREATE TABLE `tbl_resources` (`res_id` INTEGER PRIMARY KEY  AUTO_INCREMENT   NOT NULL , `res_name` VARCHAR DEFAULT ``, `res_iscmd` INTEGER DEFAULT 0, `res_isdual` INTEGER DEFAULT 0, `res_ispol` INTEGER DEFAULT 0, `res_ispop` INTEGER DEFAULT 0, `res_isonlysex` INTEGER DEFAULT 0, `res_isonlyhero` INTEGER DEFAULT 0, `released` INTEGER DEFAULT 1, `res_resname` VARCHAR DEFAULT ``);
DROP TABLE IF EXISTS `tbl_skills`;
CREATE TABLE `tbl_skills` (`skill_id` INTEGER PRIMARY KEY  NOT NULL ,`skill_name` VARCHAR DEFAULT (``) ,`skill_ico` VARCHAR DEFAULT (``) ,`skill_iscmd` INTEGER DEFAULT (0) ,`skill_isdual` INTEGER DEFAULT (0) ,`skill_ispol` INTEGER DEFAULT (0) ,`skill_ispop` INTEGER DEFAULT (0) ,`skill_cmd_force` INTEGER DEFAULT (0) ,`skill_cmd_inc` INTEGER DEFAULT (0) ,`skill_dual_force` INTEGER DEFAULT (0) ,`skill_dual_inc` INTEGER DEFAULT (0) ,`skill_pol_force` INTEGER DEFAULT (0) ,`skill_pol_inc` INTEGER DEFAULT (0) ,`skill_pop_force` INTEGER DEFAULT (0) ,`skill_pop_inc` INTEGER DEFAULT (0) ,`skill_isonlysex` INTEGER DEFAULT (0) ,`released` INTEGER DEFAULT (1) ,`skill_xpinc` INTEGER DEFAULT (100) );
