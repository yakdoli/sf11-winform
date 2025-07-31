---
title: classolapchart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\classolapchart.md
created_at: 2025-07-03
---






##### Class: OlapChart {#class-olapchart style="tab-stops: 0pt"}

###### 1.4.1.1.1.1 Public Properties {#public-properties style="tab-stops: 0pt"}

[] 

  ---------------------------- ----------------------------------------------------------------------------------------------------------
  DesignerSettings             Gets or sets the designer settings that can be used for creating the XAML report during the design-time.
  ChartAppearance              Gets or sets the chart appearance settings such as ChartArea background, BorderColor, ChartType, etc.
  ChartType                    Gets or sets the chart type.
  ColorModel                   Gets the color model used to paint series.
  CornerRadius                 Gets or sets the corner radius of the OLAP Chart.
  GridBackground               Gets or sets the grid background.
  GridLineStroke               Gets or sets the grid line stroke.
  Legend                       Gets or sets the chart legend.
  OlapDataManager              Gets or sets the olap data manager.
  PrimaryAxis                  Gets or sets the primary axis.
  ShowPrimaryAxisLabelBoder    Gets or sets a value indicating whether the primary axis label border should be visible or not.
  SecondaryAxis                Gets or sets the secondary axis.
  Series                       Gets the series collection.
  DisplayMode                  Gets or sets the display mode.
  SeriesToolTipTemplate        Gets or sets the series tool tip template.
  KpiAlignment                 Gets or sets the KPI alignment.
  PrimaryAxisLabelVisibility   Gets or sets the primary axis label visibility.
  ---------------------------- ----------------------------------------------------------------------------------------------------------

[] 

###### 1.4.1.1.1.2 Public Methods {#public-methods style="tab-stops: 0pt"}

[] 


  -------------------------- ---------------------------------------------------------------------------------------------------------------------
  DataBind                   Binds the data.
  ExportintoNewDoc           Exports the chart to a new word document.
  ExportIntoTemplateDoc      Overloaded. Exports the chart to an existing word document by replacing the chart at the marker string position.
  ExportIntoNewPdf           Exports the chart to a new PDF document.
  OnApplyTemplate            Invoked whenever application code or internal processes call ApplyTemplate().
  SetChartApperanceDetails   Sets the chart appearance settings.
  ShowAppearanceDialog       Displays the chart appearance customization dialog. It can be used for customizing the chart appearance properties.
  -------------------------- ---------------------------------------------------------------------------------------------------------------------


[] 

###### 1.4.1.1.1.3 Public Events {#public-events style="tab-stops: 0pt"}

[] 


  --------------- ---------------------------------------------
  BeforeRefresh   Occurs before the refresh of the OLAP area.
  AfterRefresh    Occurs after the refresh of the OLAP area.
  --------------- ---------------------------------------------


[] 

[]{#related-topics}

