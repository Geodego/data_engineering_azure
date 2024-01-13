from PIL import Image


def convert_png_to_pdf(png_file, pdf_file):
    # Open the PNG image
    image = Image.open(png_file)

    # Converting to RGB, necessary for PDF conversion
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Save the image as PDF
    image.save(pdf_file, 'PDF', resolution=100.0)


# Usage
png_file = '/home/geoffroy/Projects/data_engineering_azure/2-data_warehouses/0-images/chap6/star duration.png'
pdf_file = '/home/geoffroy/Projects/data_engineering_azure/6-project/star duration.pdf'

convert_png_to_pdf(png_file, pdf_file)
