---
title: addstylemanagertoanapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\addstylemanagertoanapplication.md
created_at: 2025-07-03
---






#### Add StyleManager to an Application {#add-stylemanager-to-an-application style="tab-stops: 0pt"}

Add the **StyleManager extension** method in the HEAD tag of the View pages (in most cases, It is reasonable to call it within the Site.Master page).[]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]][]**                                                                                                                                                                 |
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
| [\</][head][\>]][ ]                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| **[View][\[cshtml\]][]**                                                                                                              |
|                                                                                                                                                                                                                                                                        |
| [\<][head][ [runat][=\"server\"\>]][] |
|                                                                                                                                                                                                                                                                        |
| [ ][\@{][ Html.Syncfusion().StyleManager().Render();[}]]                                       |
|                                                                                                                                                                                                                                                                        |
| [...][]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                        |
| [...\                                                                                                                                                                                                                                                                  |
| [\</][head][\>]][ ]                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Use **Register()** method to register the Syncfusion components CSS resources.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                               |
|                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().StyleManager()\                      |
|         .Register(styleSheet =\> \                                                                                                                                       |
|             {\                                                                                                                                                           |
|                 styleSheet.Add([ComponentType].][Chart][);\ |
|                 . . .]                                                                                                               |
|                                                                                                                                                                          |
| [                . . .\                                                                                                                                                  |
|             })  [%\>]][]                                 |
|                                                                                                                                                                          |
| []                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                             |
|                                                                                                                                                                          |
| [\@{][ ][Html.Syncfusion().StyleManager()\                      |
|         .Register(styleSheet =\> \                                                                                                                                       |
|             {\                                                                                                                                                           |
|                 styleSheet.Add([ComponentType].][Chart][);\ |
|                 . . .]                                                                                                               |
|                                                                                                                                                                          |
| [                . . .\                                                                                                                                                  |
|             }).Render();[}]][]                           |
|                                                                                                                                                                          |
| []                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

The above code registers the default Office2007Blue theme for added components. All the CSS resources are combined and minified before sending to the browser.

Customization

 

Various customization options have been provided. They are:

[·      ]Minify

[·      ]Combine

[·      ]Register

[·      ]Theme

[·      ]Add CSS Files

 

Minify

 

To enable or disable the Minify feature, use **Minify()** method. Minify is Enabled by default.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                       |
|                                                                                                                                                                                                                                                                                 |
| [         **.Minify([false])**][ ][// Enable/disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                 |
| [        .Register(styleSheet =\> \                                                                                                                                                                                                                                             |
|             {\                                                                                                                                                                                                                                                                  |
|                 styleSheet.Add([ComponentType].][Chart][);\                                                                                                        |
|                 . . .]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [                . . .\                                                                                                                                                                                                                                                         |
|             })  [%\>]][ ]                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [\@{][ ][Html.Syncfusion().StyleManager()]                                                                                        |
|                                                                                                                                                                                                                                                                                |
| [        **.Minify([false])**][ ][// Enable/disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                |
| [\                                                                                                                                                                                                                                                                             |
|         .Register(styleSheet =\> \                                                                                                                                                                                                                                             |
|             {\                                                                                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].][Chart][);\                                                                                                       |
|                 . . .]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [                . . .\                                                                                                                                                                                                                                                        |
|             }).Render();[}]][]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Refer to HTTP Requests and the time details from the following images.[]

Before:[]

[] 

{border="0"}[]

Figure 4: Minify Disabled[]

[] 

After:[]

{border="0"}[]

Figure 5: Minify Enabled

The above images show the size of the resource files before and after the Minfication process. Before the Minification process 19KB file is downloaded in browser (Figure 1), whereas after minification, 14.5KB files are downloaded in browser (Figure 2). 4.5KB size reduced in the above minification process sample 

Combine  

 

 To enable or disable the Combine file feature, use **Combine()** method. Combine is enabled by default.[]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                    |
|                                                                                                                                                                                                                                                                              |
| [        .Minify([false])][ ][// Enable ordisable Minify feature.][] |
|                                                                                                                                                                                                                                                                              |
| **[        .Combine([false])]**[// Enable or disable Combine feature.][]                                          |
|                                                                                                                                                                                                                                                                              |
| [        .Register(styleSheet =\> \                                                                                                                                                                                                                                          |
|             {\                                                                                                                                                                                                                                                               |
|                 styleSheet.Add([ComponentType].Chart);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [                . . .]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [                . . .\                                                                                                                                                                                                                                                      |
| \                                                                                                                                                                                                                                                                            |
|             })  [%\>]][]                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [][]                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[][] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [\@{][ ][Html.Syncfusion().StyleManager()]                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [        .Minify([false])][ ][// Enable ordisable Minify feature.][] |
|                                                                                                                                                                                                                                                                              |
| **[        .Combine([false])]**[// Enable or disable Combine feature.][]                                          |
|                                                                                                                                                                                                                                                                              |
| [        .Register(styleSheet =\> \                                                                                                                                                                                                                                          |
|             {\                                                                                                                                                                                                                                                               |
|                 styleSheet.Add([ComponentType].Chart);\                                                                                                                                                                                              |
|                 . . .]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| [                . . .]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [            }).Render();[}]][ ]                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Refer to HTTP requests and the time details from the following images:[]

[] 

Before:[]

{border="0"}[]

Figure 6: Combine Disabled[]

[] 

After:[]

[] 

{border="0"}[]

Figure 7: Combine Enabled

The above images show the downloading time before and after the Combine process of the resource files. Before the Combine process, the browser takes 257ms to download the css resources (Figure 1), where as after Combine, it takes only 63ms to the download resources (Figure 2). 194ms time is reduced in the above Combine process sample.

[] 

[] 

Register

Two overloads are available for Register () method.

 

1.   Adding StyleManager to an application uses the first overload where the component name can be specified as a String separated by a comma.

 

To add controls in a single line, use the Register() method.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().StyleManager()\                                                                                        |
|                **.Register([\"Chart,Menu\"])**[//Specify the component names   separated by a comma.]][] |
|                                                                                                                                                                                                                                            |
| [               [%\>]][]                                                                                                   |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                                                                                               |
|                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().StyleManager()\                                                                                        |
|                **.Register([\"Chart,Menu\"])**[//Specify the component names   separated by a comma.]][] |
|                                                                                                                                                                                                                                            |
| [.Render();[}]][ ]                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[2.   ]The Second overload uses the [ComponentType][ ]to register the controls.[ ]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                   |
|                                                                                                                                                                                        |
| [\<%][=][Html.Syncfusion().StyleManager()\                                    |
|                ]**[.Register]**[(stylesheets =\>]                          |
|                                                                                                                                                                                        |
| [            {]                                                                                                                                    |
|                                                                                                                                                                                        |
| [                stylesheets.Add([ComponentType].Chart);                              ]                                    |
|                                                                                                                                                                                        |
| [            })]                                                                                                                                   |
|                                                                                                                                                                                        |
| [     [%\>]][ ][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[ ]                                  |
|                                                                                                                                                      |
| []                                                                                                  |
|                                                                                                                                                      |
| []                                                                                                               |
|                                                                                                                                                      |
| [ [\@{]Html.Syncfusion().StyleManager()]                                             |
|                                                                                                                                                      |
| [        **.Register**(stylesheets =\>]                                                                          |
|                                                                                                                                                      |
| [            {]                                                                                                  |
|                                                                                                                                                      |
| [                stylesheets.Add([ComponentType].Chart);                               ] |
|                                                                                                                                                      |
| []                                                                                                               |
|                                                                                                                                                      |
| [            })]                                                                                                 |
|                                                                                                                                                      |
| [.Render();[}]][ ]  |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To avoid child control register, use **DisableChildRegister()** method.

 For example: Grid with paging and sorting feature doesn't require sub controls like Menu, Dialog (these sub controls are used in filtering feature). In order to avoid these child registers, use the DisableChildRegister() as follows:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                      |
|                                                                                                                                                                                                                                                                                |
| [         .Minify([false])][ ][// Enable or disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                |
| [         .Combine([false])[// Enable or disable Combine feature.]][]                                                                           |
|                                                                                                                                                                                                                                                                                |
| [         .Theme([Skins].Almond)[ // Specify theme.]][]                                                                                      |
|                                                                                                                                                                                                                                                                                |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                                                           |
|             {\                                                                                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].Chart)**.DisableChildRegister()**;\                                                                                                                                                                     |
|                 . . .]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [                . . .]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [            })  [%\>]][ ]                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                                                                                                                                     |
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
|                 \                                                                                                                                                                                                                                                              |
|                 styleSheet.Add([ComponentType].Chart)**.DisableChildRegister()**;\                                                                                                                                                                     |
|                 . . .]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [                . . .]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [            }).Render();  [}]][]                                                                                                                              |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

To enable or disable the sub component registrations based on some condition, use the **AllowChildRegister()** method.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                                              |
|                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                         |
| [         .Minify([false])[ // Enable or disable the Minify feature.]]                                   |
|                                                                                                                                                                                         |
| [         .Combine([false])[// Enable or disable the Combine feature.]]                                  |
|                                                                                                                                                                                         |
| [         .Theme([Skins].Almond)[ // Specify Theme. ]]                                                |
|                                                                                                                                                                                         |
| [         .Register(styleSheet =\> \                                                                                                                                                    |
|             {\                                                                                                                                                                          |
|               styleSheet.Add([ComponentType].Chart)**.AllowChildRegister([true]);\**                                                       |
|                . . .]                                                                                                                               |
|                                                                                                                                                                                         |
| [               . . .\                                                                                                                                                                  |
|             })  [%\>]]                                                                                                  |
|                                                                                                                                                                                         |
| [][]                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                                            |
|                                                                                                                                                                                         |
| [\@{][ ][Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                         |
| [         .Minify([false])[ // Enable or disable the Minify feature.]]                                   |
|                                                                                                                                                                                         |
| [         .Combine([false])[// Enable or disable the Combine feature.]]                                  |
|                                                                                                                                                                                         |
| [         .Theme([Skins].Almond)[ // Specify Theme. ]]                                                |
|                                                                                                                                                                                         |
| [         .Register(styleSheet =\> \                                                                                                                                                    |
|             {\                                                                                                                                                                          |
|               styleSheet.Add([ComponentType].Chart)**.AllowChildRegister([true]);\**                                                       |
|                . . .]                                                                                                                               |
|                                                                                                                                                                                         |
| [               . . .]                                                                                                                              |
|                                                                                                                                                                                         |
| [            }).Render();  [}]][ ]                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Theme

To register the CSS Stylesheets for all controls, use the **Theme()** method. Office2007Blue theme is the default theme.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().StyleManager()][]                                          |
|                                                                                                                                                                                                                                                                                    |
| [         .Minify([false])][ ][// Enable or disable the Minify feature.][] |
|                                                                                                                                                                                                                                                                                    |
| [         .Combine([false])[// Enable or disable the Combine feature.]][]                                                                           |
|                                                                                                                                                                                                                                                                                    |
| [         **.Theme([Skins].Almond)**[ // Specify Theme. ]][]                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                                                               |
|             {\                                                                                                                                                                                                                                                                     |
|                 styleSheet.Add([ComponentType].Chart);\                                                                                                                                                                                                    |
|                 . . .\                                                                                                                                                                                                                                                             |
|                 . . .]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                    |
| [            })  [%\>]][]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [\@{][ ][Html.Syncfusion().StyleManager(]                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [         .Minify([false])][ ][// Enable or disable the Minify feature.][] |
|                                                                                                                                                                                                                                                                                    |
| [         .Combine([false])[// Enable or disable the Combine feature.]][]                                                                           |
|                                                                                                                                                                                                                                                                                    |
| [         **.Theme([Skins].Almond)**[ // Specify Theme. ]][]                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                                                               |
|             {\                                                                                                                                                                                                                                                                     |
|                 styleSheet.Add([ComponentType].Chart);\                                                                                                                                                                                                    |
|                 . . .]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                    |
| [                . . .]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                    |
| [            }).Render();  [}]][ ]                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

To configure individual theme for every control use Theme() method inside Register().[]

[  ]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                                                                                                |
|                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().StyleManager()][] |
|                                                                                                                                                                                                                                           |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                      |
|             {\                                                                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Chart)**.Theme([Skins].Blend)**;][]                    |
|                                                                                                                                                                                                                                           |
| [                . . .............]                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [                . . ......]                                                                                                                                                                          |
|                                                                                                                                                                                                                                           |
| [            })  [%\>]][ ]                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [\@{][ ][Html.Syncfusion().StyleManager(         ][] |
|                                                                                                                                                                                                                                                   |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                              |
|             {\                                                                                                                                                                                                                                    |
|                 styleSheet.Add([ComponentType].Chart);\                                                                                                                                                                   |
|                 . . .]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [                . . .            }).Render();  [}]][ ]                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In the above code, Office2007Blue theme registers all the other components and Blend theme registers for Grid.[ ][]

To avoid the theme "override by external Theme() method", use **DontOverride()** method. []

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                                                                   |
|                                                                                                                                                                                                              |
| [  ][\<%][=][Html.Syncfusion().StyleManager()\                       |
|       .Theme([Skins].Almond)[// Specify Theme to all components].    ]                                                     |
|                                                                                                                                                                                                              |
| [      .Register(styleSheet =\> \                                                                                                                                                                            |
|           {\                                                                                                                                                                                                 |
|        styleSheet.Add([ComponentType].Chart).Theme([Skins].Blend**).DontOverride();**\                                                                       |
|         . . .        ]                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [        . . .]                                                                                                                                                          |
|                                                                                                                                                                                                              |
| [           })  [%\>]][ ][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                                                                         |
|                                                                                                                                                                                                                      |
| [  ][\@{][ ][Html.Syncfusion().StyleManager()\                               |
|       .Theme([Skins].Almond)[// Specify Theme to all components].    ]                                                             |
|                                                                                                                                                                                                                      |
| [      .Register(styleSheet =\> \                                                                                                                                                                                    |
|           {\                                                                                                                                                                                                         |
|        styleSheet.Add([ComponentType].Chart).Theme([Skins].Blend**).DontOverride();**\                                                                               |
|         . . .        ]                                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [        . . .]                                                                                                                                                                  |
|                                                                                                                                                                                                                      |
| [           }).Render();  [}]][ ][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

In general, the external Theme() method overrides all the internal component themes register. The DontOverride() method preserves the theme registered in the Register() methods.


{border="0"}Note: The Theme () method will register the CSS style sheets for the specified theme in the html head section. Using this method, we cannot apply themes for the controls (cannot add CSS classes). If we don't use StyleManager, then the CSS style sheet for the default theme or the specified theme will be registered just before controls render starts. The StyleManager is introduced to improve the performance using its Minify and Combine feature.


Add CSS Files

To include the application CSS files to the styleManager, use the **Add()** method.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                          |
|                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().StyleManager()\ |
|         .Theme([Skins].Almond)[// Specify the theme to all components.]\                              |
|         .Register(styleSheet =\> \                                                                                                                  |
|             {\                                                                                                                                      |
|                 styleSheet.Add([ComponentType].Chart).Theme([Skins].Blend).DontOverride();\         |
|                 **styleSheet.Add([\"\~/Content/Site.css\"]);\**                                                             |
|             })  [%\>]][]            |
|                                                                                                                                                     |
| []                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                |
|                                                                                                                                                             |
| [\@{][ ][Html.Syncfusion().StyleManager()\         |
|         .Theme([Skins].Almond)[// Specify the theme to all components.]\                                      |
|         .Register(styleSheet =\> \                                                                                                                          |
|             {\                                                                                                                                              |
|                 styleSheet.Add([ComponentType].Chart).Theme([Skins].Blend).DontOverride();                \ |
|                 **styleSheet.Add([\"\~/Content/Site.css\"]);\**                                                                     |
|             }).Render();  [}]][]            |
|                                                                                                                                                             |
| []                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

Add ScriptManager to an Application

 

The **ScriptManager()** method can be added after all the components on the page. Generally, you can use this method at the end of the master page.[]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                                                                 |
|                                                                                                                                                                                                            |
| [\<][body][\>][ ] |
|                                                                                                                                                                                                            |
| [...]                                                                                                                                                                  |
|                                                                                                                                                                                                            |
| [...]                                                                                                                                                                  |
|                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().ScriptManager()[%\>]\                      |
| [\</][body][\>]][]                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                                                               |
|                                                                                                                                                                                                            |
| [\<][body][\>][ ] |
|                                                                                                                                                                                                            |
| [...]                                                                                                                                                                  |
|                                                                                                                                                                                                            |
| [...]                                                                                                                                                                  |
|                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().ScriptManager().Render();[}]\              |
| [\</][body][\>]]                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Customization

[] 

**Minify** - To enable or disable the minify feature, use the **Minify()** method. Minify is enabled by default.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**[]                                                                                                                                 |
|                                                                                                                                                                                                                                            |
| [\<][body][\>][ ]                     |
|                                                                                                                                                                                                                                            |
| [...][]                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [...][]                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().ScriptManager()][] |
|                                                                                                                                                                                                                                            |
| [.Minify([true])][]                                                                                                               |
|                                                                                                                                                                                                                                            |
| [%\>][\                                                                                                                                                                            |
| [\</][body][\>]]                                                                                                                      |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[]                                                                                                                      |
|                                                                                                                                                                                                                                   |
| [\<][body][\>][ ]            |
|                                                                                                                                                                                                                                   |
| [...][]                                                                                                                                       |
|                                                                                                                                                                                                                                   |
| [...][]                                                                                                                                       |
|                                                                                                                                                                                                                                   |
| [\@{][ ][Html.Syncfusion().ScriptManager().Minify([true]).Render();[}]\ |
| [\</][body][\>]][ ]                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[]{#related-topics}

