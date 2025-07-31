---
title: ilistdatasource.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\ilistdatasource.md
created_at: 2025-07-03
---






##### IList Data Source {#ilist-data-source style="tab-stops: 0pt"}

Simple IList-based instances can be easily bound to the Chart. The following code example illustrates how to bind IList-based instances as the data source to Chart.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [public][ [IList] marks()]                                                                                             |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [            [List]\<[mark]\> markList = [new] [List]\<[mark]\>();]        |
|                                                                                                                                                                                                                                     |
| [            markList.Add([new] [mark]() { ID = 0, Name = [\"John\"], Mark1 = 97, Mark2 = 99, Mark3 = 85, Mark4 = 92 });]  |
|                                                                                                                                                                                                                                     |
| [            markList.Add([new] [mark]() { ID = 1, Name = [\"James\"],Mark1 = 45, Mark2 = 35, Mark3 = 48, Mark4 = 42 });]  |
|                                                                                                                                                                                                                                     |
| [            markList.Add([new] [mark]() { ID = 2, Name = [\"Sam\"],Mark1 = 32, Mark2 = 65,Mark3 = 67,Mark4 = 78});]       |
|                                                                                                                                                                                                                                     |
| [            markList.Add([new] [mark]() { ID = 3, Name = [\"Victor\"],Mark1 = 30, Mark2 = 39,Mark3 = 38,Mark4 = 56});]    |
|                                                                                                                                                                                                                                     |
| [            markList.Add([new] [mark]() { ID = 4, Name = [\"Faith\"], Mark1= 25,Mark2 = 45,Mark3 = 77,Mark4 = 19});]      |
|                                                                                                                                                                                                                                     |
| [            markList.Add([new] [mark]() { ID = 5, Name =[\"Joyce\"], Mark1= 50,Mark2 = 35,Mark3 = 54,Mark4 = 55});]       |
|                                                                                                                                                                                                                                     |
| [            markList.Add([new] [mark]() { ID = 6, Name = [\"Silvy\"],Mark1 = 70, Mark2 = 28, Mark3 = 35, Mark4 = 45 });]  |
|                                                                                                                                                                                                                                     |
| [            markList.Add([new] [mark]() { ID = 7, Name = [\"Ian\"],Mark1 = 45,Mark2 = 85,Mark3 = 77,Mark4 =19});]         |
|                                                                                                                                                                                                                                     |
| [            markList.Add([new] [mark]() { ID = 8, Name = [\"Mandy\"], Mark1 = 90, Mark2 = 45, Mark3 = 54, Mark4 = 55 });] |
|                                                                                                                                                                                                                                     |
| [            markList.Add([new] [mark]() { ID = 9, Name = [\"Alan\"],  Mark1 = 50, Mark2 = 28, Mark3 = 25, Mark4 = 45 });] |
|                                                                                                                                                                                                                                     |
| [            [return] markList;]                                                                                                                                           |
|                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 The following screen shot illustrates how a Chart Series is associated to the Chart by using IList-based instances.

**[]** 

{border="0"}

Figure 55: Chart Series bound to IList Data Source

[] 

See Also

[] 

[]{.UGHyperlink}

[ ]{.UGHyperlink}

[ ]{.UGHyperlink}

[ ]{.UGHyperlink}

[]{.UGHyperlink}

[]{#p26} 

[]{#related-topics}

