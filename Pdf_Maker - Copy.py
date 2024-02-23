from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def convert_images_to_pdf_jpg_png(image_folder, pdf_filename, start_index, end_index, file_type):
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    for i in range(start_index, end_index + 1):
        image_path = f"{image_folder}\\{i}.{file_type}"

        try:
            img = Image.open(image_path)
        except FileNotFoundError:
            print(f"Image {i}.{file_type} not found. Skipping.")
            continue

        width, height = letter
        img_width, img_height = img.size

        # Scale the image to fit the page while maintaining aspect ratio
        scale_factor = min(width / img_width, height / img_height)
        img_width *= scale_factor
        img_height *= scale_factor

        c.drawInlineImage(image_path, (width - img_width) / 2, (height - img_height) / 2, width=img_width, height=img_height)
        c.showPage()

    c.save()
    print(f"PDF {pdf_filename} created successfully.")


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os

def convert_webp_images_to_pdf(image_folder, pdf_filename, start_index, end_index):
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    #IF FILE VALUES GO UP 001.webp, 002.webp, 003.webp,...,013.webp, 014.webp, 015.webp,...,100.webp
    # for i in range(start_index, end_index + 1):
    #     if(i<10):
    #         image_path = os.path.join(image_folder, f"00{i}.webp")
    #     elif (i<100):
    #         image_path = os.path.join(image_folder, f"0{i}.webp")
    #     else:
    #         image_path = os.path.join(image_folder, f"{i}.webp")

    #COMMENT lINE 50 AND 51 IF UNCOMMENTED LINE 41-47
    for i in range(start_index, end_index + 1):
        image_path = os.path.join(image_folder, f"{i}.webp")
    
        try:
            print(i)
            img = Image.open(image_path)
        except FileNotFoundError:
            print(f"Image {i}.webp not found. Skipping.")
            continue

        width, height = letter
        img_width, img_height = img.size

        # Scale the image to fit the page while maintaining aspect ratio
        scale_factor = min(width / img_width, height / img_height)
        img_width *= scale_factor
        img_height *= scale_factor

        # Draw the image on the PDF
        c.drawImage(image_path, (width - img_width) / 2, (height - img_height) / 2, width=img_width, height=img_height)

        # ShowPage is used to move to the next page
        c.showPage()

    # Save the PDF
    c.save()
    print(f"PDF {pdf_filename} created successfully.")

#RUN TO DEBUG IF PDF ISNT WORKING; IF IT DOESNT WORK IT MIGHT BE A FOLDER/FILE NAME ISSUE
def img_show_debug():
    from PIL import Image

    # Specify the path to your WebP image
    webp_path = f"C:\\X\\X\\FOLDER\\{1}.webp"

    # Open the WebP image using Pillow
    try:
        img = Image.open(webp_path)
        # Now you can work with the image using Pillow functions
        img.show()  # Opens the image using the default image viewer
    except FileNotFoundError:
        print(f"Image {webp_path} not found.")

#on a good day you can rename the pictures using this function and it will keep the
#order, on a bad day rename the pictures out of order and you will have to order it manually
def rename_files_by_order(folder_path, start, file_type):
    # Ensure the folder path ends with a slash
    if not folder_path.endswith("/"):
        folder_path += "/"

    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file and rename it
    for old_name in files:
        # Skip directories
        if os.path.isdir(os.path.join(folder_path, old_name)):
            continue

        new_name = f"{start}.{file_type}"

        # Construct the full paths
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(output_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} to {new_name}")
        start = start + 1

if __name__ == "__main__":
    pdf_filename = "NAME.pdf"
    image_folder = "C:\\X\\X\\Downloads"
    convert_images_to_pdf_jpg_png(image_folder, pdf_filename, 1, 10, "png")
    
    # convert_webp_images_to_pdf(image_folder, pdf_filename, 1, 100)


    folder_path = "C:\\X\\X\\X\\TEST"#<----MAKE SURE FOLDER WITH ONLY THE IMAGES YOU WANT TO RENAME
    output_path = "C:\\X\\X\\Downloads"

    #WARNING!!!!
    #MAKE SURE TO MOVE THE IMAGES INTO A FOLDER WITH ONLY THE IMAGES OR IT WILL RENAME EVERY FILE IN YOUR FOLDER
    # rename_files_by_order(folder_path, 1, "webp")

    #img_show_debug()
