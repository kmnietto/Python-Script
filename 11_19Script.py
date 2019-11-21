import arcpy
fc = r"H:\PythonGIS\Menietto\Data\data1\USA.gdb\us_states"
arcpy.MakeFeatureLayer_management(fc, "all")
where = """"STATE_ABBR" = 'TN'"""""
print where
arcpy.MakeFeatureLayer_management(fc, "tn", where_clause = where)
arcpy.SelectLayerByLocation_management("all", "BOUNDARY_TOUCHES", "tn")
with arcpy.da.SearchCursor("all", "STATE_ABBR") as cursor:
    for row in cursor:
        print row[0]



