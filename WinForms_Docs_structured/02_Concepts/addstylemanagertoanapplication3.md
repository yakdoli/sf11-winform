---
title: addstylemanagertoanapplication3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\addstylemanagertoanapplication3.md
created_at: 2025-07-03
---






#### Add StyleManager to an Application {#add-stylemanager-to-an-application style="tab-stops: 0pt"}

 

Add the **StyleManager extension** method in the HEAD tag of the View pages (in most cases, It is reasonable to call it within the Site.Master page).[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[aspx**]**[\]][]**                                                              |
|                                                                                                                                                                                                                                                                            |
| [\<][head][ [runat][=\"server\"\>]][ ]    |
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

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]**[]**                                                                                                                              |
|                                                                                                                                                                                                                                                                           |
| [\<][head][ [runat][=\"server\"\>]]                                                      |
|                                                                                                                                                                                                                                                                           |
| [   [\@{]Html.Syncfusion().StyleManager()]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [        .Register(stylesheets =\>]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [            {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [             ][stylesheets][.Add([ComponentType].][Menu][);] |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            }).Render();[}]]**[]**                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [\                                                                                                                                                                                                                                                                        |
| [\</][head][\>]][]                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Use **Register()** method to register the Syncfusion components CSS resources.[]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ ][View\[aspx][\]][]** |
|                                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().StyleManager()\                                                                                                                          |
|         .Register(styleSheet =\> \                                                                                                                                                                                                                                           |
|             {\                                                                                                                                                                                                                                                               |
|                 styleSheet.Add([ComponentType].Grid);\                                                                                                                                                                                               |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                                                                                                                                          |
|                 styleSheet.Add([ComponentType].Menu);\                                                                                                                                                                                               |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                                                                                                                                            |
|             })  [%\>]][]                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]**[]**        |
|                                                                                                                                                     |
| [\@{][ ][Html.Syncfusion().StyleManager()\ |
|         .Register(styleSheet =\> \                                                                                                                  |
|             {                \                                                                                                                      |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                 |
|                 styleSheet.Add([ComponentType].Menu);\                                                                      |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                   |
|             }).Render();  [}]][]    |
|                                                                                                                                                     |
| []                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

The above code registers the default Office2007Blue theme for added components. All the CSS resources are combined and minified before sending to browser.[]

 

Customization

Various customization options have been provided. They are:

[·      ]Minify

[·      ]Combine

[·      ]Register

[·      ]Theme

[·      ]Add CSS Files

 

Minify

To enable or disable Minify feature, use **Minify()** method. Minify is Enabled by default.[ ]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX]**[ **View\[aspx**]**[\]][]**                   |
|                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                       |
|                                                                                                                                                                                                                                                                                 |
| [         **.Minify([false])**][ ][// Enable/disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                 |
| [        .Register(styleSheet =\> \                                                                                                                                                                                                                                             |
|             {\                                                                                                                                                                                                                                                                  |
|                 styleSheet.Add([ComponentType].Grid);\                                                                                                                                                                                                  |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                                                                                                                                             |
|                 styleSheet.Add([ComponentType].Menu);\                                                                                                                                                                                                  |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                                                                                                                                               |
|             })  [%\>]][]                                                                                                                       |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]**[]**                                                                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [\@{][ ][Html.Syncfusion().StyleManager()][]                                      |
|                                                                                                                                                                                                                                                                                |
| [        **.Minify([false])**][ ][// Enable/disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                |
| [        .Register(styleSheet =\> \                                                                                                                                                                                                                                            |
|             {\                                                                                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Menu);\                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                                                                                                                                              |
|             }).Render();  [}]][]                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

Please refer HTTP Requests and the time details from the below images.[]

Before:[]

[] 

{border="0"}[]

Figure 3: Minify Disabled.

[] 

After:[]

{border="0"}[]

Figure 4: Minify Enabled.

The above images show the size of the resource files before and after the Minfication process. Before the Minification process 19KB file is downloaded in browser (Figure 1), whereas after minification, 14.5KB files downloaded in browser(Figure 2). 4.5KB size reduced in the above minification process sample.[]

 

Combine

 To enable or disable Combine file feature, use **Combine()** method. Combine is Enabled by default.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                     |
|                                                                                                                                                                                                                                                                               |
| [         .Minify([false])][ ][// Enable ordisable Minify feature.][] |
|                                                                                                                                                                                                                                                                               |
| **[          .Combine([false])]**[// Enable or disable Combine feature.][]                                         |
|                                                                                                                                                                                                                                                                               |
| [        .Register(styleSheet =\> \                                                                                                                                                                                                                                           |
|             {\                                                                                                                                                                                                                                                                |
|                 styleSheet.Add([ComponentType].Grid);\                                                                                                                                                                                                |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                                                                                                                                           |
|                 styleSheet.Add([ComponentType].Menu);\                                                                                                                                                                                                |
|                 styleSheet.Add([ComponentType].AutoCompleteTextBox);\                                                                                                                                                                                 |
|             })  [%\>]][]                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]**[]**                                                                                                                                  |
|                                                                                                                                                                                                                                                                               |
| [\@{][ ][Html.Syncfusion().StyleManager()][]                                     |
|                                                                                                                                                                                                                                                                               |
| [         .Minify([false])][ ][// Enable ordisable Minify feature.][] |
|                                                                                                                                                                                                                                                                               |
| **[         .Combine([false])]**[// Enable or disable Combine feature.][]                                          |
|                                                                                                                                                                                                                                                                               |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                                                          |
|             {\                                                                                                                                                                                                                                                                |
|                 styleSheet.Add([ComponentType].Grid);\                                                                                                                                                                                                |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                                                                                                                                           |
|                 styleSheet.Add([ComponentType].Menu);\                                                                                                                                                                                                |
|                 styleSheet.Add([ComponentType].AutoCompleteTextBox);\                                                                                                                                                                                 |
|             })  .Render(); ]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [ [}]][ ]                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Please refer HTTP Requests and the time details from the below images:[]

[] 

Before:[]

{border="0"}[]

Figure 5: Combine Disabled

[] 

After:

 

{border="0"}[]

Figure 6: Combine Enabled

 

The above images show the downloading time before and after the Combine process of the resource files. Before the Combine process, browser takes 257ms to download the css resources (Figure 1), where as after Combine it takes only 63ms to the download resources (Figure 2). 194ms time is reduced in the above Combine process sample.[]

 

Register

Two overloads are available for **Register**() method. Adding StyleManager to an application uses the one where the component name can be specified as String separated by a comma.[]

1.   To add controls in a single line, use **Register()** method.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().StyleManager()\                                                                                              |
| **    .Register([\"Grid,Menu,Toolbar,Accordion\"])**[//Specify the component names   separated by a comma.]][] |
|                                                                                                                                                                                                                                                  |
| [               [%\>]][]                                                                                                         |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[][] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| [\@{][ ][Html.Syncfusion().StyleManager()\                                                                                                         |
|                **.Register([\"Grid,Menu,Toolbar,Accordion\"])**[//Specify the component names   separated by a comma.]][] |
|                                                                                                                                                                                                                                                             |
| [.Render();[}]][ ]                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[2.   ]Second overload uses the [ComponentType][ to register the controls.[ ]]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().StyleManager()\                                                                                     |
|                ]**[.Register]**[(stylesheets =\>]                                                                           |
|                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [                stylesheets.Add([ComponentType].]**[Accordion]**[);                              ] |
|                                                                                                                                                                                                                                         |
| [            })]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [     [%\>]][ ][]                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**[ ]                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [ [\@{]Html.Syncfusion().StyleManager()]                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [        **.Register**(stylesheets =\>]                                                                                                                                                              |
|                                                                                                                                                                                                                                          |
| [            {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [                stylesheets.Add([ComponentType].]**[Accordion]**[);                               ] |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [            })]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [.Render();[}]][ ]                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To avoid child control register, use **DisableChildRegister()** method.[]

**For example:** Grid with paging and sorting feature doesn't require sub controls like Menu, Dialog (these sub controls are used in filtering feature). In order to avoid these child registers use ***DisableChildRegister*()** as  follows: []

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX]**[ **View\[aspx**]**[\]][]**                  |
|                                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                      |
|                                                                                                                                                                                                                                                                                |
| [         .Minify([false])][ ][// Enable or disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                |
| [         .Combine([false])[// Enable or disable Combine feature.]][]                                                                           |
|                                                                                                                                                                                                                                                                                |
| [         .Theme([Skins].Almond)[ // Specify theme.]][]                                                                                      |
|                                                                                                                                                                                                                                                                                |
| [ComponentType][.Menu)**.DisableChildRegister()**;\                                                                                                                                                                        |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                                                                                                                                              |
|             }) ][]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [ [%\>]][ ]                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [\@{][ ][Html.Syncfusion().StyleManager()][]                                      |
|                                                                                                                                                                                                                                                                                |
| [         .Minify([false])][ ][// Enable or disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                |
| [         .Combine([false])[// Enable or disable Combine feature.]][]                                                                           |
|                                                                                                                                                                                                                                                                                |
| [         .Theme([Skins].Almond)[ // Specify theme.]][]                                                                                      |
|                                                                                                                                                                                                                                                                                |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                                                           |
|             {\                                                                                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].Menu)**.DisableChildRegister()**;\                                                                                                                                                                      |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                                                                                                                                              |
|             }).Render(); ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [ [}]][  ]                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

To enable or disable the sub component registrations based on some condition, use **AllowChildRegister()** method.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX][View\[aspx][\]]** |
|                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().StyleManager()]            |
|                                                                                                                                                                                                    |
| [         .Minify([false])[ // Enable or disable Minify feature.]]                                                  |
|                                                                                                                                                                                                    |
| [         .Combine([false])[// Enable or disable Combine feature.]]                                                 |
|                                                                                                                                                                                                    |
| [         .Theme([Skins].Almond)[ // Specify Theme. ]]                                                           |
|                                                                                                                                                                                                    |
| [ComponentType][.Menu)**.AllowChildRegister([true]);\**                                                                   |
|               styleSheet.Add([ComponentType].Accordion);\                                                                                                                  |
|               styleSheet.Add([ComponentType].Toolbar);\                                                                                                                    |
|             })  ]                                                                                                                                              |
|                                                                                                                                                                                                    |
| [%\>][ ]                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]                                                                                                  |
|                                                                                                                                                                                         |
| [\@{][ ][Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                         |
| [         .Minify([false])[ // Enable or disable Minify feature.]]                                       |
|                                                                                                                                                                                         |
| [         .Combine([false])[// Enable or disable Combine feature.]]                                      |
|                                                                                                                                                                                         |
| [         .Theme([Skins].Almond)[ // Specify Theme. ]]                                                |
|                                                                                                                                                                                         |
| [         .Register(styleSheet =\> \                                                                                                                                                    |
|             {\                                                                                                                                                                          |
|               styleSheet.Add([ComponentType].Menu)**.AllowChildRegister([true]);\**                                                        |
|               styleSheet.Add([ComponentType].Accordion);\                                                                                                       |
|               styleSheet.Add([ComponentType].Toolbar);\                                                                                                         |
|             }).Render(); ]                                                                                                                          |
|                                                                                                                                                                                         |
| [ [}]][  ]                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Theme

To register the CSS Stylesheets for all controls, use Theme() method. Office2007Blue theme is the default theme.

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX][View\[aspx][\]]**                                                                             |
|                                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                      |
|                                                                                                                                                                                                                                                                                |
| [         .Minify([false])][ ][// Enable or disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                |
| [         .Combine([false])[// Enable or disable Combine feature.]][]                                                                           |
|                                                                                                                                                                                                                                                                                |
| [         **.Theme([Skins].Almond)**[ // Specify Theme. ]][]                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                                                           |
|             {                \                                                                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Menu);\                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                                                                                                                                              |
|             })  [%\>]][]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [\@{][ ][Html.Syncfusion().StyleManager()][]                                      |
|                                                                                                                                                                                                                                                                                |
| [         .Minify([false])][ ][// Enable or disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                |
| [         .Combine([false])[// Enable or disable Combine feature.]][]                                                                           |
|                                                                                                                                                                                                                                                                                |
| [         **.Theme([Skins].Almond)**[ // Specify Theme. ]][]                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                                                           |
|             {                \                                                                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Menu);\                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                                                                                                                                              |
|             }).Render(); ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [ [}]][  ]                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

To configure individual theme for every controls use **Theme()** method inside Register().[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[aspx**]**[\]]**                                                                               |
|                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().StyleManager()][] |
|                                                                                                                                                                                                                                           |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                      |
|             {\                                                                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Accordion)**.Theme([Skins].Blend)**;      \                                                                                                |
|                 styleSheet.Add([ComponentType].Menu);\                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Toolbar][)][;][]   |
|                                                                                                                                                                                                                                           |
| [})  [%\>]][ ]                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [\@{][ ][Html.Syncfusion().StyleManager()][] |
|                                                                                                                                                                                                                                           |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                      |
|             {\                                                                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Accordion)**.Theme([Skins].Blend)**;      \                                                                                                |
|                 styleSheet.Add([ComponentType].Menu);\                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Toolbar);]                                                                                                                     |
|                                                                                                                                                                                                                                           |
| [}).Render(); ]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                           |
| [ [}]][  ]                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In this above code, Office2007Blue theme registers all the other components and Blend theme registers for Grid.[]

To register JQuery themes to JqueryControls, use **JqueryTheme()** method.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX][View\[aspx][\]]** |
|                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().StyleManager()]            |
|                                                                                                                                                                                                    |
| [         .Register(styleSheet =\> \                                                                                                                                                               |
|             {]                                                                                                                                                 |
|                                                                                                                                                                                                    |
| [  styleSheet.Add([ComponentType].Accordion).**JqueryTheme(Syncfusion.Mvc.Tools.[jQuerySkins].Cupertino);**\                                       |
|              })  [%\>]]                                                                                                            |
|                                                                                                                                                                                                    |
| []                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]                                                                                                  |
|                                                                                                                                                                                         |
| [\@{][ ][Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                         |
| [         .Register(styleSheet =\> \                                                                                                                                                    |
|             {]                                                                                                                                      |
|                                                                                                                                                                                         |
| [  styleSheet.Add([ComponentType].Accordion).**JqueryTheme(Syncfusion.Mvc.Tools.[jQuerySkins].Cupertino);**\                            |
|              }).Render(); ]                                                                                                                         |
|                                                                                                                                                                                         |
| [ [}]][  ]                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To avoid theme override by external Theme() method, use **DontOverride()** method. []

[  ]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX][View\[aspx][\]]** |
|                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().StyleManager()\                                                |
|       .Theme([Skins].Almond)[// Specify Theme to all components].   ][]      |
|                                                                                                                                                                                                    |
| [ ][      .Register(styleSheet =\> \                                                                                              |
|           {\                                                                                                                                                                                       |
|         styleSheet.Add([ComponentType].Menu).Theme([Skins].Blend**).DontOverride();**\                                                             |
|         styleSheet.Add([ComponentType].Accordion);       \                                                                                                                 |
|         styleSheet.Add([ComponentType].Toolbar);\                                                                                                                          |
|            })[%\>]][ ]                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]                                                                    |
|                                                                                                                                                           |
| [\@{][ ][Html.Syncfusion().StyleManager()\       |
|       .Theme([Skins].Almond)[// Specify Theme to all components].     ] |
|                                                                                                                                                           |
| [      .Register(styleSheet =\> \                                                                                                                         |
|           {\                                                                                                                                              |
|         styleSheet.Add([ComponentType].Menu).Theme([Skins].Blend**).DontOverride();**\                    |
|         styleSheet.Add([ComponentType].Accordion);       \                                                                        |
|         styleSheet.Add([ComponentType].Toolbar);\                                                                                 |
|            })  .Render(); ]                                                                                           |
|                                                                                                                                                           |
| [ [}]][  ]               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

In general, the external Theme() method overrides all the internal component themes register. The DontOverride() method preserves the theme registered in the Register() methods.


{border="0"}Note: The Theme () method will register the CSS style sheets for the specified theme in the html head section. Using this method, we cannot apply themes for the controls (cannot add CSS classes). If we don't use StyleManager then the CSS style sheet for default theme or specified theme will be registered just before controls render starts. The StyleManager is introduced to improve the performance using its Minify and Combine feature.[]


Add CSS Files

To include the application CSS files to styleManager, use **Add()** method.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX][View\[aspx][\]]** |
|                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().StyleManager()\                                                |
|         .Theme([Skins].Almond)[// Specify Theme to all components.]\                                                                                 |
|         .Register(styleSheet =\> \                                                                                                                                                                 |
|             {\                                                                                                                                                                                     |
|                 styleSheet.Add([ComponentType].Menu).Theme([Skins].Blend).DontOverride();\                                                         |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                                                                |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                                                                  |
|                 **styleSheet.Add([\"\~/Content/Site.css\"]);\**                                                                                                            |
|             })  [%\>]][]                                                           |
|                                                                                                                                                                                                    |
| []                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **View\[cshtml\]**]                                                              |
|                                                                                                                                                     |
| [\@{][ ][Html.Syncfusion().StyleManager()\ |
|         .Theme([Skins].Almond)[// Specify Theme to all components.]\                                  |
|         .Register(styleSheet =\> \                                                                                                                  |
|             {\                                                                                                                                      |
|                 styleSheet.Add([ComponentType].Menu).Theme([Skins].Blend).DontOverride();\          |
|                 styleSheet.Add([ComponentType].Accordion);\                                                                 |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                   |
|                 **styleSheet.Add([\"\~/Content/Site.css\"]);\**                                                             |
|             })]                                                                                                 |
|                                                                                                                                                     |
| [        .Render();]                                                                                            |
|                                                                                                                                                     |
| [ [}]][  ]         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[]{#related-topics}

