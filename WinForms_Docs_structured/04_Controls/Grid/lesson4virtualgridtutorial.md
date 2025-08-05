---
title: lesson4virtualgridtutorial.md
original_path: WinForms_Docs/04_Controls/Grid/lesson4virtualgridtutorial.md
created_at: 2025-08-05
---








  









### Lesson 4: Virtual Grid Tutorial {#lesson-4-virtual-grid-tutorial style="tab-stops: 0pt"}

[] 

A virtual grid is one where the grid does not hold any data. All the data that is displayed by the grid is provided on demand from some external data source to the grid when it needs it. Virtual grids are ideal for displaying large amounts of data which are already stored in some manner. This data is not moved from its original location or stored in **GridStyleInfo** objects. Instead, GridInfoStyle objects are created on the fly, to temporarily hold only the necessary data and are discarded when they are no longer needed. There is no data stored in the grid.

[] 

Implementing a virtual grid is straight forward. Depending upon the functionality that you need, you can implement a virtual grid with as few as three events. To implement a virtual grid, you must tell the grid how many rows and columns your data source has, and provide the grid the data from your data source. You must do these things in real time, only when the grid requests these data elements. When the grid needs to know the number of rows in the grid, it will fire the **QueryRowCount** event. When it needs to know the number of columns in the grid, it will fire the **QueryColCount** event. When it needs to know a GridStyleInfo object for a particular cell, it will fire the **QueryCellInfo** event. By handling these events and setting appropriate members of the **EventArgs**, you are providing the information that the grid needs at the time when it needs it.

[] 

In this section, you will learn how to set up an external data source, and then display it by using a virtual grid. The first iteration will allow the display of the external data source; a second iteration will add code that will allow you to edit the displayed data in the virtual grid, pushing the changes back to your data source.

[] 

In this lesson, you will learn about the following topics.

[] 

 

[]{#p20} 

 

More:



















