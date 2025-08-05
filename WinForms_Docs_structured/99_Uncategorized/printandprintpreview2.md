---
title: printandprintpreview2.md
original_path: WinForms_Docs/99_Uncategorized/printandprintpreview2.md
created_at: 2025-08-05
---








  









## Print and Print Preview {#print-and-print-preview style="tab-stops: 0pt"}

The OLAP Chart can be printed by using the following code snippets. Also, a preview of the control is possible before printing it.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                        |
| [Bitmap][ bmp = [new] [Bitmap](([int])[this].olapChart1.Width.Value, ([int])[this].olapChart1.Height.Value);] |
|                                                                                                                                                                                                                                                                                                                                        |
| [this][.olapChart1.Draw(bmp);]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                        |
| [ImageResourceInfo][ iri = [new] [ImageResourceInfo](bmp, System.Drawing.Imaging.[ImageFormat].Png, [this].olapChart1.Parent.ID);]                   |
|                                                                                                                                                                                                                                                                                                                                        |
| [ResourceHolder][ printHolder = [new] [ResourceHolder]([this].Page, [this].olapChart1);]                                                                |
|                                                                                                                                                                                                                                                                                                                                        |
| [printHolder.AddResource(iri);]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                        |
| [ChartUtils][.PrintImageOnClient([this].Page, printHolder.GetResourceUrl(iri));][]                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ bmp [As] Bitmap = [New] Bitmap([CInt](Fix([Me].olapChart1.Width.Value)), [CInt](Fix([Me].olapChart1.Height.Value)))] |
|                                                                                                                                                                                                                                                                                                                                                |
| [Me][.olapChart1.Draw(bmp)]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ iri [As] ImageResourceInfo = [New] ImageResourceInfo(bmp, System.Drawing.Imaging.ImageFormat.Png, [Me].olapChart1.Parent.ID)]                                                       |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ printHolder [As] ResourceHolder = [New] ResourceHolder([Me].Page, [Me].olapChart1)]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| [printHolder.AddResource(iri)]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| [ChartUtils.PrintImageOnClient([Me].Page, printHolder.GetResourceUrl(iri))]                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 49: Print option

Sample Location

 

A sample demo is available at the following location:

 

..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapChart.Web\\Samples\\3.5\\ Exporting\\Exporting Chart Demo\\[]

[]{#related-topics}

