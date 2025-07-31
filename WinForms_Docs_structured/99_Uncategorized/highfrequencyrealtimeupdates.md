---
title: highfrequencyrealtimeupdates.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\highfrequencyrealtimeupdates.md
created_at: 2025-07-03
---






##### High Frequency Real Time Updates {#high-frequency-real-time-updates style="tab-stops: 0pt"}

[] 

Essential Grid supports frequent updates that occur in random cells across the grid while keeping CPU usage to a minimum level.

[] 

Example:

[] 

In this example, a timer changes the cell in the short intervals, inserts and removes rows. This example draws cell changes directly to the graphics context instead of performing an Invalidate. It also shows you how to draw text using the GDI instead of the GDI+ and how to optimize updates for inserting and removing rows. You can start multiple instances without slowing down your machine. You can confirm the same by viewing the TaskManager CPU usage while the sample runs.

[] 

{border="0"}

[] 

*[Figure ][194][: Trader Grid]*

[] 

A sample demonstrating this feature is available under the following sample installation path.

[] 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Performance\\Trader Grid Test Demo***

 

[]{#p355} 

 

[]{#related-topics}

