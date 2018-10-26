from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='openstack')
images = conn.list_images()
for image in images:
    print(image)
