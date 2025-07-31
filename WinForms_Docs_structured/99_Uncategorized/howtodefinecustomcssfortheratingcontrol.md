---
title: howtodefinecustomcssfortheratingcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodefinecustomcssfortheratingcontrol.md
created_at: 2025-07-03
---






##### How to define Custom CSS for the Rating control? {#how-to-define-custom-css-for-the-rating-control style="tab-stops: 0pt"}

[[[]]]{.underline} 

The rating control supports custom CSS so that images for ratings (size, shape, and so on) can be customized to suit your application.

 This is the property for Custom skins for Rating control-

Properties

  ------------------- ------------------------------------------------------ ------------------ ------------------- ------------
  Name                Description                                            Type of property   Value it accepts    Dependency
  CustomCSS           Sets the class attribute of the control.               string             Any string          NA
  CustomImageHeight   Gets the height of the custom rating icon in pixels.   int                1 to int.MaxValue   NA
  CustomImageWidth    Gets the height of the custom rating icon in pixels.   int                1 to int.MaxValue   NA
  ------------------- ------------------------------------------------------ ------------------ ------------------- ------------

 

Using ASPX code-

Build and run the application using the following ASPX code:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][syncfusion][:][Rating][ [ID][=\"Rating1\"] [runat][=\"server\"] [CustomCss][=\"MyRatingStyle\"]][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [CustomImageHeight][=\"28\"][ [CustomImageWidth][=\"28\"] [/\>]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

**Using C# or VB code-**

Build and run the application using either one of the following code snippets:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                |
|                                                                                                                                                                                             |
| [       [Rating] rating = [new] [Rating]();][] |
|                                                                                                                                                                                             |
| [    rating.CustomCss = [\"][ MyRatingStyle][ \"];]                              |
|                                                                                                                                                                                             |
| [    rating.CustomImageHeight = 28;]                                                                                                                    |
|                                                                                                                                                                                             |
| [    rating.CustomImageWidth = 28;]                                                                                                                     |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                                                                                                  |
|                                                                                                                                                                                                               |
| [        [Dim] rating [As] [New] [Rating]()][] |
|                                                                                                                                                                                                               |
| [    rating.CustomCss = [\"][ MyRatingStyle][ \"]]                                                 |
|                                                                                                                                                                                                               |
| [    rating.CustomImageHeight = 28]                                                                                                                                       |
|                                                                                                                                                                                                               |
| [    rating.CustomImageWidth = 28]                                                                                                                                        |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[[]]]{.underline} 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ \[Css\]]                                                                                                                                                     |
|                                                                                                                                                                                                    |
| [.MyRatingStyle][]                                                                                          |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [display]: [block];]                                                                                     |
|                                                                                                                                                                                                    |
| [            [position]: [relative];]                                                                                 |
|                                                                                                                                                                                                    |
| [            [margin-top]: [-7px];]                                                                                   |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle.horizontal] [.star-container]]                                                          |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [list-style-type]: [none];]                                                                              |
|                                                                                                                                                                                                    |
| [            [padding]: [0] [2px]; [display]:[inline];] |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle.vertical] [.star-container]]                                                            |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [list-style-type]: [none];]                                                                              |
|                                                                                                                                                                                                    |
| [            [margin]: [0] [0] [0] [-2px];]            |
|                                                                                                                                                                                                    |
| [            [padding]: [0] [2px];]                                                              |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle.horizontal] [.star-list]]                                                               |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [list-style-type]: [none];]                                                                              |
|                                                                                                                                                                                                    |
| [            [float]: [left];]                                                                                        |
|                                                                                                                                                                                                    |
| [            [width]: [28px];]                                                                                        |
|                                                                                                                                                                                                    |
| [            [height]: [28px];]                                                                                       |
|                                                                                                                                                                                                    |
| [            [background]: [url(\"../Images/crystal-stars.png\")no-repeat];]                                          |
|                                                                                                                                                                                                    |
| [            [background-position]: [0] [-56px];]                                                |
|                                                                                                                                                                                                    |
| [            [cursor]:[pointer];]                                                                                     |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle.vertical] [.star-list]]                                                                 |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [list-style-type]: [none];]                                                                              |
|                                                                                                                                                                                                    |
| [            [width]: [28px];]                                                                                        |
|                                                                                                                                                                                                    |
| [            [height]: [28px];]                                                                                       |
|                                                                                                                                                                                                    |
| [            [background]: [url(\"../Images/crystal-stars.png\")no-repeat];]                                          |
|                                                                                                                                                                                                    |
| [            [background-position]: [0] [-56px];]                                                |
|                                                                                                                                                                                                    |
| [            [cursor]:[pointer];]                                                                                     |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle.horizontal] [.stars]]                                                                   |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [background]: [url(\"../Images/crystal-stars.png\")no-repeat];]                                          |
|                                                                                                                                                                                                    |
| [            [float]: [left];]                                                                                        |
|                                                                                                                                                                                                    |
| [            [height]: [28px];]                                                                                       |
|                                                                                                                                                                                                    |
| [            [width]: [28px];]                                                                                        |
|                                                                                                                                                                                                    |
| [            [cursor]: [pointer];]                                                                                    |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle.vertical] [.stars]]                                                                     |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [background]: [url(../Images/crystal-stars.png)] [no-repeat];]                      |
|                                                                                                                                                                                                    |
| [            [height]: [28px];]                                                                                       |
|                                                                                                                                                                                                    |
| [            [width]: [28px];]                                                                                        |
|                                                                                                                                                                                                    |
| [            [cursor]: [pointer];]                                                                                    |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle.horizontal] [.reset]]                                                                   |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [background]: [url(\"../Images/crystal-stars.png\")no-repeat];]                                          |
|                                                                                                                                                                                                    |
| [            [float]: [left];]                                                                                        |
|                                                                                                                                                                                                    |
| [            [height]: [28px];]                                                                                       |
|                                                                                                                                                                                                    |
| [            [width]: [28px];]                                                                                        |
|                                                                                                                                                                                                    |
| [            [margin-right]: [2px];]                                                                                  |
|                                                                                                                                                                                                    |
| [            [cursor]: [pointer];]                                                                                    |
|                                                                                                                                                                                                    |
| [            [background-position]: [0px] [0px];]                                                |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle.vertical] [.reset]]                                                                     |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [background]: [url(\"../Images/crystal-stars.png\")no-repeat];]                                          |
|                                                                                                                                                                                                    |
| [            [height]: [28px];]                                                                                       |
|                                                                                                                                                                                                    |
| [            [width]: [28px];]                                                                                        |
|                                                                                                                                                                                                    |
| [            [margin-bottom]: [2px];]                                                                                 |
|                                                                                                                                                                                                    |
| [            [cursor]: [pointer];]                                                                                    |
|                                                                                                                                                                                                    |
| [            [background-position]: [0px] [0px];]                                                |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle] [.reset:hover]]                                                                        |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [background-position]: [0] [-28px];]                                                |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle] [.stars.inactive]]                                                                     |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [background-position]: [0] [-56px];]                                                |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle] [.stars.active]]                                                                       |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [background-position]: [0] [-112px];]                                               |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle] [.stars.selected]]                                                                     |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [background-position]: [0] [-84px];]                                                |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [        [.MyRatingStyle] [.stars.precision]]                                                                    |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| [            [background-position]: [0] [-84px];]                                                |
|                                                                                                                                                                                                    |
| [            [width]: [0px];]                                                                                         |
|                                                                                                                                                                                                    |
| [            [margin-left]: [-28px];]                                                                                 |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                                    |
|                                                                                                                                                                                                    |
| []                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following figure shows the crystal-stars.png sprite image used in the code sample.

{border="0"}[]

**[Figure ][449][: Sprite Image]**

                  

Individual images can be made into sprites by using [[SpriteGen]](http://spritegen.website-performance.org/)---an automated process for generating CSS sprites.

The figure shows the how the sprite images appear in the rating control.

{border="0"}[]

**[Figure ][450][: Rating Control with Custom CSS Sprite Image]**

 

[]{#related-topics}

