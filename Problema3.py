import requests
import zipfile

response = requests.get("https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

image_data = response.content

zip_file = zipfile.ZipFile("image.zip", "w")

zip_file.writestr("image.jpg", image_data)

zip_file.close()

zip_file = zipfile.ZipFile("image.zip", "r")

file_names = zip_file.namelist()

image_data = zip_file.read(file_names[0])

zip_file.close()
