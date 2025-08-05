---
title: addstylemanagertoanapplication1.md
original_path: WinForms_Docs/02_Concepts/addstylemanagertoanapplication1.md
created_at: 2025-08-05
---






#### Add StyleManager to an Application {#add-stylemanager-to-an-application style="tab-stops: 0pt"}

[] 

Add the **StyleManager** extension method in the [\<][head][\>] element of the view pages (in most cases, it is reasonable to call it within the Site.Master page).[]

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

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [\<][head][ [runat][=\"server\"\>]][]                                  |
|                                                                                                                                                                                                                                                                                                         |
| [   [\@{]Html.Syncfusion().StyleManager()]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [        .Register(stylesheets =\>]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| [             ][stylesheets][.Add([ComponentType].][Schedule][);] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [            }).Render();[}]]**[]**                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [\                                                                                                                                                                                                                                                                                                      |
| [\</][head][\>]][]                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[] 

Use the **Register()** method to register the Syncfusion component's CSS resources.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                  |
|                                                                                                                                                     |
| []                                                                                                  |
|                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().StyleManager()\ |
|         .Register(styleSheet =\> \                                                                                                                  |
|             {\                                                                                                                                      |
|                 styleSheet.Add([ComponentType].Grid);\                                                                      |
|                 . . .]                                                                                          |
|                                                                                                                                                     |
| [                . . .\                                                                                                                             |
|             })  [%\>]][]            |
|                                                                                                                                                     |
| []                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [   [\@{]Html.Syncfusion().StyleManager()]                                                                                    |
|                                                                                                                                                                                                            |
| [        .Register(stylesheets =\>]                                                                                                                       |
|                                                                                                                                                                                                            |
| [            {]                                                                                                                                           |
|                                                                                                                                                                                                            |
| [             ][stylesheets][.Add([ComponentType].Grid);] |
|                                                                                                                                                                                                            |
| []                                                                                                                                                        |
|                                                                                                                                                                                                            |
| [            }).Render();[}]]**[]**                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The code above registers the default Office2007Blue theme for added components. All the CSS resources are combined and minified before being sent to the browser.

 

Customization

Various customization options have been provided. They are:

 

[·      ]Minify

[·      ]Combine

[·      ]Register

[·      ]Theme

[·      ]Add CSS files

 

Minify

 

To enable or disable the minify feature, use the **Minify()** method. Minify is enabled by default.

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
| [        .Register(styleSheet =\> \                                                                                                                                                                                                                                             |
|             {\                                                                                                                                                                                                                                                                  |
|                 styleSheet.Add([ComponentType].Grid);\                                                                                                                                                                                                  |
|                 . . .]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [                . . .\                                                                                                                                                                                                                                                         |
|             })  [%\>]][]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                    |
| [ ][  [\@{]Html.Syncfusion().StyleManager()]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                    |
| [        ]**[.Minify([false])]**[ ][// Enable/disable Minify feature.][] |
|                                                                                                                                                                                                                                                                                                                                    |
| [        .Register(][styleSheet][ =\>]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                    |
| [            {                                           ]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                    |
| [                styleSheet.Add([ComponentType].Grid);\                                                                                                                                                                                                                                                    |
|                 . . .]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                    |
| [                . . .\                                                                                                                                                                                                                                                                                                            |
| ][            ][}).Render();  [}]][]                                                                                          |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Please refer to the HTTP requests and the time details from the images below.[]

[] 

**Before:[]**

[] 

{border="0"}

Figure 5: Minify Disabled.

[] 

**After:[]**

{border="0"}

Figure 6: Minify Enabled

The preceding images show the size of the resource files before and after the minfication process. Before the minification process a 19-KB file is downloaded in the browser (Figure 5), whereas after minification a 14.5-KB file is downloaded in the browser (Figure 6). 4.5 KB size reduced in the minification process sample above.[]

[] 

Combine

[] 

To enable or disable the combine file feature, use the **Combine()** method. Combine is enabled by default.[]

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
| **[         .Combine([false])]**[// Enable or disable Combine feature.][]                                          |
|                                                                                                                                                                                                                                                                               |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                                                          |
|             {\                                                                                                                                                                                                                                                                |
|                 styleSheet.Add([ComponentType].Grid);\                                                                                                                                                                                                |
|                 . . .]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [                . . .\                                                                                                                                                                                                                                                       |
|             })  [%\>]][]                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [ ][  [\@{]Html.Syncfusion().StyleManager()]                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| [          ][.Minify([false])][ ][// Enable/disable Minify feature.]             |
|                                                                                                                                                                                                                                                                                           |
| [         ]**[.Combine([false])]**[// Enable or disable Combine feature.][] |
|                                                                                                                                                                                                                                                                                           |
| [          .Register(][styleSheet][ =\>]                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| [            {                                           ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                           |
| [                styleSheet.Add([ComponentType].Grid);\                                                                                                                                                                                                           |
|                 . . .]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| [                . . .\                                                                                                                                                                                                                                                                   |
| ][            }).Render();[]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Please refer to the HTTP requests and the time details from the following images:[]

[] 

**Before:**

[] 

{border="0"}

[Figure]{#_Ref311798756} 7: Combine Disabled[]

[] 

**After:[]**

[] 

{border="0"}

[Figure]{#_Ref311798767} 8: Combine Enabled

 

The images above show the downloading time before and after the resource files go through the combine process. Before the combine process, the browser takes 257 ms to download the CSS resources (Figure 7, whereas after the combine process it takes only 63 ms to download the resources (Figure 8). 194 ms of download time is reduced in the combine process sample above.[]

[] 

[] 

Register

Two overloads are available for the **Register()** method.

 

[1.    ]Adding **StyleManager** to an application uses the first overload where the component name can be specified as a string separated by commas.

 

To add controls in a single line, use the **Register()** method.[]

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]][]**                                                                                                                                        |
|                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().StyleManager()\                                                                                              |
|                **.Register([\"Grid,Menu,Toolbar"])**[//Specify the component names   separated by a comma.]][] |
|                                                                                                                                                                                                                                                  |
| [               [%\>]][]                                                                                                         |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**[]                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [\@{][ ][Html.Syncfusion().StyleManager()\                                                                                               |
|                **.Register([\"Grid,Menu,Toolbar\"])**[//Specify the component names   separated by a comma.]][] |
|                                                                                                                                                                                                                                                   |
| [.Render();]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [}][ ]                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[2.    ]The second overload uses the [ComponentType][ ]to register the controls.[ ][]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[]                                                                                          |
|                                                                                                                                                                                        |
| [\<%][=][Html.Syncfusion().StyleManager()\                                    |
|                ]**[.Register]**[(stylesheets =\>]                          |
|                                                                                                                                                                                        |
| [            {]                                                                                                                                    |
|                                                                                                                                                                                        |
| [                stylesheets.Add([ComponentType].Grid);                              ]                                     |
|                                                                                                                                                                                        |
| [            })]                                                                                                                                   |
|                                                                                                                                                                                        |
| [     [%\>]][ ][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**[ ]                                  |
|                                                                                                                                                     |
| []                                                                                                 |
|                                                                                                                                                     |
| []                                                                                                              |
|                                                                                                                                                     |
| [ [\@{]Html.Syncfusion().StyleManager()]                                            |
|                                                                                                                                                     |
| [        **.Register**(stylesheets =\>]                                                                         |
|                                                                                                                                                     |
| [            {]                                                                                                 |
|                                                                                                                                                     |
| [                stylesheets.Add([ComponentType].Grid);                               ] |
|                                                                                                                                                     |
| []                                                                                                              |
|                                                                                                                                                     |
| [            })]                                                                                                |
|                                                                                                                                                     |
| [.Render();[}]][ ] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To avoid child control register, use the **DisableChildRegister()** method.

[] 

**For example:** A grid with paging and sorting features doesn't require sub-controls like Menu or Dialog (these sub-controls are used in the filtering feature). In order to avoid these child registers, use **DisableChildRegister()** as follows:

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
| [         .Theme([Skins].Almond)[ // Specify theme.]][]                                                                                      |
|                                                                                                                                                                                                                                                                                |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                                                           |
|             {\                                                                                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].Grid)**.DisableChildRegister()**;\                                                                                                                                                                      |
|                 . . .]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [                . . .\                                                                                                                                                                                                                                                        |
|             })  [%\>]][]                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| [ ][  [\@{]Html.Syncfusion().StyleManager()]                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [          ][.Minify([false])][ ][// Enable/disable Minify feature.] |
|                                                                                                                                                                                                                                                                               |
| [         ][.Combine([false])][// Enable or disable Combine feature.]                                            |
|                                                                                                                                                                                                                                                                               |
| [         ][.Theme([Skins].Almond)[ // Specify theme.]][]                                |
|                                                                                                                                                                                                                                                                               |
| [          .Register(][styleSheet][ =\>]                                                                                                |
|                                                                                                                                                                                                                                                                               |
| [            {                                           ]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [                styleSheet.Add([ComponentType].Grid)**.DisableChildRegister()**;\                                                                                                                                                                    |
|                 . . .]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [                . . .\                                                                                                                                                                                                                                                       |
| ][            }).Render();[]]                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

To enable or disable the sub-component registrations based on some condition, use the **AllowChildRegister()** method.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                         |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().StyleManager()]    |
|                                                                                                                                                                                            |
| [         .Minify([false])[ // Enable or disable Minify feature.]]                                          |
|                                                                                                                                                                                            |
| [         .Combine([false])[// Enable or disable Combine feature.]]                                         |
|                                                                                                                                                                                            |
| [         .Theme([Skins].Almond)[ // Specify Theme. ]]                                                   |
|                                                                                                                                                                                            |
| [         .Register(styleSheet =\> \                                                                                                                                                       |
|             {\                                                                                                                                                                             |
|               styleSheet.Add([ComponentType].Grid)**.AllowChildRegister([true]);**                 . . .] |
|                                                                                                                                                                                            |
| [              . . .           \                                                                                                                                                           |
|             })  [%\>]]                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| [ ][  [\@{]Html.Syncfusion().StyleManager()]                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [          ][.Minify([false])][ ][// Enable/disable Minify feature.] |
|                                                                                                                                                                                                                                                                               |
| [         ][.Combine([false])][// Enable or disable Combine feature.]                                            |
|                                                                                                                                                                                                                                                                               |
| [         ][.Theme([Skins].Almond)[ // Specify theme.]][]                                |
|                                                                                                                                                                                                                                                                               |
| [          .Register(][styleSheet][ =\>]                                                                                                |
|                                                                                                                                                                                                                                                                               |
| [            {                                           ]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [                styleSheet.Add([ComponentType].Grid)**.AllowChildRegister([true]);\**                                                                                                                                           |
| \                                                                                                                                                                                                                                                                             |
|                 . . .]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [                . . .\                                                                                                                                                                                                                                                       |
| ][            }).Render();[}]]                                                                                                                               |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Theme

To register the CSS stylesheets for all controls, use the **Theme()** method. Office2007Blue is the default theme.[]

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
| [         **.Theme([Skins].Almond)**[ // Specify Theme. ]][]                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                                                           |
|             {\                                                                                                                                                                                                                                                                 |
|                 styleSheet.Add([ComponentType].Grid);\                                                                                                                                                                                                 |
|                 . . .]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [                . . .\                                                                                                                                                                                                                                                        |
|             })  [%\>]][]                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| [ ][  [\@{]Html.Syncfusion().StyleManager()]                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [          ][.Minify([false])][ ][// Enable/disable Minify feature.]  |
|                                                                                                                                                                                                                                                                                |
| [         ][.Combine([false])][// Enable or disable Combine feature.]                                             |
|                                                                                                                                                                                                                                                                                |
| [         ]**[.Theme([Skins].Almond)]**[ // Specify theme.][] |
|                                                                                                                                                                                                                                                                                |
| [          .Register(][styleSheet][ =\>]                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [            {                                           ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [                styleSheet.Add([ComponentType].Grid**;**\                                                                                                                                                                                             |
|                 . . .]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [                . . .\                                                                                                                                                                                                                                                        |
| ][            }).Render();[}]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

To configure individual themes for every control use the **Theme()** method inside **Register()**.[]

[  ]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().StyleManager()][] |
|                                                                                                                                                                                                                                           |
| [         .Register(styleSheet =\> \                                                                                                                                                                                                      |
|             {\                                                                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Grid)**.Theme([Skins].Blend)**;][]                     |
|                                                                                                                                                                                                                                           |
| [                styleSheet.Add([ComponentType].Accordion);\                                                                                                                                                      |
|                 styleSheet.Add([ComponentType].Menu);\                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Toolbar);\                                                                                                                                                         |
|             })  [%\>]][]                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                 |
|                                                                                                                                                                                                      |
| []                                                                                                                                                   |
|                                                                                                                                                                                                      |
| [ ][  [\@{]Html.Syncfusion().StyleManager()          ] |
|                                                                                                                                                                                                      |
| [          .Register(][styleSheet][ =\>]                       |
|                                                                                                                                                                                                      |
| [            {                                           ]                                                                                          |
|                                                                                                                                                                                                      |
| [                styleSheet.Add([ComponentType].Grid)**.Theme([Skins].Blend)**;\                                                                     |
|                 . . .]                                                                                                                                           |
|                                                                                                                                                                                                      |
| [                . . .\                                                                                                                                                                              |
| ][            }).Render();[}]]                                                      |
|                                                                                                                                                                                                      |
| []                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

In the code above, the Blend theme registers for the grid and the Office2007Blue theme registers all the other components.[]

 

To avoid theme overrides by external **Theme()** methods, use the **DontOverride()** method. []

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                     |
|                                                                                                                                                                                        |
| []                                                                                                                                     |
|                                                                                                                                                                                        |
| [  ][\<%][=][Html.Syncfusion().StyleManager()\ |
|       .Theme([Skins].Almond)[// Specify Theme to all components].     ]                              |
|                                                                                                                                                                                        |
| [      .Register(styleSheet =\> \                                                                                                                                                      |
|       {\                                                                                                                                                                               |
|         styleSheet.Add([ComponentType].Grid).Theme([Skins].Blend**).DontOverride();**\                                                 |
|         . . .]                                                                                                                                     |
|                                                                                                                                                                                        |
| [        . . .\                                                                                                                                                                        |
|       })  [%\>]][]                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[\
\
]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| [ ][  [\@{]Html.Syncfusion().StyleManager() ]                            |
|                                                                                                                                                                                                                        |
| [       .Theme([Skins].Almond)[// Specify Theme to all components].    ][         ] |
|                                                                                                                                                                                                                        |
| [        .Register(][styleSheet][ =\>]                                           |
|                                                                                                                                                                                                                        |
| [        {                                         ]                                                                                                                  |
|                                                                                                                                                                                                                        |
| [          styleSheet.Add([ComponentType].Grid).Theme([Skins].Blend**). DontOverride();**\                                                                             |
|           . . .]                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [          . . .\                                                                                                                                                                                                      |
| ][            }).Render();[}]]                                                                        |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In general, the external **Theme()** method overrides all the internal component themes registered. The **DontOverride()** method preserves the theme registered in the **Register()** method.

 


{border="0"}Note: The Theme () method will register the CSS style sheets for the specified theme in the the HEAD section of the HTML. Using this method, we cannot apply themes for the controls (cannot add CSS classes). If we don't use StyleManager then the CSS style sheet for default theme or specified theme will be registered just before the control rendering starts. The StyleManager is introduced to improve the performance using its minify and combine features.[]


[] 

Add CSS Files

To add the application CSS files to StyleManager, use the **Add()** method.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                               |
|                                                                                                                                                                                  |
| []                                                                                                                               |
|                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().StyleManager()\                              |
|         .Theme([Skins].Almond)[// Specify theme to all components.]\                                                               |
|         .Register(styleSheet =\> \                                                                                                                                               |
|             {\                                                                                                                                                                   |
|                 styleSheet.Add([ComponentType].Grid).Theme([Skins].Blend).DontOverride();                \                       |
|                 **styleSheet.Add([\"\~/Content/Site.css\"]);**]                                                      |
|                                                                                                                                                                                  |
| **[                . . .]**                                                                                                                  |
|                                                                                                                                                                                  |
| **[                . . .]**                                                                                                                  |
|                                                                                                                                                                                  |
| **[          \                                                                                                                                                                   |
| ]**[            })  [%\>]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| [ ][  [\@{]Html.Syncfusion().StyleManager() ]                            |
|                                                                                                                                                                                                                        |
| [       .Theme([Skins].Almond)[// Specify Theme to all components].    ][         ] |
|                                                                                                                                                                                                                        |
| [        .Register(][styleSheet][ =\>]                                           |
|                                                                                                                                                                                                                        |
| [        {                                         ]                                                                                                                  |
|                                                                                                                                                                                                                        |
| [          styleSheet.Add([ComponentType].Grid).Theme([Skins].Blend**).** DontOverride();]                                         |
|                                                                                                                                                                                                                        |
| [          **styleSheet.Add([\"\~/Content/Site.css\"]);**][\                                                                                               |
|           . . .]                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [          . . .\                                                                                                                                                                                                      |
| ][            }).Render();[}]]                                                                        |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[]{#related-topics}

