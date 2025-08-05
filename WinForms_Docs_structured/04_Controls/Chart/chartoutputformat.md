---
title: chartoutputformat.md
original_path: WinForms_Docs/04_Controls/Chart/chartoutputformat.md
created_at: 2025-08-05
---








  









## Chart Output Format {#chart-output-format style="tab-stops: 0pt"}

[] 

Essential Chart is first rendered as an image on the server which is then displayed on the client browser.

 

The **OutputFormat** property in ChartWebControl defines how the Chart image from the server is to be served to the Client at runtime. This property can be set to **DiskFile** or **Handler**.                                

[] 

DiskFile

[] 

[·      ]When the **OutputFormat** property is set to **DiskFile**, the chart generates a temporary disk file whose link is served to the Client. The **ImageUrlPath** controls where the disk files are stored.

[·      ]In DiskFile setting, the chart creates several temporary disk files (images of the generated chart). Setting the AutoTempFileCleanUp property to true will automatically clean up these files based on the AutoCleanupCacheExpiration property setting. The latter property controls the time for which such images are allowed to exist on disk. Note that this time is approximate. Actual cleanup time cannot be accurately controlled.


{border="0"}Note: The ASP.NET user will need to have permissions to use this folder on the server. If the permission is not provided, the chart will not be able to write it to disk.


[] 

{border="0"}

**[]** 

Figure 10: Permissions for the Chart

[] 

Handler

**[]** 

[·      ]When the **OutputFormat** is set to **Handler**, the chart does not generate any disk files. **This can lead to better performance than when using DiskFiles.** The Handler entry will be made in the Web.config file automatically, if you drag the control, on to the designer. Otherwise, if you add the control manually, you must specify the entry in the HttpHandlers section of the Web.Config file as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][httpHandlers][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][add][ ][verb][=][\"[\*]\"[ ][path][=]\"[syncfusion_generate.ashx]\"[ ][type][=]\"[Syncfusion.Web.UI.WebControls.Chart.ChartWebHandler,Syncfusion.Chart.Web, Version=X.X.X.X, culture=]\"[Neutral],[PublicKeyToken][=]\"[3d67ed1f87d44c89]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][httpHandlers][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


 

 

{border="0"} Note: X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.


 

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ChartWebControl Properties        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ImageFormat                       | Specifies the image format in which the chart image should be generated. Is of type System.Drawing.ImageFormat. Default is **Png**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OutputFormat                      | Controls how the chart is served at run time from the server. Possible values:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   | *[]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   | DiskFile (**default**)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   | Handler                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AutoTempFileCleanUp               | After enabling this, temporary disk files are cleaned, when the **Outputformat** is set to **DiskFile**, based on the expiration time specified below. Default is **false**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AutoCleanupCacheExpiration        | This setting specifies the approximate time for which, the above images are allowed to exist on disk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ImageUrlPath                      | This specifies the path, where the chart images are stored, that are automatically generated by the chart when the **OutputFormat** is set to **DiskFileMode**. This directory has to exist and the ASP.NET user account need to be provided access to it for the chart to be able to generate images. The default setting is that the chart stores images in the base virtual directory. For this reason if the OutputFormat is set to DiskFile, user ASP.NET should be given write permission for your application root directory (see above for more info). The format of this path must be relative to the application root (default is \".\\\\\"). |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [//To access a subfolder, \"Images\" in the application]                    |
|                                                                                                                               |
| [ChartWebControl1.ImageURLPath = [\"Images\"];]                    |
|                                                                                                                               |
| []                                                                                        |
|                                                                                                                               |
| [//To access a folder outside the application folder]                       |
|                                                                                                                               |
| [ChartWebControl1.ImageURLPath = [\"syncfusion\\\\web\\\\data\"];] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                               |
|                                                                                                                              |
| [\'To access a subfolder, \"Images\" in the application]                   |
|                                                                                                                              |
| [ChartWebControl1.ImageURLPath = [\"Images\"]]                    |
|                                                                                                                              |
| []                                                                        |
|                                                                                                                              |
| [\'To access a folder outside the application folder]                      |
|                                                                                                                              |
| [ChartWebControl1.ImageURLPath = [\"syncfusion\\\\web\\\\data\"]] |
+------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Running ChartWebApplication with Handler OutputFormat in IIS7

**[]** 

While running ChartWebApplication in IIS7 with default Integrated managed pipeline mode, Handler Output format will work only when HTTP Handlers for ChartWebControl are added under the \<System.WebServer\> whereas, when the Chart is added to the Web application, the HTTP Handlers will be added under \<System.Web\> by default.

 

For the application to work properly with IIS 7, any of the following methods can be used.

[] 

1.   Migrate the application to work with the Integrated .NET mode.

[] 

Cmd prompt\>%systemroot%\\system32\\inetsrv\\APPCMD.EXE migrate config \"Default Web Site/\<SampleWebSiteName\>\"

[] 

2.   Change the ApplicationPool of the website to Classic.NetApplicationPool using the following command.

[] 

%systemroot%\\system32\\inetsrv\\APPCMD.EXE set app \"Default Web Site/\<SampleWebSiteName\>\" \" /applicationPool:\"Classic .NET AppPool\".

 

Refer to the following link for more information on ASP.NET Integration With IIS 7.0.

[ ]{.UGHyperlink}[[http://learn.iis.net/page.aspx/243/aspnet-integration-with-iis7.]{.UGHyperlink}](http://learn.iis.net/page.aspx/243/aspnet-integration-with-iis7.)[]{.UGHyperlink}

[]{#p14} 

[]{#related-topics}

