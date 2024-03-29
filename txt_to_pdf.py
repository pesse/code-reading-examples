# Thank you GPT4
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def add_line_numbers(input_file, output_file):
    # Set up the canvas
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Define the font and font size for line numbers
    line_number_font = "Courier"
    line_number_font_size = 10

    # Open the input file and read its contents
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Calculate the line height based on font size
    line_height = line_number_font_size + 2

    # Calculate the maximum line number width
    max_line_number_width = len(str(len(lines)))

    # Set the color for the line numbers
    c.setFillColor(colors.black)

    # Iterate over each line of the text file
    for line_number, line in enumerate(lines, start=1):
        # Replace tabs with three spaces for indentation
        line = line.replace("\t", "")
        line = line.replace("    ", "  ")

        # Calculate the y-coordinate for the line
        y = height - (line_number * line_height)

        # Draw the line number on the left side of the page, respecting whitespaces and indentation
        line_number_text = str(line_number).rjust(max_line_number_width)
        c.setFont(line_number_font, line_number_font_size)
        c.drawString(20, y, line_number_text)

        # Draw the line of text next to the line number
        c.setFont("Courier", 10)
        c.drawString(40, y, line.rstrip())

    # Save the PDF
    c.save()

# Specify the input text file and output PDF file
input_file = "examples\code_reading_at_the_beach_230614.txt"
output_file = "examples\code_reading_at_the_beach_230614.pdf"

# Generate the PDF with line numbers
add_line_numbers(input_file, output_file)
