
#生成xml文件
cat > da.xml << END_TEXT
<?xml version = "1.0" encoding = "GBK"?>
<project basedir="." default="sourcecheckout" name="checkout_mavn">
    <property file="/home/deployuser/.jenkins/st_ant_maven.conf"/>
    <property name="stproject" value="EC" />
    <property name="stview" value="EC" />
     <target name="sourcecheckout">
    <stcheckout servername="\${stserver}"
    serverport="\${stport}"
    projectname="EC"
    viewname="EC"
    username="\${stuser}"
    password="\${stpassword}"
    label="$labal"
    rootstarteamfolder="04-src/ec/ecappFront"
    rootlocalfolder="./source"
    forced="true"
    recursive="true"
    deleteuncontrolled="false" />
    </target>
</project>
END_TEXT
