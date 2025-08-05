---
title: printing.md
original_path: WinForms_Docs/99_Uncategorized/printing.md
created_at: 2025-08-05
---








  









## Printing {#printing style="tab-stops: 0pt"}

**[]** 

Print a chart control using the **ChartUtils** class of chart control as follows:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Bitmap][ bmp = [new] [Bitmap](([int])[this].ChartWebControl1.Width.Value, ([int])[this].ChartWebControl1.Height.Value);] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [this][.ChartWebControl1.Draw(bmp);]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| [ImageResourceInfo][ iri = [new] [ImageResourceInfo](bmp, ImageFormat.Png, [this].ChartWebControl1.Parent.ID);]                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [ResourceHolder][ printHolder = [new] [ResourceHolder]([this].Page);]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [printHolder.AddResource(iri);]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [ChartUtils][.PrintImageOnClient([this].Page, printHolder.GetResourceUrl(iri));]                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ bmp [As] [New] Bitmap([CInt]([Me].ChartWebControl1.Width.Value), [CInt]([Me].ChartWebControl1.Height.Value))] |
|                                                                                                                                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.Draw(bmp)]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ iri [As] [New] ImageResourceInfo(bmp, ImageFormat.Png, [Me].ChartWebControl1.Parent.ID)]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ printHolder [As] [New] ResourceHolder([Me].Page)]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [printHolder.AddResource(iri)]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [ChartUtils.PrintImageOnClient([Me].Page, printHolder.GetResourceUrl(iri))]                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

A sample illustrating the printing features is available in the below location.

 

..\\My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Web\\chart.web\\Samples\\3.5\\Printing\\ChartWebPrinting

[]{#p270} 

[]{#related-topics}

