---
title: methods15.md
original_path: WinForms_Docs/99_Uncategorized/methods15.md
created_at: 2025-08-05
---






#### Methods {#methods style="tab-stops: 0pt"}

 

The following table describes the methods required for Zooming and Panning of Chart.

Methods for Chart Zooming/Panning


  ------------------ ---------------------------------- ------------ -------------
  Method             Description                        Parameters   Return Type
  SwitchZooming      Enables zooming operations            Nil       void
  ZoomInCommand      Enables zooming in operation          Nil       void
  ZoomOutCommand     Enables zooming out operation         Nil       void
  ZoomResetCommand   Enables zooming reset operation.      Nil       void
  ------------------ ---------------------------------- ------------ -------------


[] 


[{border="0"}]Note[:][ T]o enable the zooming feature, the SwitchZooming method has to be invoked.


 The following code snippet describes how to call the above methods.[]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[\[C#\][]                                                                                                       |
|                                                                                                                                                                  |
| [ ][//To Enable Zoom Operations][]         |
|                                                                                                                                                                  |
| chart.Areas\[0\].SwitchZooming();[]                                                                              |
|                                                                                                                                                                  |
| [ ][//To perform the Zoom-In command][]    |
|                                                                                                                                                                  |
| chart.Areas\[0\].ZoomInCommand();[]                                                                              |
|                                                                                                                                                                  |
| [ ][//To perform the Zoom-Out command][]   |
|                                                                                                                                                                  |
| chart.Areas\[0\].ZoomOutCommand();[]                                                                             |
|                                                                                                                                                                  |
| [ ][//To perform the Zoom-Reset command][] |
|                                                                                                                                                                  |
| chart.Areas\[0\].ZoomResetCommand();                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

