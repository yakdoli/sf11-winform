---
title: blendabilitysupport4.md
original_path: WinForms_Docs/99_Uncategorized/blendabilitysupport4.md
created_at: 2025-08-05
---






#### Blendability support {#blendability-support style="tab-stops: 0pt"}

The template of the Carousel control can be easily editable in Expression Blend, to give a nice look and feel.

[] 

Using Blendability Support in an Application

Following are the steps to edit the template in Expression Blend.

1.   Open the Carousel control in blend.

2.   Go to Object -\>Edit Style -\> Edit a Copy to edit the template of Carousel control as shown below.

[] 

{border="0"}

Figure 114: Blend---Edit Template

 

A window will open as shown below where you can create a new style for the Carousel control and can define exactly where you would like to store it.

[] 

{border="0"}

Figure 115: Blend---Create Style

 

What's produced through this set of steps is quite a bit of XAML which is placed within your application. This XAML represents the default style for the Carousel control. In the same way, you can edit the template of CarouselItem.

 

{border="0"}

Figure 116: Carousel---Template Parts

 

Now you can edit each part in the template and can create custom look and feel for the control. In the below sample, template for CarouselItem is edited to give a reflection effect.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [           ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [        ][\<][Style][ TargetType][=\"syncfusion:CarouselItem\"\>][\                                                                                                                                                                                                    |
| [            ][\<][Setter][ Property][=\"Template\"\>]\                                                                                                                                                                                                                                                                                                                                                             |
| [                ][\<][Setter.Value][\>]\                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\<][ControlTemplate][ TargetType][=\"syncfusion:CarouselItem\"\>]\                                                                                                                                                                                                                                                                                                                           |
| [                        ][\<][Grid][\>]\                                                                                                                                                                                                                                                                                                                                                                                               |
| [                            ][\<][Grid.RowDefinitions][\>]\                                                                                                                                                                                                                                                                                                                                                                            |
| [                                ][\<][RowDefinition][/\>]\                                                                                                                                                                                                                                                                                                                                                                             |
| [                                ][\<][RowDefinition][/\>]\                                                                                                                                                                                                                                                                                                                                                                             |
| [                            ][\</][Grid.RowDefinitions][\>]\                                                                                                                                                                                                                                                                                                                                                                           |
| [                            ][\<][Border][ x][:][Name][=\"border\"][ BorderBrush][=\"#FF333333\"][ RenderTransformOrigin][=\"0.5,0.5\"][ CornerRadius][=\"4\"][ Padding][=\"4\"\>]\                   |
|  \                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                                ][\<][ContentPresenter][ Content][=\"{][TemplateBinding][ Content][}\"] \                                                                                                                                                                                                                                         |
|                                               [        ContentTemplate][=\"{][TemplateBinding][ ContentTemplate][}\" /\>]\                                                                                                                                                                                                                                                                                              |
| [                            ][\</][Border][\>]\                                                                                                                                                                                                                                                                                                                                                                                        |
|  \                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                            ][\<][Border][ BorderThickness][=\"2\"][ Grid.Row][=\"1\"][ Height][=\"100\"][ VerticalAlignment][=\"Top\"][ HorizontalAlignment][=\"Stretch\"][ CornerRadius][=\"5\"\>]\ |
| [                                ][\<][Border.BorderBrush][\>]\                                                                                                                                                                                                                                                                                                                                                                         |
| [                                    ][\<][LinearGradientBrush][ EndPoint][=\"0.5,1\"][ StartPoint][=\"0.5,0\"\>]\                                                                                                                                                                                                                                                         |
| [                                        ][\<][GradientStop][ Color][=\"#FFDADADA\"][ Offset][=\"0\"/\>]\                                                                                                                                                                                                                                                                  |
| [                                        ][\<][GradientStop][ Color][=\"Transparent\"][ Offset][=\"0.712\"/\>]\                                                                                                                                                                                                                                                            |
| [                                    ][\</][LinearGradientBrush][\>]\                                                                                                                                                                                                                                                                                                                                                                   |
| [                                ][\</][Border.BorderBrush][\>]\                                                                                                                                                                                                                                                                                                                                                                        |
| [                                ][\<][Border.Background][\>]\                                                                                                                                                                                                                                                                                                                                                                          |
| [                                    ][\<][LinearGradientBrush][ EndPoint][=\"0.5,1\"][ StartPoint][=\"0.5,0\"\>]\                                                                                                                                                                                                                                                         |
| [                                        ][\<][GradientStop][ Color][=\"#FFDADADA\"/\>]\                                                                                                                                                                                                                                                                                                                            |
| [                                        ][\<][GradientStop][ Color][=\"Transparent\"][ Offset][=\"0.705\"/\>]\                                                                                                                                                                                                                                                            |
| [                                    ][\</][LinearGradientBrush][\>]\                                                                                                                                                                                                                                                                                                                                                                   |
| [                                ][\</][Border.Background][\>]\                                                                                                                                                                                                                                                                                                                                                                         |
|  \                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                            ][\</][Border][\>]\                                                                                                                                                                                                                                                                                                                                                                                        |
| [                        ][\</][Grid][\>]\                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    ][\</][ControlTemplate][\>]\                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\</][Setter.Value][\>]\                                                                                                                                                                                                                                                                                                                                                                                              |
| [            ][\</][Setter][\>]\                                                                                                                                                                                                                                                                                                                                                                                                        |
| [        ][\</][Style][\>]]                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

*Figure* *117: Carousel*

[]{#related-topics}

