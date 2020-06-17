import common, sql
import os, sys
import add_project_snapshots as aps

def read_cl_args():
    return sys.argv[1], sys.argv[2], sys.argv[3]

if __name__=='__main__':
    project, snapshotFile, alertFile = read_cl_args()
    projectId=common.get_project_id(project)
    
    aps.add_snapshots(snapshotFile)

    