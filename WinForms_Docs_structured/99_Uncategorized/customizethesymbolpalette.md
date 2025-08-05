---
title: customizethesymbolpalette.md
original_path: WinForms_Docs/99_Uncategorized/customizethesymbolpalette.md
created_at: 2025-08-05
---








  









### Customize the SymbolPalette {#customize-the-symbolpalette style="tab-stops: 0pt"}

The appearance of the SymbolPalette can be customized to suit any application. Several properties have been provided in the **SymbolPalette** class to enable its customization.

 

The following properties can be used to customize the SymbolPalette in your application.\
\

Table 83: Property Table


+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| Property                          | Description                                                                                         | Type of the property | Value it accepts | Any other dependencies/ sub properties associated |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| Background                        | Specifies the background color of the SymbolPalette.                                                | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default color is *Beige*.                                                                       |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| BorderThickness                   | Gets or sets the border thickness of the SymbolPalette.                                             | Dependency property  | Thickness        | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is 1.                                                                             |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| BorderBrush                       | Specifies the border color of the SymbolPalette.                                                    | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default color is *Brown*.                                                                       |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| SymbolPaletteGroupBackground      | Specifies the background color of the SymbolPalette Group.                                          | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default color is *Bisque*.                                                                      |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| SymbolPaletteGroupForeground      | Specifies the foreground color of the SymbolPalette Group.                                          | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default color is *SaddleBrown.*                                                                 |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| SymbolPaletteGroupBorderBrush     | Specifies the border color of the SymbolPalette Group.                                              | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default color is *Chocolate.*                                                                   |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ItemBorderThickness               | Gets or sets the border thickness of the SymbolPalette Item.                                        | Dependency property  | Thickness        | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is 1.                                                                             |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ItemCornerRadius                  | Gets or sets the corner radius of the SymbolPalette Item.                                           | Dependency property  | CornerRadius     | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is 2.                                                                             |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ItemMouseOverBorderBrush          | Specifies the border color of the SymbolPalette Item over which the mouse pointer rests.            | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *Orange*.                                                                      |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ItemCheckedBorderBrush            | Specifies the border color of the SymbolPalette Item that is selected.                              | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *Red*.                                                                         |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ItemCheckedMouseOverBorderBrush   | Specifies the border color of the selected SymbolPalette Item over which the mouse pointer rests.   | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *Green*.                                                                       |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| FilterSelectorBackground          | Specifies the background color of the SymbolPalette Filter.                                         | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *Chocolate*.                                                                   |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| FilterSelectorForeground          | Specifies the foreground color of the SymbolPalette Filter.                                         | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *DarkSlateGray*.                                                               |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| FilterSelectorBorderThickness     | Gets or sets the border thickness of the SymbolPalette Filter.                                      | Dependency property  | Thickness        | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is (0,0,0,1).                                                                     |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| FilterSelectorMouseOverForeground | Specifies the foreground color of the SymbolPalette Filter over which the mouse pointer rests.      | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *OldLace*.                                                                     |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| FilterSelectorBorderBrush         | specifies the border color of the SymbolPalette Filter                                              | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *Chocolate*.                                                                   |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpBackground                   | Specifies the background color of the SymbolPalette Pop-up.                                         | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *WhiteSmoke*.                                                                  |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpForeground                   | Specifies the foreground color of the SymbolPalette Pop-up.                                         | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *DarkSlateGray*.                                                               |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpBorderThickness              | Gets or sets the border thickness of the SymbolPalette Pop-up                                       | Dependency property  | Thickness        | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is (0,1,1,1).                                                                     |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpMouseOverBrush               | Specifies the background color of the SymbolPalette pop-up Item over which the mouse pointer rests. | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *LightSalmon*.                                                                 |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpBorderBrush                  | Specifies the border color of the SymbolPalette pop-up.                                             | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *Chocolate*.                                                                   |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpLeftColumnBackground         | Specifies the background color of the Check Box Column in the SymbolPalette pop-up.                 | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *LightGray*.                                                                   |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| CheckerBackground                 | Specifies the the background color of the Check Boxes in the SymbolPalette pop-up.                  | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *Bisque*.                                                                      |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| CheckerBorderBrush                | Specifies the the border color of the Check Boxes in the SymbolPalette pop-up.                      | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *DarkSlateGray.*                                                               |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| CheckerTickBrush                  | Specifies the Tick color of the selected Check Box in the SymbolPalette pop-up.                     | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                     |                      |                  |                                                   |
|                                   | The default value is *DarkSlateGray.*                                                               |                      |                  |                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+


[] 

The following code example illustrates how to set some of the SymbolPalette properties.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [DiagramControl][ diagramControl = [new] [DiagramControl](); diagramControl.SymbolPalette.BorderThickness = [new] [Thickness](2);]                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.BorderBrush = [Brushes].MidnightBlue;]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.Background = [Brushes].Blue; diagramControl.SymbolPalette.SymbolPaletteGroupBackground = [Brushes].DarkBlue; diagramControl.SymbolPalette.SymbolPaletteGroupForeground = [Brushes].White;] |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.SymbolPaletteGroupBorderBrush = [Brushes].SlateBlue;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.FilterSelectorBackground = [Brushes].SkyBlue; diagramControl.SymbolPalette.FilterSelectorForeground = [Brushes].White;]                                                                                            |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.FilterSelectorBorderBrush = [Brushes].Blue; diagramControl.SymbolPalette.FilterSelectorBorderThickness = [new] [Thickness](0);]                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.CheckerTickBrush = [Brushes].White;]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.CheckerBorderBrush = [Brushes].MidnightBlue;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.CheckerBackground = [Brushes].LightBlue; diagramControl.SymbolPalette.PopUpItemMouseOverBrush = [Brushes].CornflowerBlue;]                                                                                         |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.PopUpBorderBrush = [Brushes].MidnightBlue;]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.ItemBorderThickness = [new] [Thickness](2);]                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ diagramControl [As] [New] [DiagramControl]()]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.BorderThickness = [New] Thickness(2)]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.BorderBrush = Brushes.MidnightBlue]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.Background = Brushes.Blue]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.SymbolPaletteGroupBackground = Brushes.DarkBlue]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.SymbolPaletteGroupForeground = Brushes.White]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.SymbolPaletteGroupBorderBrush = Brushes.SlateBlue]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.FilterSelectorBackground = Brushes.SkyBlue]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.FilterSelectorForeground = Brushes.White]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.FilterSelectorBorderBrush = Brushes.Blue]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.FilterSelectorBorderThickness = [New] Thickness(0)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.CheckerTickBrush = Brushes.White]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.CheckerBorderBrush = Brushes.MidnightBlue]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.CheckerBackground = Brushes.LightBlue]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.PopUpItemMouseOverBrush = Brushes.CornflowerBlue]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.PopUpBorderBrush = Brushes.MidnightBlue]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.ItemBorderThickness = [New] Thickness(2)]**[]**                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates the various customization options that are available for the SymbolPalette Item, Group and Filter Selector.

[] 

{border="0"}

Figure 199: SymbolPalette Item, Group and Filter Selector Customization Properties[]

[] 

***[]*** 

The following screen shot illustrates the various customization options available for the SymbolPalette PopUp.

[] 

{border="0"}

Figure 200: SymbolPalette PopUp Customization Properties[]

[]{#p98} 

[]{#related-topics}

