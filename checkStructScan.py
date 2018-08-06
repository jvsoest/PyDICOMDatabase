from DicomDatabase import DicomDatabase

# initialize dicom DB
dicomDb = DicomDatabase()
# walk over all files in folder, and index in the database
dicomDb.parseFolder("./DICOM")

for ptid in dicomDb.getPatientIds():
    # get patient by ID
    myPatient = dicomDb.getPatient(ptid)
    # loop over RTStructs of this patient
    for myStructUID in myPatient.getRTStructs():
        # Get RTSTRUCT by SOP Instance UID
        myStruct = myPatient.getRTStruct(myStructUID)
        # Get CT which is referenced by this RTStruct, and is linked to the same patient
        # mind that this can be None, as only a struct, without corresponding CT scan is found
        myScan = myPatient.getScanForRTStruct(myStruct)
        
        #only show if we have both RTStruct and linked CT
        if myScan is not None:
            print("Found patient %s RTStruct %s and linked %s" % (ptid, myStructUID, myScan.getSliceHeader(0)[0x8,0x60].value))
        else:
            print("could not find scan for RTStruct %s for patient %s" % (myStructUID, ptid))
    
    # Also check the other way around. For the scans available for a patient, is there also a RTStruct available.
    # Only needed to report the unhappy path. Happy path would have been tested by the for-loop above.
    for seriesUID in myPatient.getScans():
        if len(myPatient.getRTStructsForScan(seriesUID)) == 0:
            print("No RTStruct linked to CT %s found for patient %s" % (seriesUID, ptid))