from pywebhdfs.webhdfs import PyWebHdfsClient

hdfs = PyWebHdfsClient(host='localhost',port='9870', user_name='root')

#To use this client
PyWebHdfsClient(host='host',port='50070', user_name='hdfs')

# Appends to an existing file on HDFS
my_data = '01010101010101010101010101010101'
my_file = 'user/hdfs/data/myfile.txt'
hdfs.append_file(my_file, my_data)

# Creates a new file on HDFS
my_data = '01010101010101010101010101010101'
my_file = 'user/hdfs/data/myfile.txt'
hdfs.create_file(my_file, my_data)

# Delete an existing file or directory from HDFS
my_file = 'user/hdfs/data/myfile.txt'
hdfs.delete_file_dir(my_file)

# Get the file_status of a single file or directory on HDFS
my_file = 'user/hdfs/data/myfile.txt'
hdfs.get_file_dir_status(my_file)

# Get a list of file_status for all files and directories inside an HDFS directory
my_dir = 'user/hdfs'
hdfs.list_dir(my_dir)

# Create a new directory on HDFS
my_dir = 'user/hdfs/data/new_dir'
hdfs.make_dir(my_dir)

# Reads from a file on HDFS and returns the content
my_file = 'user/hdfs/data/myfile.txt'
hdfs.read_file(my_file)

# Rename an existing directory or file on HDFS
current_dir = 'user/hdfs/data/my_dir'
destination_dir = 'user/hdfs/data/renamed_dir'
hdfs.rename_file_dir(current_dir, destination_dir)