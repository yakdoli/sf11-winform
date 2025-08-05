---
title: pathsupportformaps2.md
original_path: WinForms_Docs/99_Uncategorized/pathsupportformaps2.md
created_at: 2025-08-05
---








  









## Path Support for Maps {#path-support-for-maps style="tab-stops: 0pt"}

Paths are the lines which are used to depict the way or route between two points. Paths are drawn through given points. By using Paths we can show train, road, air and sea ways in the maps. With path support street view for the particular city can also implemented.

{border="0"}

Figure 17: Map Path

Properties

  --------------------- ------------------------------------------------ ------------ --------------------------------------------------------- ------------------------------
  Property              Description                                      Type         Data Type                                                 Reference links
  PathPoints            The start and end points of a particular path.   Dependency   ObservableCollection\<Point\>[]   NA[]
  PathLabel             The name of a particular path.                   Dependency   string                                                    NA
  PathLabelFontStyle    The font style for PathLabel.                    Dependency   FontStyle                                                 NA
  PathColor             The color options for the path.                  Dependency   Brush                                                     NA
  PathStroke            Gets or sets stroke color of the MapPath.        Dependency   Brush                                                     NA
  PathStrokeThickness   Gets or sets stroke thickness of the MapPath.    Dependency   double                                                    NA
  PathLabelForeground   The color options of PathLabel.                  Dependency   Brush                                                     NA
  PathLabelFontFamily   Font names can be changed for the PathLabel.     Dependency   FontFamily                                                NA
  PathLabelFontSize     Font size can be changed for the Path Label.     Dependency   Double                                                    NA
  LabelPoint            The location of the LabelPoint.                  Dependency   Point                                                     NA
  PathLabelPosition     OnPoint and OnMiddlePoint.                       Dependency   PathLabelPosition                                         NA
  IsDynamicCreatePath   A dynamic path is created when enabled.          Dependency   bool                                                      NA[]
  --------------------- ------------------------------------------------ ------------ --------------------------------------------------------- ------------------------------

 

More:





