---
title: addingstylemanagertoanapplication.md
original_path: WinForms_Docs/02_Concepts/addingstylemanagertoanapplication.md
created_at: 2025-08-05
---






#### Adding StyleManager to an Application {#adding-stylemanager-to-an-application style="tab-stops: 0pt"}

[] 

Add the **StyleManager extension** method in the HEAD tag of the View pages (in most cases, It is reasonable to call it within the Site.Master page).[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [\<][head][ [runat][=\"server\"\>]][]     |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().StyleManager()[%\>]][] |
|                                                                                                                                                                                                                                                                            |
| [...][]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [...\                                                                                                                                                                                                                                                                      |
| [\</][head][\>]][]                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Use **Register()** method to register the Syncfusion components CSS resources.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().StyleManager()[%\>]][] |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The above code registers the default Office2007Blue theme for added components. All the CSS resources are combined and minified before sending to the browser.

 

Customization

Various customization options have been provided. They are:

[·      ]Minify

[·      ]Combine

[·      ]Register

[·      ]Add CSS Files

 

Minify[]

To enable or disable Minify feature, use **Minify()** method. Minify is Enabled by default.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                       |
|                                                                                                                                                                                                                                                                                 |
| [         **.Minify([false])**][ ][// Enable/disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                 |
| [%\>][]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Refer to HTTP Requests and the time details from the following images.[]

[] 

Before:[]

[] 

{border="0"}

Figure 3: Minify Disabled[]

[] 

After:[]

{border="0"}

Figure 4: Minify Enabled[]

 

The above images show the size of the resource files before and after the Minfication process. Before the Minification process 19KB file is downloaded in browser (Figure 1), whereas after minification, 14.5KB files are downloaded in browser (Figure 2). 4.5KB size is reduced in the above minification process sample.[]

[] 

Combine []

[] 

 To enable or disable Combine file feature, use **Combine()** method. Combine is enabled by default.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                     |
|                                                                                                                                                                                                                                                                               |
| [         .Minify([false])][ ][// Enable ordisable Minify feature.][] |
|                                                                                                                                                                                                                                                                               |
| **[          .Combine([false])]**[// Enable or disable Combine feature.][]                                         |
|                                                                                                                                                                                                                                                                               |
| [%\>][]                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Refer to HTTP Requests and the time details from the following images:[]

[] 

Before:

[] 

{border="0"}

Figure 5: Combine Disabled[]

[] 

After:[]

[] 

{border="0"}

Figure 6: Combine Enabled[]

 

The above images show the downloading time before and after the Combine process of the resource files. Before the Combine process, the browser takes 257ms  to download the css resources (Figure 1), whereas after Combine, it takes only 63ms to the download resources(Figure 2). 194ms time is reduced in the above Combine process sample.[]

[] 

Register[]

 

Two overloads are available for **Register**() method. Adding StyleManager to an application uses the one where the component name can be specified as a String separated by a comma.[]

To add controls in a single line, use **Register()** method.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [\<%][=][Html.Syncfusion().StyleManager()\                                                                                                         |
|                **.Register([\"Grid,Menu,Toolbar,Accordion\"])**[//Specify the component names   separated by a comma.]][] |
|                                                                                                                                                                                                                                                             |
| [               [%\>]][]                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To avoid child control register, use **DisableChildRegister()** method.[]

**For example:** Grid with paging and sorting feature does not require sub controls namely Menu and Dialog (these sub controls are used in filtering feature). In order to avoid these child registers, use ***DisableChildRegister*()** as  follows:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                      |
|                                                                                                                                                                                                                                                                                |
| [         .Minify([false])][ ][// Enable or disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                |
| [         .Combine([false])[// Enable or disable Combine feature.]][]                                                                           |
|                                                                                                                                                                                                                                                                                |
| [%\>][]                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To enable or disable the sub component registrations based on some condition, use **AllowChildRegister()**  method.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                      |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                         |
| [         .Minify([false])[ // Enable or disable Minify feature.]]                                       |
|                                                                                                                                                                                         |
| [         .Combine([false])[// Enable or disable Combine feature.]]                                      |
|                                                                                                                                                                                         |
| [%\>][]                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Add CSS Files[]

[] 

To include the application CSS files to styleManager, use **Add()** method.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                      |
|                                                                                                                                                                                         |
| []                                                                                                                                      |
|                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                         |
| [        .Register(styleSheet =\> \                                                                                                                                                     |
|             {\                                                                                                                                                                          |
|                 **styleSheet.Add([\"\~/Content/Site.css\"]);\**                                                                                                 |
|             })  [%\>]][]                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

