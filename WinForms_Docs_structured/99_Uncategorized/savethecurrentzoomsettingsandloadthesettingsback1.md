---
title: savethecurrentzoomsettingsandloadthesettingsback1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\savethecurrentzoomsettingsandloadthesettingsback1.md
created_at: 2025-07-03
---








  









### Save the Current Zoom Settings and Load the Settings Back {#save-the-current-zoom-settings-and-load-the-settings-back style="tab-stops: 0pt"}

Zoom settings can be saved into variables and this saved settings can be applied back again using the following code snippet.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                     |
| [            [//Save current zoom setting.]]                                                                                                              |
|                                                                                                                                                                                                                     |
| [            [double] SavedZoomFactor = diagramView.ZoomFactor;]                                                                                           |
|                                                                                                                                                                                                                     |
| [            [double] SavedCurrentZoom = ([double]) diagramView.GetValue([DiagramView].CurrentZoomProperty);] |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [            [//Load the saved zoom settings.]]                                                                                                           |
|                                                                                                                                                                                                                     |
| [            [//Reset the current zoom]]                                                                                                                  |
|                                                                                                                                                                                                                     |
| [            [ZoomCommands].Reset.Execute(diagramView.Page, diagramView);]                                                                              |
|                                                                                                                                                                                                                     |
| [            [//Set the zoom factor temporarily to the stored CurrentZoomProperty ]]                                                                      |
|                                                                                                                                                                                                                     |
| [            diagramView.ZoomFactor = SavedCurrentZoom - 1;]                                                                                                                    |
|                                                                                                                                                                                                                     |
| [            [//Now if a zoom operation is performed, we will get the stored zoom setting.]]                                                              |
|                                                                                                                                                                                                                     |
| [            [ZoomCommands].ZoomIn.Execute(diagramView.Page, diagramView);]                                                                             |
|                                                                                                                                                                                                                     |
| [            [//Change the Zoom factor to the required value.]]                                                                                           |
|                                                                                                                                                                                                                     |
| [            diagramView.ZoomFactor = SavedZoomFactorr;]                                                                                                                        |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [            ]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [\'Save current zoom setting.][]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [        [Dim] SavedZoomFactor [As] [Double] = [DiagramView].ZoomFactor]                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [        [Dim] SavedCurrentZoom [As] [Double] = [CDbl]([DiagramView].GetValue([DiagramView].CurrentZoomProperty))] |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [        [\'Load the saved zoom settings.]]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                            |
| [        [\'Reset the current zoom]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [                  ZoomCommands.Reset.Execute(diagramView.Page, diagramView)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                            |
| [        [\'Set the zoom factor temporarily to the stored CurrentZoomProperty ]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                            |
| [                  diagramView.ZoomFactor = SavedCurrentZoom - 1]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                            |
| [        [\'Now if a zoom operation is performed, we will get the stored zoom setting.]]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [                  ZoomCommands.ZoomIn.Execute(diagramView.Page, diagramView)]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [        [\'Change the Zoom factor to the required value.]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                            |
| [                  diagramView.ZoomFactor = SavedZoomFactorr][]                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

