---
title: howtorejectthechangesmadetothegridgroupingcontrol.md
original_path: WinForms_Docs/04_Controls/Grid/howtorejectthechangesmadetothegridgroupingcontrol.md
created_at: 2025-08-05
---






#### How to reject the changes made to the GridGroupingControl {#how-to-reject-the-changes-made-to-the-gridgroupingcontrol style="tab-stops: 0pt"}

[] 

By default, any changes made to the GridGroupingControl will affect the underlying data source. In order to cancel the changes, you can make use of the **RejectChanges** method to reject the recent changes made to the data source. Also, ensure that the **AcceptChanges** method is called after the date source is filled, as the RejectChanges method will roll back all the changes made to the data source, since the last time the AcceptChanges method was called.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [private][ [void] button1_Click([object] sender, [EventArgs] e) ]               |
|                                                                                                                                                                                                                                        |
| [{ ]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                        |
| [DataTable][ dt = [this].gridGroupingControl1.DataSource [as] [DataTable]; ] |
|                                                                                                                                                                                                                                        |
| [dt.RejectChanges(); ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] button1_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                            |
| [Dim][ dt [As] DataTable = [TryCast]([Me].gridGroupingControl1.DataSource, DataTable)]                                                                 |
|                                                                                                                                                                                                                                                                                                            |
| [dt.RejectChanges()]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p656} 

[]{#related-topics}

