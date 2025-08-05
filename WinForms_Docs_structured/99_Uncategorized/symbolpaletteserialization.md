---
title: symbolpaletteserialization.md
original_path: WinForms_Docs/99_Uncategorized/symbolpaletteserialization.md
created_at: 2025-08-05
---








  









### SymbolPaletteSerialization {#symbolpaletteserialization style="tab-stops: 0pt"}

Serialization is the process of saving and retrieving the SymbolPalette groups and items. Essential Diagram WPF supports saving the SymbolPalette as a XAML file. This load and save feature allows you to save the SymbolPalette for future use. You can continue working on their page by loading the appropriate XAML file.

SymbolPaletteSerialization feature provides an option to save and load the SymbolPalette, SymbolPalette groups, elements and items in diagram control. So any item can be customised and imported onto the SymbolPalette.

 

[[·     ]]{.apple-style-span}[[User can easily Save/Load the SymbolPalette]]{.apple-style-span}[[]]{.apple-style-span}

[[·     ]]{.apple-style-span}[[User can Save/Load the SymbolPaletteGroup]]{.apple-style-span}[[]]{.apple-style-span}

[[·     ]]{.apple-style-span}[[User can Save/Load the SymbolPaletteItem]]{.apple-style-span}[[]]{.apple-style-span}

 


+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| Method                 | Description                                                                                                                                     | Parameters         | Return Type | Reference links |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| SaveSymbolPalette      | Displays the save dialog box to save the entire SymbolPallete(including all SymbolPalette groups) into XAML file.                               | NA                 | Void        | NA              |
|                        |                                                                                                                                                 |                    |             |                 |
|                        |                                                                                                                                                 |                    |             |                 |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| LoadSymbolPalette      | The existing SymbolPallete groups will be cleared and new groups will be added from selected Xaml file.                                         | NA                 | Void        | NA              |
|                        |                                                                                                                                                 |                    |             |                 |
|                        |                                                                                                                                                 |                    |             |                 |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| SaveSymbolPaletteGroup | Saves the Symbol Palette Group into Xaml file using the given  SymbolPaletteGroup parameter                                                     | SymbolPaletteGroup | Void        | NA              |
|                        |                                                                                                                                                 |                    |             |                 |
|                        |                                                                                                                                                 |                    |             |                 |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| LoadSymbolPaletteGroup | Displays the Load Dialogue Box to load the Symbol Palette Group from the selected Xaml file.                                                    | NA                 | Void        | NA              |
|                        |                                                                                                                                                 |                    |             |                 |
|                        |                                                                                                                                                 |                    |             |                 |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| SaveSymbolPaletteItem  | Saves the Symbol Palette Item into Xaml file using the given SymbolPaletteItem parameter.                                                       | NA                 | Void        | NA              |
|                        |                                                                                                                                                 |                    |             |                 |
|                        |                                                                                                                                                 |                    |             |                 |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| LoadSymbolPaletteItem  | Loads the SymbolPalette Item from the Xaml file. The Items are loaded in any given Symbol Palette Group using the SymbolPaletteGroup parameter. | NA                 | Void        | NA              |
|                        |                                                                                                                                                 |                    |             |                 |
|                        |                                                                                                                                                 |                    |             |                 |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------+-----------------+


 

 

[]{#related-topics}

