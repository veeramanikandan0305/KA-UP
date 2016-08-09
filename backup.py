
import zipfile
import sys
import os
import datetime
import re
from distutils.dir_util import copy_tree
 

def zip_folder(folder_path, output_path):
    """Zip the contents of an entire folder (with that folder included
    in the archive). Empty subfolders will be included in the archive
    as well.
    """
    parent_folder = os.path.dirname(folder_path)
    # Retrieve the paths of the folder contents.
    contents = os.walk(folder_path)
    try:
        zip_file = zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED)
        for root, folders, files in contents:
            # Include all subfolders, including empty ones.
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder + '\\',
                                                      '')
                print "Adding '%s' to archive." % absolute_path
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder + '\\',
                                                      '')
                print "Adding '%s' to archive." % absolute_path
                zip_file.write(absolute_path, relative_path)
        print "'%s' created successfully." % output_path
    except IOError, message:
        print message
        sys.exit(1)
    except OSError, message:
        print message
        sys.exit(1)
    except zipfile.BadZipfile, message:
        print message
        sys.exit(1)
    finally:
        zip_file.close()
#~ def copy_file():       

def backup():
	backup= open('/backup.txt').read()
	backup=backup.splitlines()
	len(backup)
	for index in range(len(backup)):
		backup_list = backup[index].split(',')
		if  ('/' in backup_list[0]):
			backup_list[0]=backup_list[0].replace(" ", "")
			filename=backup_list[0].split('/')
			file_index=len(filename)
			file_name=str(filename[file_index-1])+"_"+str(datetime.datetime.now().day)+"_"+str(datetime.datetime.now().month)
			fromDirectory = backup_list[0].replace("/"+str(filename[file_index-1]),"")
			fromsrc=backup_list[0]
			file_tempname=str(filename[file_index-1])
			toDirectory = "/backup_temp/"+file_tempname
			copy_tree(fromsrc, toDirectory)
			if not re.search(fromDirectory, toDirectory, re.IGNORECASE):
				#~ copy_tree(fromDirectory, toDirectory)
				print fromDirectory
				print toDirectory
			backup_list[1]=backup_list[1].replace(" ", "")
			cron_time=backup_list[2].replace(" ", "")
			dest=backup_list[1]+file_name+".zip"
			src="./backup_temp/"+file_tempname
			cron_time=cron_time.split('/')
			if (int(cron_time[1]) is 1):
				zip_folder(backup_list[0],dest)
			elif(int(cron_time[1]) is 7):
				week_days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
				day_name=datetime.datetime.today().strftime("%A")
				if re.search(day_name, week_days[int(cron_time[0])], re.IGNORECASE):
					zip_folder(src,dest)
			elif(int(cron_time[1]) is 30):
				month_day= datetime.datetime.today().day
				if (int(cron_time[0]) is month_day):
					zip_folder(src,dest)
			else:
				print "WARNING : Please Mention Valid  Cron Time for  backup on line number " + str(index+1)
			#~ if re.search('Social', strong_tag.title.text, re.IGNORECASE):

	
if __name__ == '__main__':
    backup()
