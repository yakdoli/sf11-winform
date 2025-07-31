---
title: howtogetacountofthenumberofoccurrencesofastringintheeditcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtogetacountofthenumberofoccurrencesofastringintheeditcontrol.md
created_at: 2025-07-03
---








  









## How To Get a Count Of the Number Of Occurrences Of a String In the Edit Control {#how-to-get-a-count-of-the-number-of-occurrences-of-a-string-in-the-edit-control style="tab-stops: 0pt"}

[] 

You can get a count of the number of occurrences of a string in the Edit Control using the **Matches** method of the **Regex** class.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [Regex][ r = [new] [Regex](searchText, [RegexOptions].IgnoreCase);] |
|                                                                                                                                                                                                                         |
| [MatchCollection][ ma = r.Matches([this].editControl1.Text);]                                                 |
|                                                                                                                                                                                                                         |
| [return][ ma.Count;]                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                  |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [Dim][ r [As] Regex = [New] Regex(pattern, RegexOptions.IgnoreCase)] |
|                                                                                                                                                                                                     |
| [Dim][ ma [As] MatchCollection = r.Matches([Me].editControl1.Text)]  |
|                                                                                                                                                                                                     |
| [return][ ma.Count]                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p192} 

[]{#related-topics}

