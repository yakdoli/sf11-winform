---
title: pathsupportformaps.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\pathsupportformaps.md
created_at: 2025-07-03
---








  









## Path Support for Maps {#path-support-for-maps style="tab-stops: 0pt"}

This feature enables you to provide a street view in a map. You can add paths to a map by specifying the points, and display label on those paths. While performing zoom and pan operations, paths will be automatically updated. You can customize the path style.

 

Use Case Scenarios

Path support enables you to draw paths that depict routes in a map.

 

Properties

Table 15: Properties Table


  --------------------- --------------------------------------------------------------- ------------ --------------------------------------------------------- ------------------------------
  Property              Description                                                     Type         Data Type                                                 Reference links
  PathPoints\*          Specifies the start and end points of a particular path.        Dependency   ObservableCollection\<Point\>[]   NA[]
  PathLabel             Specifies the text for PathLabel.                               Dependency   String                                                    NA
  PathLabelFontStyle    Specifies the font style for PathLabel.                         Dependency   FontStyle                                                 NA
  PathColor             Specifies the color options for the path.                       Dependency   Brush                                                     NA
  PathStrokeThickness   Gets or sets stroke thickness of the MapPath.                   Dependency   Double                                                    NA
  PathLabelForeground   Specifies the color options of PathLabel's Foreground.          Dependency   Brush                                                     NA
  PathLabelFontFamily   Specifies the FontFamily for the PathLabel.                     Dependency   FontFamily                                                NA
  PathLabelFontSize     Specifies the font size for the Path Label.                     Dependency   Double                                                    NA
  LabelPoint            Specifies the PathLabel's Position on the Path.                 Dependency   Point                                                     NA
  PathLabelPosition     Specifies the PathLabel position as OnPoint or OnMiddlePoint.   Dependency   PathLabelPosition                                         NA
  IsDynamicCreatePath   Specifies whether dynamic path creation is enabled.             Dependency   Bool                                                      NA
  --------------------- --------------------------------------------------------------- ------------ --------------------------------------------------------- ------------------------------


***[]*** 


Note:



***[·    ]***Properties marked with \* are mandatory.[]

***[·    ]***LabelPoint is mandatory, when you add label to the path through Code Behind.



[] 


More:









