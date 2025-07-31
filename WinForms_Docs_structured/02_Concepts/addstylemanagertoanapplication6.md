---
title: addstylemanagertoanapplication6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\addstylemanagertoanapplication6.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Add StyleManager to an Application {#add-stylemanager-to-an-application style="TEXT-INDENT: -43.2pt; MARGIN-LEFT: 43.2pt; tab-stops: 43.2pt"}

 

Add the **StyleManager extension** method in the HEAD tag of the View pages (in most cases, It is reasonable to call it within the Site.Master page).[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [\<] [head] [ [runat][=\"server\"\>]]     |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.Syncfusion().StyleManager()[%\>]] |
|                                                                                                                                                                                                                            |
| [...]                                                                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [\</] [head] [\>] []              |
|                                                                                                                                                                                                                            |
| [ **\[Razor\]**]                                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [\<] [head] [ [runat][=\"server\"\>]]     |
|                                                                                                                                                                                                                            |
| [@] [Html.Syncfusion().StyleManager()]                                                                                         |
|                                                                                                                                                                                                                            |
| [...]                                                                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [\</] [head] [\>] []              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Use **Register()** method to register the Syncfusion components CSS resources.[]

+--------------------------------------------------------------------------------------------------------------------------+
| [ **\[ASPX\]**]                                                                      |
|                                                                                                                          |
| [\<%] [{]                    |
|                                                                                                                          |
| [          Html.Syncfusion().StyleManager()]                                         |
|                                                                                                                          |
| [              .Register(stylesheets =\>]                                            |
|                                                                                                                          |
| [               {]                                                                   |
|                                                                                                                          |
| [                   stylesheets.Add([ComponentType].Chart);] |
|                                                                                                                          |
| [               ] [}).Render();]                 |
|                                                                                                                          |
| [ } [%\>]]                                               |
|                                                                                                                          |
| [ [] ]                                                   |
|                                                                                                                          |
| [ **\[Razor\]**]                                                                     |
|                                                                                                                          |
| [    [\@{]]                                              |
|                                                                                                                          |
| [        Html.Syncfusion().StyleManager()]                                           |
|                                                                                                                          |
| [        ] [.Register(stylesheets =\>]           |
|                                                                                                                          |
| [            {]                                                                      |
|                                                                                                                          |
| [                stylesheets.Add([ComponentType].Chart);]    |
|                                                                                                                          |
| [            }).Render();]                                                           |
|                                                                                                                          |
| [    [}]]                                                |
|                                                                                                                          |
| []                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

The above code registers the default DarkNight theme for added components. All the CSS resources are combined and minified before sending to browser.[]

Customization

Various customization options have been provided. They are:

[·      ]Minify

[·      ]Combine

[·      ]Register

[·      ]Theme

[·      ]Add CSS Files

Minify

 To enable or disable Minify feature, use **Minify()** method. Minify is Enabled by default.[ ]

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                |
|                                                                                                                          |
| [    [\<%]{]                                             |
|                                                                                                                          |
| [          Html.Syncfusion().StyleManager()]                                         |
|                                                                                                                          |
| [              ]                                                                     |
|                                                                                                                          |
| [              .Minify([false]) ]                               |
|                                                                                                                          |
| [              ]                                                                     |
|                                                                                                                          |
| [              .Register(stylesheets =\>]                                            |
|                                                                                                                          |
| [               {]                                                                   |
|                                                                                                                          |
| [                   stylesheets.Add([ComponentType].Chart);] |
|                                                                                                                          |
| [               }).Render();]                                                        |
|                                                                                                                          |
| [      } [%\>]]                                          |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| []                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]** []                            |
|                                                                                                                       |
| [    [\@{]]                                           |
|                                                                                                                       |
| [        Html.Syncfusion().StyleManager()]                                        |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [        .Minify([false])]                                   |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [        .Register(stylesheets =\>]                                               |
|                                                                                                                       |
| [            {]                                                                   |
|                                                                                                                       |
| [                stylesheets.Add([ComponentType].Chart);] |
|                                                                                                                       |
| [            }).Render();]                                                        |
|                                                                                                                       |
| [    [}]]                                             |
|                                                                                                                       |
| []                                                                                |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

Please refer HTTP Requests and the time details from the below images.[]

Before:[]

[] 

{border="0"} []

Figure 3: Minify Disabled.

[] 

After:[]

{border="0"} []

Figure 4: Minify Enabled.

The above images show the size of the resource files before and after the Minfication process. Before the Minification process 19KB file is downloaded in browser (Figure 1), whereas after minification, 14.5KB files downloaded in browser (Figure 2). 4.5KB size reduced in the above minification process sample.[]

Combine

 To enable or disable Combine file feature, use **Combine()** method. Combine is Enabled by default.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                |
|                                                                                                                          |
| [    [\<%]{]                                             |
|                                                                                                                          |
| [          Html.Syncfusion().StyleManager()]                                         |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| [              .Combine([false])]                               |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| [              .Register(stylesheets =\>]                                            |
|                                                                                                                          |
| [               {]                                                                   |
|                                                                                                                          |
| [                   stylesheets.Add([ComponentType].Chart);] |
|                                                                                                                          |
| [               }).Render();]                                                        |
|                                                                                                                          |
| [      } [%\>]]                                          |
|                                                                                                                          |
| []                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]** []                            |
|                                                                                                                       |
| [    [\@{]]                                           |
|                                                                                                                       |
| [        Html.Syncfusion().StyleManager()]                                        |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [        .Combine([false])]                                  |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [        .Register(stylesheets =\>]                                               |
|                                                                                                                       |
| [            {]                                                                   |
|                                                                                                                       |
| [                stylesheets.Add([ComponentType].Chart);] |
|                                                                                                                       |
| [            }).Render();]                                                        |
|                                                                                                                       |
| [    [}]]                                             |
|                                                                                                                       |
| []                                                                                |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

Please refer HTTP Requests and the time details from the below images:[]

[] 

Before:[]

{border="0"} []

Figure 5: Combine Disabled

[] 

After:[]

[] 

{border="0"} []

Figure 6: Combine Enabled

The above images show the downloading time before and after the Combine process of the resource files. Before the Combine process, browser takes 257ms to download the css resources (Figure 1), where as after Combine it takes only 63ms to the download resources (Figure 2). 194ms time is reduced in the above Combine process sample.[]

[] 

Register

Two overloads are available for **Register**() method. Adding StyleManager to an application uses the one where the component name can be specified as String separated by a comma.[]

To add controls in a single line, use **Register()** method.[]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                       |
|                                                                                                                                                                                 |
| [      [\<%]{]                                                                                                  |
|                                                                                                                                                                                 |
| [          Html.Syncfusion().StyleManager()]                                                                                                |
|                                                                                                                                                                                 |
| [             .Register([\"Chart\"]) [//Specify the component names   separated by a comma.]] |
|                                                                                                                                                                                 |
| [              .Render();]                                                                                                                  |
|                                                                                                                                                                                 |
| [      } [%\>]]                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]** []                                                                                     |
|                                                                                                                                                                                |
| [    [\@{]]                                                                                                    |
|                                                                                                                                                                                |
| [        Html.Syncfusion().StyleManager()]                                                                                                 |
|                                                                                                                                                                                |
| [            .Register([\"Chart\"]) [//Specify the component names   separated by a comma.]] |
|                                                                                                                                                                                |
| [            .Render();]                                                                                                                   |
|                                                                                                                                                                                |
| [    [}]] [ ]                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

To avoid child control register, use **DisableChildRegister()** method as follows: []

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                       |
|                                                                                                                                                 |
| [    [\<%]{]                                                                    |
|                                                                                                                                                 |
| [          Html.Syncfusion().StyleManager()]                                                                |
|                                                                                                                                                 |
| [              .Register(stylesheets =\>]                                                                   |
|                                                                                                                                                 |
| [               {]                                                                                          |
|                                                                                                                                                 |
| [                   stylesheets.Add([ComponentType].Chart).DisableChildRegister();] |
|                                                                                                                                                 |
| [               ] [}).Render();]                                        |
|                                                                                                                                                 |
| [      } [%\>]]                                                                 |
|                                                                                                                                                 |
| **[]**                                                                                                      |
|                                                                                                                                                 |
| **[\[Razor\]]** []                                                      |
|                                                                                                                                                 |
| [    [\@{]]                                                                     |
|                                                                                                                                                 |
| [        Html.Syncfusion().StyleManager()]                                                                  |
|                                                                                                                                                 |
| [        ] [.Register(stylesheets =\>]                                  |
|                                                                                                                                                 |
| [            {]                                                                                             |
|                                                                                                                                                 |
| [                stylesheets.Add([ComponentType].Chart).DisableChildRegister();]    |
|                                                                                                                                                 |
| [            }).Render();]                                                                                  |
|                                                                                                                                                 |
| [    [}]]                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To enable or disable the sub component registrations based on some condition, use **AllowChildRegister()** method.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                                                |
|                                                                                                                                                                          |
| [    [\<%]{]                                                                                             |
|                                                                                                                                                                          |
| [          Html.Syncfusion().StyleManager()]                                                                                         |
|                                                                                                                                                                          |
| [              .Register(stylesheets =\>]                                                                                            |
|                                                                                                                                                                          |
| [               {]                                                                                                                   |
|                                                                                                                                                                          |
| [                   stylesheets.Add([ComponentType].Chart).AllowChildRegister([true]);] |
|                                                                                                                                                                          |
| [               ] [}).Render();]                                                                 |
|                                                                                                                                                                          |
| [      } [%\>]]                                                                                          |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| **[\[Razor\]]** []                                                                               |
|                                                                                                                                                                          |
| [    [\@{]]                                                                                              |
|                                                                                                                                                                          |
| [        Html.Syncfusion().StyleManager()]                                                                                           |
|                                                                                                                                                                          |
| [        ] [.Register(stylesheets =\>]                                                           |
|                                                                                                                                                                          |
| [            {]                                                                                                                      |
|                                                                                                                                                                          |
| [                stylesheets.Add([ComponentType].Chart).AllowChildRegister([true]);]    |
|                                                                                                                                                                          |
| [            }).Render();]                                                                                                           |
|                                                                                                                                                                          |
| [    [}]]                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Theme

To register the CSS Stylesheets for all controls, use Theme() method. DarkNight theme is the default theme.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                 |
|                                                                                                                                           |
| [    [\<%]{]                                                              |
|                                                                                                                                           |
| [          Html.Syncfusion().StyleManager()]                                                          |
|                                                                                                                                           |
| [              ]                                                                                      |
|                                                                                                                                           |
| [              .Theme([MobSkins].MetroBlue)]                                  |
|                                                                                                                                           |
| [              ]                                                                                      |
|                                                                                                                                           |
| [              .Register(stylesheets =\>]                                                             |
|                                                                                                                                           |
| [               {]                                                                                    |
|                                                                                                                                           |
| [                   stylesheets.Add([ComponentType].Chart);]                  |
|                                                                                                                                           |
| [               ] [}).Render();]                                  |
|                                                                                                                                           |
| [      } [%\>]]                                                           |
|                                                                                                                                           |
| []                                                                                |
|                                                                                                                                           |
| [ **\[Razor\]**]                                                                                      |
|                                                                                                                                           |
| [    [\@{]]                                                               |
|                                                                                                                                           |
| [        Html.Syncfusion().StyleManager()]                                                            |
|                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                           |
| [        ] [.Theme([MobSkins].MetroBlue)] |
|                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                           |
| [        .Register(stylesheets =\>]                                                                   |
|                                                                                                                                           |
| [            {]                                                                                       |
|                                                                                                                                           |
| [                stylesheets.Add([ComponentType].Chart);]                     |
|                                                                                                                                           |
| [            }).Render();]                                                                            |
|                                                                                                                                           |
| [    [}]]                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To configure individual theme for every controls use **Theme()** method inside Register().[]

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **\[ASPX\]**]                                                                                                                         |
|                                                                                                                                                                             |
| [    [\<%]{]                                                                                                |
|                                                                                                                                                                             |
| [          Html.Syncfusion().StyleManager()]                                                                                            |
|                                                                                                                                                                             |
| [              .Register(stylesheets =\>]                                                                                               |
|                                                                                                                                                                             |
| [               {]                                                                                                                      |
|                                                                                                                                                                             |
| [                   stylesheets.Add([ComponentType].Menu).Theme([MobSkins].MetroBlue);] |
|                                                                                                                                                                             |
| [               ] [}).Render();]                                                                    |
|                                                                                                                                                                             |
| [      } [%\>]]                                                                                             |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [  **\[Razor\]**]                                                                                                                       |
|                                                                                                                                                                             |
| [    [\@{]]                                                                                                 |
|                                                                                                                                                                             |
| [        Html.Syncfusion().StyleManager()]                                                                                              |
|                                                                                                                                                                             |
| [        ] [.Register(stylesheets =\>]                                                              |
|                                                                                                                                                                             |
| [            {]                                                                                                                         |
|                                                                                                                                                                             |
| [                stylesheets.Add([ComponentType].Menu).Theme([MobSkins].MetroBlue);]    |
|                                                                                                                                                                             |
| [            }).Render();]                                                                                                              |
|                                                                                                                                                                             |
| [    [}]]                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In this above code, DarkNight theme registers all the other components and MetroBlue theme registers for Menu control.[]

To avoid theme override by external Theme() method, use **DontOverride()** method. []

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                                       |
|                                                                                                                                                 |
| [  [\<%][=]Html.Syncfusion().StyleManager()\                                                   |
|       .Theme([Skins].Almond)[// Specify Theme to all components].      .Register(styleSheet =\> \ |
|           {\                                                                                                                                    |
|         styleSheet.Add([ComponentType].Chart)**.DontOverride();**\                                                      |
| \                                                                                                                                               |
|            })  [%\>]]                                                           |
|                                                                                                                                                 |
| []                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In general, the external Theme() method overrides all the internal component themes register. The DontOverride() method preserves the theme registered in the Register() methods.


{border="0"}Note: The Theme () method will register the CSS style sheets for the specified theme in the html head section. Using this method, we cannot apply themes for the controls (cannot add CSS classes). If we don't use StyleManager then the CSS style sheet for default theme or specified theme will be registered just before controls render starts. The StyleManager is introduced to improve the performance using its Minify and Combine feature.[]


Add CSS Files

To include the application CSS files to styleManager, use **Add()** method.[]

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]** []                                    |
|                                                                                                                              |
| [    [\<%]{]                                                 |
|                                                                                                                              |
| [          Html.Syncfusion().StyleManager()]                                             |
|                                                                                                                              |
| [              .Register(stylesheets =\>]                                                |
|                                                                                                                              |
| [               {]                                                                       |
|                                                                                                                              |
| [                   stylesheets.Add([ComponentType].Chart);]     |
|                                                                                                                              |
| [                   stylesheets.Add([\"\~/Content/site.css\"]);] |
|                                                                                                                              |
| [               }).Render();]                                                            |
|                                                                                                                              |
| [      } [%\>]]                                              |
|                                                                                                                              |
| []                                                                                       |
|                                                                                                                              |
| []                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]** []                                |
|                                                                                                                           |
| [    [\@{]]                                               |
|                                                                                                                           |
| [        Html.Syncfusion().StyleManager()]                                            |
|                                                                                                                           |
| [        .Register(stylesheets =\>]                                                   |
|                                                                                                                           |
| [            {]                                                                       |
|                                                                                                                           |
| [                stylesheets.Add([ComponentType].Chart);]     |
|                                                                                                                           |
| [                stylesheets.Add([\"\~/Content/site.css\"]);] |
|                                                                                                                           |
| [            }).Render();]                                                            |
|                                                                                                                           |
| [    [}]]                                                 |
|                                                                                                                           |
| []                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------+

 

[] 

[]{#related-topics}

