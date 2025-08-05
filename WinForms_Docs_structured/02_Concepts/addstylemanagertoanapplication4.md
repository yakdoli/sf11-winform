---
title: addstylemanagertoanapplication4.md
original_path: WinForms_Docs/02_Concepts/addstylemanagertoanapplication4.md
created_at: 2025-08-05
---






#### Add StyleManager to an Application {#add-stylemanager-to-an-application style="tab-stops: 0pt"}

 

Add the **StyleManager** extension method in the HEAD tag of the **view** pages (in most cases, It is reasonable to call it within the **Site.Master** page).

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [\<][head][ [runat][=\"server\"\>]]               |
|                                                                                                                                                                                                                                    |
| [\<%][=][ Html.MobSyncfusion().StyleManager()] |
|                                                                                                                                                                                                                                    |
| [          .Register(stylesheets =\>]                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [                  {]                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [                      stylesheets.Add([MobComponentType].Tab);]                                                                                          |
|                                                                                                                                                                                                                                    |
| [                  })]                                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [    [%\>]]                                                                                                                                           |
|                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [...]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| [\</][head][\>]                                                               |
|                                                                                                                                                                                                                                    |
| **[\[Razor\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [\<][head][ [runat][=\"server\"\>]]               |
|                                                                                                                                                                                                                                    |
| [@(][Html.MobSyncfusion().StyleManager()]                                                                    |
|                                                                                                                                                                                                                                    |
| [    .Register(stylesheets =\>]                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [                stylesheets.Add([MobComponentType].Tab);]                                                                                                |
|                                                                                                                                                                                                                                    |
| [            })[)]]                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [ ...]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [\</][head][\>][]                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Use the **Register()** method to register the Syncfusion component CSS resources.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **\[ASPX\]**]                                                                                                                           |
|                                                                                                                                                                               |
| [\<%][{]                                                                          |
|                                                                                                                                                                               |
| [          Html.MobSyncfusion().StyleManager()]                                                                                           |
|                                                                                                                                                                               |
| [              .Register(stylesheets =\>]                                                                                                 |
|                                                                                                                                                                               |
| [               {]                                                                                                                        |
|                                                                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].ListBox);]                                                 |
|                                                                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].Menu);]                                                    |
|                                                                                                                                                                               |
| [                     stylesheets.Add([MobComponentType].ToolBar);]                                  |
|                                                                                                                                                                               |
| [               }).Render();]                                                                                                             |
|                                                                                                                                                                               |
| [ } [%\>]]                                                                                                    |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
| [ **\[Razor\]**]                                                                                                                          |
|                                                                                                                                                                               |
| [    [\@{]]                                                                                                   |
|                                                                                                                                                                               |
| [        Html.MobSyncfusion().StyleManager()]                                                                                             |
|                                                                                                                                                                               |
| [        .Register(stylesheets =\>]                                                                                                       |
|                                                                                                                                                                               |
| [            {]                                                                                                                           |
|                                                                                                                                                                               |
| [                stylesheets.Add([MobComponentType].ListBox);]                                                    |
|                                                                                                                                                                               |
| [                stylesheets.Add([MobComponentType].Menu);]                                                       |
|                                                                                                                                                                               |
| [                ][stylesheets.Add([MobComponentType].ToolBar);] |
|                                                                                                                                                                               |
| [            }).Render();]                                                                                                                |
|                                                                                                                                                                               |
| [    [}]]                                                                                                     |
|                                                                                                                                                                               |
| []                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The above code registers the default DarkNight theme for added components. All the CSS resources are combined and minified before being sent to the browser.

Customization

Various customization options have been provided. They are:

[•   ][Minify]

[•   ][Combine]

[•   ][Register]

[•   ][Theme]

[•   ][Add CSS Files]

**[Minify]**

 To enable or disable the Minify feature, use the **Minify()** method. Minify is enabled by default. 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                            |
|                                                                                                                               |
| [    [\<%]{]                                                  |
|                                                                                                                               |
| [          Html.MobSyncfusion().StyleManager()]                                           |
|                                                                                                                               |
| [              ]                                                                          |
|                                                                                                                               |
| [              .Minify([false]) ]                                    |
|                                                                                                                               |
| [              ]                                                                          |
|                                                                                                                               |
| [              .Register(stylesheets =\>]                                                 |
|                                                                                                                               |
| [               {]                                                                        |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].Menu);]    |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].ListBox);] |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].ToolBar);] |
|                                                                                                                               |
| [                }).Render();]                                                            |
|                                                                                                                               |
| [      } [%\>]]                                               |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [ **\[Razor\]**]                                                                          |
|                                                                                                                               |
| [    [\@{]]                                                   |
|                                                                                                                               |
| [        Html.MobSyncfusion().StyleManager()]                                             |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [        .Minify([false])]                                           |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [        .Register(stylesheets =\>      ]                                                 |
|                                                                                                                               |
| [            {]                                                                           |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].Menu);]       |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].ListBox);]    |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].ToolBar);]    |
|                                                                                                                               |
| [            }).Render();]                                                                |
|                                                                                                                               |
| [    [}]][]                          |
+-------------------------------------------------------------------------------------------------------------------------------+

 

Please refer HTTP requests and the time details from the below images.

**Before**

{border="0"}

[]{#_Ref316896978}[Figure]{#_Ref316896987} 4: Minify Disabled

 

**After**

{border="0"} 

[Figure]{#_Ref316897012} 5: Minify Enabled

The above images show the size of the resource files before and after the minfication process. Before the minification process a 3.6KB file is downloaded in the browser ([Figure 4](#_Ref316896987)), whereas after minification, a 3KB file is downloaded in the browser ([Figure 5](#_Ref316897012)). 0.6KB size reduced in the above minification process sample.

 

**[Combine ]**

To enable or disable the combine file feature, use the **Combine()** method. This method is enabled by default.

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                            |
|                                                                                                                               |
| [    [\<%]{]                                                  |
|                                                                                                                               |
| [          Html.MobSyncfusion().StyleManager()]                                           |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [              .Combine([false])]                                    |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [              .Register(stylesheets =\>]                                                 |
|                                                                                                                               |
| [               {]                                                                        |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].Menu);]    |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].ListBox);] |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].ToolBar);] |
|                                                                                                                               |
| [               }).Render();]                                                             |
|                                                                                                                               |
| [      } [%\>]]                                               |
|                                                                                                                               |
| [ **\[Razor\]**]                                                                          |
|                                                                                                                               |
| [    [\@{]]                                                   |
|                                                                                                                               |
| [        Html.MobSyncfusion().StyleManager()]                                             |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [        .Combine([false])]                                          |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [        .Register(stylesheets =\>]                                                       |
|                                                                                                                               |
| [            {]                                                                           |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].Menu);]       |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].ListBox);]    |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].ToolBar);]    |
|                                                                                                                               |
| [            }).Render();]                                                                |
|                                                                                                                               |
| [    [}]][]                          |
+-------------------------------------------------------------------------------------------------------------------------------+

 

Please refer HTTP requests and the time details from the below images:

 

**Before**

 

{border="0"}

[Figure]{#_Ref316897173} 6: Combine Disabled

 

**After**

 

{border="0"}

[Figure]{#_Ref316897182} 7: Combine Enabled

The above images show the downloading time before and after the combine process of the resource files. Before the combine process, the browser takes 109ms to download the CSS resources ([Figure 6](#_Ref316897173)), whereas after the combine process it takes only 32ms to download the resources ([Figure 7](#_Ref316897182)). 77ms time is reduced in the above combine process sample.

 

Register

Two overloads are available for the **Register()** method. Adding StyleManager to an application uses the one where the component name can be specified as strings separated by a comma.

To add controls in a single line, use the **Register()** method.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                         |
|                                                                                                                                                                                            |
| [      [\<%]{]                                                                                                             |
|                                                                                                                                                                                            |
| [          Html.MobSyncfusion().StyleManager()]                                                                                                        |
|                                                                                                                                                                                            |
| [             .Register([\"Menu,Tab,Toolbar\"]) [//Specify the component names   separated by a comma.]] |
|                                                                                                                                                                                            |
| [              .Render();]                                                                                                                             |
|                                                                                                                                                                                            |
| [      } [%\>]]                                                                                                            |
|                                                                                                                                                                                            |
|                                                                                                                                                                                            |
|                                                                                                                                                                                            |
| **[\[Razor\]]**                                                                                                                                        |
|                                                                                                                                                                                            |
| [    [\@{]]                                                                                                                |
|                                                                                                                                                                                            |
| [        Html.MobSyncfusion().StyleManager()]                                                                                                          |
|                                                                                                                                                                                            |
| [            .Register([\"Menu,Tab,Toolbar\"]) [//Specify the component names   separated by a comma.]]  |
|                                                                                                                                                                                            |
| [            .Render();]                                                                                                                               |
|                                                                                                                                                                                            |
| [    [}] ][]                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Theme

To register the CSS StyleSheets for all controls, use the **Theme()** method.\
The DarkNight theme is the default theme for Essential Tools in Mobile MVC.

 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                            |
|                                                                                                                               |
| [    [\<%]{]                                                  |
|                                                                                                                               |
| [          Html.MobSyncfusion().StyleManager()]                                           |
|                                                                                                                               |
| [              ]                                                                          |
|                                                                                                                               |
| [              .Theme([MobSkins].MetroBlue)]                      |
|                                                                                                                               |
| [              ]                                                                          |
|                                                                                                                               |
| [              .Register(stylesheets =\>]                                                 |
|                                                                                                                               |
| [               {]                                                                        |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].Menu);]    |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].Tab);]     |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].ToolBar);] |
|                                                                                                                               |
| [               }).Render();]                                                             |
|                                                                                                                               |
| [      } [%\>]]                                               |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [ **\[Razor\]**]                                                                          |
|                                                                                                                               |
| [    [\@{]]                                                   |
|                                                                                                                               |
| [        Html.MobSyncfusion().StyleManager()]                                             |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [        .Theme([MobSkins].MetroBlue)]                            |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [        .Register(stylesheets =\>]                                                       |
|                                                                                                                               |
| [            {]                                                                           |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].Menu);]       |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].Tab);]        |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].ToolBar);]    |
|                                                                                                                               |
| [            }).Render();]                                                                |
|                                                                                                                               |
| [    [}]][]                          |
+-------------------------------------------------------------------------------------------------------------------------------+

 

To configure an individual theme for every control, use the **Theme()** method inside **Register()**.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ **\[ASPX\]**]                                                                                                                            |
|                                                                                                                                                                                |
| [    [\<%]{]                                                                                                   |
|                                                                                                                                                                                |
| [          Html.MobSyncfusion().StyleManager()]                                                                                            |
|                                                                                                                                                                                |
| [              .Register(stylesheets =\>]                                                                                                  |
|                                                                                                                                                                                |
| [               {]                                                                                                                         |
|                                                                                                                                                                                |
| [                   stylesheets.Add([MobComponentType].Menu).Theme([MobSkins].MetroBlue);] |
|                                                                                                                                                                                |
| [                   stylesheets.Add([MobComponentType].Tab);]                                                      |
|                                                                                                                                                                                |
| [                   stylesheets.Add([MobComponentType].ToolBar);]                                                  |
|                                                                                                                                                                                |
| [               }).Render();]                                                                                                              |
|                                                                                                                                                                                |
| [      } [%\>]]                                                                                                |
|                                                                                                                                                                                |
|                                                                                                                                                                                |
|                                                                                                                                                                                |
| [  **\[Razor\]**]                                                                                                                          |
|                                                                                                                                                                                |
| [    [\@{]]                                                                                                    |
|                                                                                                                                                                                |
| [        Html.MobSyncfusion().StyleManager()]                                                                                              |
|                                                                                                                                                                                |
| [        .Register(stylesheets =\>]                                                                                                        |
|                                                                                                                                                                                |
| [            {]                                                                                                                            |
|                                                                                                                                                                                |
| [                stylesheets.Add([MobComponentType].Menu).Theme([MobSkins].MetroBlue);]    |
|                                                                                                                                                                                |
| [                stylesheets.Add([MobComponentType].Tab);]                                                         |
|                                                                                                                                                                                |
| [                stylesheets.Add([MobComponentType].ToolBar);]                                                     |
|                                                                                                                                                                                |
| [            }).Render();]                                                                                                                 |
|                                                                                                                                                                                |
| [    [}]][]                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

In the code above, the MetroBlue theme registers for the Menu control and the DarkNight theme is registered for all the other components.

To avoid theme override by the external **Theme()** method, use the **DontOverride()** method.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                              |
|                                                                                                                                                                 |
| [  [\<%][=]Html.Syncfusion().StyleManager()\                                                                   |
|       .Theme([MobSkins].DarkNight)[//Specify Theme to all components].      ] |
|                                                                                                                                                                 |
| [.Register(styleSheet =\> \                                                                                                                                     |
|           {\                                                                                                                                                    |
|       styleSheet.Add([MobComponentType].ListBox).Theme([MobSkins].DarkNight) **).DontOverride()**;\             |
|         styleSheet.Add([MobComponentType].Menu);\                                                                                       |
|         styleSheet.Add([MobComponentType].Toolbar);\                                                                                    |
|            })  [%\>]]                                                                           |
|                                                                                                                                                                 |
| []                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

In general, the external **Theme()** method overrides all the internal component themes registered. The **DontOverride()** method preserves the theme registered in the **Register()** methods.

{border="0"}[Note: The **Theme()** method will register the CSS for the specified theme in the HTML HEAD section. Using this method, we cannot apply themes for the controls (cannot add CSS classes). If we don't use StyleManager then the CSS for default themes or specified themes will be registered just before controls rendering starts. The StyleManager is introduced to improve the performance using its minify and combine features.]

Add CSS Files

To include the application CSS files in StyleManager, use the **Add()** method.

 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                            |
|                                                                                                                               |
| [    [\<%]{]                                                  |
|                                                                                                                               |
| [          Html.MobSyncfusion().StyleManager()]                                           |
|                                                                                                                               |
| [              .Register(stylesheets =\>]                                                 |
|                                                                                                                               |
| [               {]                                                                        |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].Menu);]    |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].Tab);]     |
|                                                                                                                               |
| [                   stylesheets.Add([MobComponentType].ToolBar);] |
|                                                                                                                               |
| [                   stylesheets.Add([\"\~/Content/site.css\"]);]  |
|                                                                                                                               |
| [               }).Render();]                                                             |
|                                                                                                                               |
| [      } [%\>]]                                               |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| **[\[Razor\]]**                                                                           |
|                                                                                                                               |
| [    [\@{]]                                                   |
|                                                                                                                               |
| [        Html.MobSyncfusion().StyleManager()]                                             |
|                                                                                                                               |
| [        .Register(stylesheets =\>]                                                       |
|                                                                                                                               |
| [            {]                                                                           |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].Menu);]       |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].Tab);]        |
|                                                                                                                               |
| [                stylesheets.Add([MobComponentType].ToolBar);]    |
|                                                                                                                               |
| [                stylesheets.Add([\"\~/Content/site.css\"]);]     |
|                                                                                                                               |
| [            }).Render();]                                                                |
|                                                                                                                               |
| [    [}]]                                                     |
|                                                                                                                               |
| []                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

