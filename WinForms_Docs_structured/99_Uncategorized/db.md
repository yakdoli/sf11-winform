---
title: db.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\db.md
created_at: 2025-07-03
---








  









### DB {#db style="tab-stops: 0pt"}

 

Returns the depreciation of an asset for a specified period using the fixed-declining balance method.

 

**Syntax**

 

**DB(cost, salvage, life, period, month)**

 

where:

**cost** is the initial cost of the asset.

**salvage** is the value at the end of the depreciation (sometimes called the salvage value of the asset).

**life** is the number of periods over which, the asset is being depreciated (sometimes called the useful life of the asset).

**period** is the period for which, you want to calculate the depreciation. Period must use the same units as life.

**month** is the number of months in the first year. If month is omitted, it is assumed to be 12.

 

Remarks

[] 

[·      ]The fixed-declining balance method computes the depreciation at a fixed rate. DB uses the following formulas to calculate the depreciation for a period:

[] 

(cost - total depreciation from prior periods) \* rate

[] 

where:

**rate** = 1 - ((salvage / cost) \^ (1 / life)), rounded to three decimal places

 

[·      ]Depreciation for the first and last periods is a special case. For the first period, DB uses this formula:

[] 

cost \* rate \* month / 12

[] 

[·      ]For the last period, DB uses this formula:

[] 

((cost - total depreciation from prior periods) \* rate \* (12 - month)) / 12

 

[]{#related-topics}

