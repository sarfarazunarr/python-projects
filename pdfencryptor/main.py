import pikepdf

sample_pdf = pikepdf.Pdf.open('SAMPLE_PDF')

no_extraction = pikepdf.Permissions(extract=False)

sample_pdf.save('DOC_NAME', encryption= pikepdf.Encryption(user='YOURPASS', owner='OWNER', allow=no_extraction))
