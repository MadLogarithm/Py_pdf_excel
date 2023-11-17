package org.example;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.Rectangle;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.text.PDFTextStripper;

import java.io.File;
import java.io.PrintWriter;

public class PdfCroppingExample {
    public static void main(String[] args) {
        try {
            // Load PDF
            Document pdfDocument = new Document("./pdf/gg.pdf");


            // Get reference of page
            for(int i = 1; i <= pdfDocument.getPages().size(); i++) {
                Page page = pdfDocument.getPages().get_Item(i);

                System.out.println(page.getCropBox());
                System.out.println(page.getTrimBox());
                System.out.println(page.getArtBox());
                System.out.println(page.getBleedBox());
                System.out.println(page.getMediaBox());

                // Create new Box Rectangle
                Rectangle newBox = new Rectangle(0, 73, 1000, 788);

                // Assign new box
                page.setCropBox(newBox);
                page.setTrimBox(newBox);
                page.setArtBox(newBox);
                page.setBleedBox(newBox);
            }


            // Save cropped PDF
            pdfDocument.save("./drop_pdf/gg.pdf");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}