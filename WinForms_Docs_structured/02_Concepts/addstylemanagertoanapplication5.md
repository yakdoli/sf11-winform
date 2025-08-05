---
title: addstylemanagertoanapplication5.md
original_path: WinForms_Docs/02_Concepts/addstylemanagertoanapplication5.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Add StyleManager to an Application {#add-stylemanager-to-an-application style="tab-stops: 0pt"}

Add the **StyleManager extension** method in the HEAD tag of the View pages (in most cases, It is reasonable to call it within the Site.Master page).[]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [\<] [head] [ [runat][=\"server\"\>]]     |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.Syncfusion().StyleManager()[%\>]] |
|                                                                                                                                                                                                                            |
| [...]                                                                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [...\                                                                                                                                                                                                                      |
| [\</][head][\>]]                                                                                                      |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Use the *Register()* method to register the Syncfusion components CSS resources.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                             |
|                                                                                                                                                       |
| []                                                                                                                |
|                                                                                                                                                       |
| [\<%] [=] [Html.Syncfusion().StyleManager()\ |
|         .Register(styleSheet =\> \                                                                                                                    |
|             {\                                                                                                                                        |
|                 styleSheet.Add([ComponentType].Chart);\                                                                       |
|                 \...]                                                                                             |
|                                                                                                                                                       |
| [                \...                ]                                                                            |
|                                                                                                                                                       |
| [            })  [%\>]]                                                               |
|                                                                                                                                                       |
| []                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The above code registers the default Office2007Blue theme for added components. All the CSS resources are combined and minified before sending to browser.

Customization

 

Various customization options have been provided. They are:

[·      ]Minify

[·      ]Combine

[·      ]Register

[·      ]Theme

[·      ]Add CSS Files

 

**Minify ** []

[You can enable or disable the Minify feature using the *Minify()* method. By default this is enabled.]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                 |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [\<%] [=] [Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                           |
| [         **.Minify([false])**[ // Enable/disable Minify feature.]]                                        |
|                                                                                                                                                                                           |
| [        .Register(styleSheet =\> \                                                                                                                                                       |
|             {\                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Chart);\                                                                                                           |
|                 \...]                                                                                                                                 |
|                                                                                                                                                                                           |
| [                \...\                                                                                                                                                                    |
|             })  [%\>]]                                                                                                    |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Please refer HTTP Requests and the time details from the below images.[]

Before:[]

[] 

{border="0"} []

Figure 4: Minify Disabled[]

[] 

After:[]

{border="0"} []

Figure 5: Minify Enabled

The above images show the size of the resource files before and after the Minfication process. Before the Minification process 19KB file is downloaded in browser (Figure 1), whereas after minification, 14.5KB files downloaded in browser (Figure 2). 4.5KB size reduced in the above minification process sample 

 

Combine  

 

 You can enable or disable the Combine file feature using the *Combine()*method. By default this is enabled.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                                                   |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\<%] [=] [Html.Syncfusion().StyleManager()]                                   |
|                                                                                                                                                                                                                             |
| [         .Minify([false])[ // Enable or disable Minify feature.]]                                                                           |
|                                                                                                                                                                                                                             |
| **[          .Combine([false])]** [// Enable or disable Combine feature.] [] |
|                                                                                                                                                                                                                             |
| [        .Register(styleSheet =\> \                                                                                                                                                                                         |
|             {\                                                                                                                                                                                                              |
|                 styleSheet.Add([ComponentType].Chart);\                                                                                                                                             |
|                 \...]                                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [                \...\                                                                                                                                                                                                      |
|             })  [%\>]]                                                                                                                                      |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Please refer HTTP Requests and the time details from the below images:[]

[] 

Before:[]

{border="0"} []

Figure 6: Combine Disabled[]

[] 

After:[]

[] 

{border="0"} []

Figure 7: Combine Enabled

The above images show the downloading time before and after the Combine process of the resource files. Before the Combine process, browser takes 257ms to download the css resources (Figure 1), where as after Combine it takes only 63ms to the download resources (Figure 2). 194ms time is reduced in the above Combine process sample.[]

[] 

Register

There are two overloads available for the *Register()* method.

[] 

[·      ]Adding StyleManager to an application uses the first overload where the component names can be specified as the String separated by comma.

[] 

To add controls in a single line, use the *Register()* method.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                |
|                                                                                                                                                                                          |
| [\<%] [=] [Html.Syncfusion().StyleManager()\                                    |
|                **.Register([\"Chart,Menu\"])**[//Specify the component names   separated by a comma.]] |
|                                                                                                                                                                                          |
| [               [%\>]]                                                                                                   |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Second overload uses the *ComponentType* to register the controls.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                             |
|                                                                                                                                                       |
| [\<%] [=] [Html.Syncfusion().StyleManager()\ |
|                **.Register**(stylesheets =\>]                                                                     |
|                                                                                                                                                       |
| [            {]                                                                                                   |
|                                                                                                                                                       |
| [                stylesheets.Add([ComponentType].Chart);                              ]   |
|                                                                                                                                                       |
| [            })]                                                                                                  |
|                                                                                                                                                       |
| [     [%\>] ]                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can avoid child control register using the *DisableChildRegister()* method.

[] 

 For example: Grid with paging and sorting feature doesn't require sub controls like Menu, Dialog (these sub controls are used in filtering feature). In order to avoid these child registers use the DisableChildRegister() as  follows:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                 |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [\<%] [=] [Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                           |
| [         .Minify([false])[ // Enable or disable Minify feature.]]                                         |
|                                                                                                                                                                                           |
| [         .Combine([false])[// Enable or disable Combine feature.]]                                        |
|                                                                                                                                                                                           |
| [         .Theme([Skins].Almond)[ // Specify theme.]]                                                   |
|                                                                                                                                                                                           |
| [         .Register(styleSheet =\> \                                                                                                                                                      |
|             {\                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Chart)**.DisableChildRegister()**;]                                            |
|                                                                                                                                                                                           |
| [                . . .]                                                                                                                               |
|                                                                                                                                                                                           |
| [                . . .\                                                                                                                                                                   |
|             })  [%\>]]                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can enable or disable the sub component registrations based on the condition you define using the *AllowChildRegister()*  method.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                 |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [\<%] [=] [Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                           |
| [         .Minify([false])[ // Enable or disable Minify feature.]]                                         |
|                                                                                                                                                                                           |
| [         .Combine([false])[// Enable or disable Combine feature.]]                                        |
|                                                                                                                                                                                           |
| [         .Theme([Skins].Almond)[ // Specify Theme. ]]                                                  |
|                                                                                                                                                                                           |
| [         .Register(styleSheet =\> \                                                                                                                                                      |
|             {\                                                                                                                                                                            |
|               styleSheet.Add([ComponentType].Chart)**.AllowChildRegister([true]);\**                                                         |
|               . . .]                                                                                                                                  |
|                                                                                                                                                                                           |
| [              . . .\                                                                                                                                                                     |
|             })  [%\>]]                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Theme[]

*[To]* register the CSS Stylesheets for all controls, use the *Theme()* method. Default theme is Office2007Blue.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                 |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [\<%] [=] [Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                           |
| [         .Minify([false])[ // Enable or disable Minify feature.]]                                         |
|                                                                                                                                                                                           |
| [         .Combine([false])[// Enable or disable Combine feature.]]                                        |
|                                                                                                                                                                                           |
| [         **.Theme([Skins].Almond)**[ // Specify Theme. ]]                                              |
|                                                                                                                                                                                           |
| [         .Register(styleSheet =\> \                                                                                                                                                      |
|             {\                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Chart);\                                                                                                           |
|                 . . .]                                                                                                                                |
|                                                                                                                                                                                           |
| [                . . .\                                                                                                                                                                   |
|             })  [%\>]]                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

You can configure the individual theme for every controls using the *Theme()*method inside the *Register().*

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                 |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [\<%] [=] [Html.Syncfusion().StyleManager()] |
|                                                                                                                                                                                           |
| [         .Register(styleSheet =\> \                                                                                                                                                      |
|             {\                                                                                                                                                                            |
|                 styleSheet.Add([ComponentType].Chart)**.Theme([Skins].Blend)**;]                      |
|                                                                                                                                                                                           |
| [                . . .]                                                                                                                               |
|                                                                                                                                                                                           |
| [                . . .\                                                                                                                                                                   |
|             })  [%\>]]                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In this above code, Office2007Blue theme registers all the other components and Blend theme registers for Grid.[]

[ ] [ ] []

You can avoid theme override by the external *Theme()* method using the *DontOverride()* method.

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                             |
|                                                                                                                                                       |
| []                                                                                                                |
|                                                                                                                                                       |
| [  [\<%][=]Html.Syncfusion().StyleManager()\                                                         |
|    .Theme([Skins].Almond)[// Specify Theme to all components].    ] |
|                                                                                                                                                       |
| [   .Register(styleSheet =\> \                                                                                                                        |
|           {\                                                                                                                                          |
|         styleSheet.Add([ComponentType].Chart).Theme([Skins].Blend**).DontOverride();**\               |
|         . . .]                                                                                                    |
|                                                                                                                                                       |
| [        . . .\                                                                                                                                       |
|            })  [%\>]]                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In general, the external Theme() method overrides all the internal component themes register. The DontOverride() method preserves the theme registered in the Register() methods.


{border="0"}Note: The Theme () method will register the CSS style sheets for the specified theme in the html head section. Using this method, we cannot apply themes for the controls (cannot add CSS classes). If we don't use StyleManager then the CSS style sheet for default theme or specified theme will be registered just before controls render starts. The StyleManager is introduced to improve the performance using its Minify and Combine feature.

 


**Add the CSS Files**

To include the application CSS files to the styleManager, use the *Add()* method.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                   |
|                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                             |
| [\<%] [=] [Html.Syncfusion().StyleManager()\       |
|         .Theme([Skins].Almond)[// Specify Theme to all components.]\                                          |
|         .Register(styleSheet =\> \                                                                                                                          |
|             {\                                                                                                                                              |
|                 styleSheet.Add([ComponentType].Chart).Theme([Skins].Blend).DontOverride();                \ |
|                 **styleSheet.Add([\"\~/Content/Site.css\"]);**]                                 |
|                                                                                                                                                             |
| **[                . . .\                                                                                                                                   |
| ]** [            })  [%\>]]                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Add ScriptManager to an Application

 

The *ScriptManager()* method can be added after all the components on the page. Generally, you can use this method at the end of the master page.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                                    |
|                                                                                                                                                                                                              |
| [\<] [body] [\>] [] |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [...]                                                                                                                                                                    |
|                                                                                                                                                                                                              |
| [...]                                                                                                                                                                    |
|                                                                                                                                                                                                              |
| [\<%] [=] [Html.Syncfusion().ScriptManager()[%\>]\                      |
| [\</][body][\>]]                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Customization

[] 

**Minify** - To enable or disable the minify feature, use the **Minify()** method. Minify is enabled by default.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                                    |
|                                                                                                                                                                                                              |
| [\<] [body] [\>] [] |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [...]                                                                                                                                                                    |
|                                                                                                                                                                                                              |
| [...]                                                                                                                                                                    |
|                                                                                                                                                                                                              |
| [\<%] [=] [Html.Syncfusion().ScriptManager()]                   |
|                                                                                                                                                                                                              |
| [.Minify([true])]                                                                                                                                   |
|                                                                                                                                                                                                              |
| [%\>] [\                                                                                                                                             |
| [\</] [body] [\>] ]                                                                                     |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

