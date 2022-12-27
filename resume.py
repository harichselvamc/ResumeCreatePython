from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas

def build_ats_resume(name, email, phone, education, experience, skills):
  # Create a canvas with a letter-sized page
  canvas = Canvas("resume.pdf", pagesize=letter)

  # Add the header with the name and contact information
  canvas.setFont("Helvetica", 16)
  canvas.drawString(50, 750, name)
  canvas.setFont("Helvetica", 12)
  canvas.drawString(50, 735, email)
  canvas.drawString(50, 720, phone)

  # Add the education section
  canvas.setFont("Helvetica", 14)
  canvas.drawString(50, 690, "Education:")
  canvas.setFont("Helvetica", 12)
  y = 670
  for degree in education:
    canvas.drawString(50, y, degree)
    y -= 15

  # Add the experience section
  canvas.setFont("Helvetica", 14)
  canvas.drawString(50, y, "Experience:")
  y -= 20
  canvas.setFont("Helvetica", 12)
  for job in experience:
    canvas.drawString(50, y, job)
    y -= 15

  # Add the skills section
  canvas.setFont("Helvetica", 14)
  canvas.drawString(50, y, "Skills:")
  y -= 20
  canvas.setFont("Helvetica", 12)
  for skill in skills:
    canvas.drawString(50, y, skill)
    y -= 15

  # Save the PDF
  canvas.save()

name =input("enter your name: ")
email =input("enter your email address")
phone =input("enter your phone number")
education =tuple(input("enter your education"))
experience =tuple(input("enter your experience"))
skills = tuple(input("enter your skills"))



build_ats_resume(name, email, phone, education, experience, skills)\

print("Your resume is saved successfully")