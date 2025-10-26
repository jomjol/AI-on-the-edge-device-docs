# Scripted File Upload
To upload a file e.g. using `curl`, you first have to delete it and then upload it:
```
curl -d '' http://192.168.1.153/delete/html/index.html
curl --data-binary @ota_page.html http://192.168.1.153/upload/html/index.html
```
