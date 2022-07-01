def upload_location(instance, filename):
	_, extension = filename.split('.')
	upload_name = instance.title.lower()
	upload_name = upload_name.replace(" ", "-")
	if extension == "jpg":
		return f"books_image/{upload_name}.{extension}"
	elif extension == "pdf":
		return f"books_pdf/{upload_name}.{extension}"
    

    
    
