def handle_uploaded_file(file,name):
    with open(f"/images/{name}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
        print("teste",f"/images/{name}")