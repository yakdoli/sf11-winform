---
title: separatorsettings.md
original_path: WinForms_Docs/99_Uncategorized/separatorsettings.md
created_at: 2025-08-05
---






##### Separator Settings {#separator-settings style="tab-stops: 0pt"}

[] 

When separator lines have to be provided between the items, the **ItemClass** property can be used. When this is set to **Separator** value for an item with the **Text** value left empty, a line will be displayed.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------+
| Property                          | Description                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------+
| ItemClass                         | Gets/sets the item type. Default value is Common. The options included are as follows: |
|                                   |                                                                                        |
|                                   | [·      ]\                                                |
|                                   | Common                                                                                 |
|                                   |                                                                                        |
|                                   | [·      ]Separator                                        |
+-----------------------------------+----------------------------------------------------------------------------------------+


[] 

{border="0"}

**[]** 

Figure 226: Menu with ItemClass property set

[] 

Customizing Separator

[] 

The default separator styles can be overridden by using the css style definitions for the separator by applying it through **SeparatorCSSClass** property.

[] 


+-----------------------------------+-----------------------------------------------------------------------+
|                                   |                                                                       |
|                                   |                                                                       |
| Menu Property                     | Description                                                           |
+-----------------------------------+-----------------------------------------------------------------------+
|                                   |                                                                       |
|                                   |                                                                       |
| SeparatorCSSClass                 | Specifies the class name of the css definitions to use for separator. |
+-----------------------------------+-----------------------------------------------------------------------+


[] 

{border="0"}

 

Figure 227: Menu with custom Separator settings

[] 

The separator can be customized by specifying the colors and types by overriding the default settings as shown below. Also the separator can be applied to the entire row else can be set such that it does not apply to the left image segment as shown in the above image. Here the default css style names are used with custom style definitions overriding the default values.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [.menuSep][ [.menuSepImg]]            |
|                                                                                                                                                                                     |
| [{]                                                                                                                             |
|                                                                                                                                                                                     |
| [       [line-height]: [0px];]                                                         |
|                                                                                                                                                                                     |
| [       [font-size]:[0px];       ]                                                     |
|                                                                                                                                                                                     |
| [       [border-top]:[1px] [solid] [black];] |
|                                                                                                                                                                                     |
| [       [border-style]:[outset];]                                                      |
|                                                                                                                                                                                     |
| [}]                                                                                                                             |
|                                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                                     |
| [.menuImg]                                                                                                       |
|                                                                                                                                                                                     |
| [{]                                                                                                                             |
|                                                                                                                                                                                     |
| [       [height]:[16px];]                                                              |
|                                                                                                                                                                                     |
| [       [width]:[16px];]                                                               |
|                                                                                                                                                                                     |
| [}]                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

