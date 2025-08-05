---
title: clientsidemethods25.md
original_path: WinForms_Docs/99_Uncategorized/clientsidemethods25.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Client Side Methods {#client-side-methods style="tab-stops: 0pt"}

The menu control supports a rich set of client side methods to control its behavior.

Methods

  --------- ------------ ------------- ---------------------------------
  Name      Parameters   Return type   Description
  disable   \-           \-            Disables all the menu items.
  enable    \-           \-            Enables all the menu items.
  show      \-           \-            Show the menu from hidden state
  hide      \-           \-            Hide the menu
  --------- ------------ ------------- ---------------------------------

 

The following steps guide you in using client side methods for the menu control:

1.   In **View**, invoke the menu helper with menu ID as the first argument.

**[]**  

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| [   [\<%][=]Html.MobSyncfusion().Menu([\"MethodsMenu\"])]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [                   .Items(items =\>]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                    |
| [                   {]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                    |
| [                       items.Add().Text([\"FaceBook\"]).ImageUrl([\"\~/Content/Menu/Images/Facebook.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] })] |
|                                                                                                                                                                                                                                                                                                    |
| [                           .Children(child =\>]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [                           {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| [                               child.Add().Text([\"Home Page\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [                               child.Add().Text([\"Log on\"]);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                    |
| [                           });]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [                       items.Add().Text([\"Twitter\"]).ImageUrl([\"\~/Content/Menu/Images/twitter.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] })]   |
|                                                                                                                                                                                                                                                                                                    |
| [                           .Children(child =\>]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [                           {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| [                               child.Add().Text([\"Home Page\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [                           });]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [                       items.Add().Text([\"Google\"]).ImageUrl([\"\~/Content/Menu/Images/Google.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] })]     |
|                                                                                                                                                                                                                                                                                                    |
| [                           .Children(child =\>]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [                           {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| [                               child.Add().Text([\"Home Page\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [                               child.Add().Text([\"Gmail\"]);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                    |
| [                               child.Add().Text([\"Orkut\"]);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                    |
| [                               child.Add().Text([\"Maps\"]);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                    |
| [                               child.Add().Text([\"News\"]);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                    |
| [                           });]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [                       items.Add().Text([\"YouTube\"]).ImageUrl([\"\~/Content/Menu/Images/youtube.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] });]  |
|                                                                                                                                                                                                                                                                                                    |
| [                       items.Add().Text([\"Books\"]).ImageUrl([\"\~/Content/Menu/Images/book.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] });]       |
|                                                                                                                                                                                                                                                                                                    |
| [                       items.Add().Text([\"Games\"]).ImageUrl([\"\~/Content/Menu/Images/game.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] });]       |
|                                                                                                                                                                                                                                                                                                    |
| [                   })[%\>]]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                             |
| [   [\@{]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                             |
| [        Html.MobSyncfusion().Menu([\"MethodsMenu\"])]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                             |
| [            .Items(items =\>]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                             |
| [                items.Add().Text([\"FaceBook\"]).ImageUrl([\"\~/Content/Menu/Images/Facebook.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] })] |
|                                                                                                                                                                                                                                                                                             |
| [                    .Children(child =\>]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                             |
| [                    {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                             |
| [                        child.Add().Text([\"Home Page\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                             |
| [                        child.Add().Text([\"Log on\"]);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                             |
| [                    });]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                             |
| [                items.Add().Text([\"Twitter\"]).ImageUrl([\"\~/Content/Menu/Images/twitter.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] })]   |
|                                                                                                                                                                                                                                                                                             |
| [                    .Children(child =\>]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                             |
| [                    {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                             |
| [                        child.Add().Text([\"Home Page\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                             |
| [                    });]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                             |
| [                items.Add().Text([\"Google\"]).ImageUrl([\"\~/Content/Menu/Images/Google.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] })]     |
|                                                                                                                                                                                                                                                                                             |
| [                    .Children(child =\>]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                             |
| [                    {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                             |
| [                        child.Add().Text([\"Home Page\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                             |
| [                        child.Add().Text([\"Gmail\"]);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                             |
| [                        child.Add().Text([\"Orkut\"]);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                             |
| [                        child.Add().Text([\"Maps\"]);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                             |
| [                        child.Add().Text([\"News\"]);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                             |
| [                    });]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                             |
| [                items.Add().Text([\"YouTube\"]).ImageUrl([\"\~/Content/Menu/Images/youtube.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] });]  |
|                                                                                                                                                                                                                                                                                             |
| [                items.Add().Text([\"Books\"]).ImageUrl([\"\~/Content/Menu/Images/book.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] });]       |
|                                                                                                                                                                                                                                                                                             |
| [                items.Add().Text([\"Games\"]).ImageUrl([\"\~/Content/Menu/Images/game.png\"]).ImageAttributes([new] { \@class = [\"menu-img\"] });]       |
|                                                                                                                                                                                                                                                                                             |
| [            })]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                             |
| [                .Render();]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                             |
| [    [}]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In Javascript, use the methods to enable and disable an item as follows.

**[]**  

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                                                                  |
|                                                                                                                                                                           |
| [    [\<][script][type][=\"text/javascript\"\>]] |
|                                                                                                                                                                           |
| [        [function] disableMenu() {]                                                                             |
|                                                                                                                                                                           |
| [            [//Code to disable the menu ]]                                                                 |
|                                                                                                                                                                           |
| [            \$([\"#MethodsMenu\"]).sfMenu([\"disable\"]);]                             |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| [        [function] enableMenu() {]                                                                              |
|                                                                                                                                                                           |
| [            [//Code to enable the menu ]]                                                                  |
|                                                                                                                                                                           |
| [            \$([\"#MethodsMenu\"]).sfMenu([\"enable\"]);]                              |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| [        [function] hideMenu() {]                                                                                |
|                                                                                                                                                                           |
| [            [//Code to hide the menu ]]                                                                    |
|                                                                                                                                                                           |
| [            \$([\"#MethodsMenu\"]).sfMenu([\"hide\"]);]                                |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| [        [function] showMenu() {]                                                                                |
|                                                                                                                                                                           |
| [            [//Code to show the menu ]]                                                                    |
|                                                                                                                                                                           |
| [            \$([\"#MethodsMenu\"]).sfMenu([\"show\"]);]                                |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| [    [\</][script][\>]]                                              |
|                                                                                                                                                                           |
| []                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

The output when the menu is disabled is shown in the following screenshots.

{border="0"}

Figure 82: Menu with disabled state

 

[]{#related-topics}

