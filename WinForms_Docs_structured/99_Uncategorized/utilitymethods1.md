---
title: utilitymethods1.md
original_path: WinForms_Docs/99_Uncategorized/utilitymethods1.md
created_at: 2025-08-05
---






##### Utility Methods {#utility-methods style="tab-stops: 0pt"}

 

Resetting Ribbon States

You can load the Normal (Initial) Ribbon state at runtime by calling the ResetRibbonState method. This is a parameter less method. This will load the Normal state of the Ribbon control. Resetting the Ribbon state is applicable while AutoPersist is enabled in Ribbon elements. You can customize the resetting state of Ribbon elements by enabling the AutoPersist property.

**[]** 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                  |
| [private][ [void] ResetState_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                  |
| [        {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [            [this].MyRibbon.ResetRibbonState();]                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [        }]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Deleting Ribbon States

You can delete the unused saved Isolated Storage files by using the DeleteRibbonState method. This method has two overloads. They are:

[·      ]DeleteRibbonState()

[·      ]DeleteRibbonState(IsolatedStorageFile isoStorage, string deletefileName)

The first overloaded method will delete the default saved file from the default Isolated Storage file location. The following code snippet shows how to delete the default saved file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                           |
| [  private][ [void] DeleteRibbonState_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                           |
| [     {]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                           |
| [       [this].MyRibbon.DeleteRibbonState(); ]                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [     }]                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The second overloaded method is used to delete any file from specified Isolated Storage location. The following code snippet shows how to delete any file from the Isolated Storage location.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                           |
| [  private][ [void] DeleteRibbonState_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                           |
| [     {]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                           |
| [       [IsolatedStorageFile] storage = ]                                                                                                                                     |
|                                                                                                                                                                                                                                           |
| [                      [IsolatedStorageFile].GetStore([IsolatedStorageScope].User  ]                                                                  |
|                                                                                                                                                                                                                                           |
| [                              \|[IsolatedStorageScope].Assembly, [null], [null]);]                                                 |
|                                                                                                                                                                                                                                           |
| [       [this].MyRibbon.DeleteRibbonState(storage,[\"RibbonState1.dat\"]);       ]                                                                       |
|                                                                                                                                                                                                                                           |
| [     }]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#_How_to_load} 

[]{#related-topics}

