# https://pythonhosted.org/pywebhdfs/

from pywebhdfs.webhdfs import PyWebHdfsClient

hdfs = PyWebHdfsClient(host='localhost',port='9870', user_name='root')


# Append file
my_data = '01010101010101010101010101010101'
my_file = '/test/myfile.txt'
hdfs.append_file(my_file, my_data)

# Create File
my_data = '01010101010101010101010101010101'
my_file = '/user/root/test/test.txt'
hdfs.create_file(my_file, my_data)

my_dir = '/user/root/test'
print(hdfs.get_file_dir_status(my_dir))

my_dir = '/user/root/test'
print(hdfs.list_dir(my_dir))

# Rename an existing directory or file on HDFS
current_dir = '/user/root/teste'
destination_dir = '/user/root/test'
hdfs.rename_file_dir(current_dir, destination_dir)