## CSVPDFusion

### Description:
A Python based solution for generating PDF files tailored for note-taking on specific programming topics. The topics and the number of pages dedicated to each are sourced from a CSV file. Each topic receives a master page with the topic name as a header and footer, followed by additional pages with the topic name as a footer. All pages feature lines for note-taking purposes.

### Features:
- Dynamic generation of note-taking templates based on the input CSV file.
- Master page for each topic with the topic name as a header and footer.
- Additional pages for each topic with the topic name only as a footer.
- Empty lines on all pages for note-taking.

### Technologies Used:
- **Python**
- **FPDF**: For PDF generation.
- **Pandas**: For CSV data manipulation.
- **CSV**: Data storage for topics.

### How to Use:
1. Ensure you have Python installed on your machine.
2. Clone this repository.
3. Navigate to the project directory.
4. Install the required libraries using the command: pip install -r requirements.txt
5. Run `main.py`: python main.py
6. Check the generated "output.pdf" in the project directory.

### Files in the Repository:
- **main.py**: The main script that generates the PDF.
- **topics.csv**: Contains the list of programming topics and the number of pages dedicated to each.
- **requirements.txt**: Contains the required Python libraries for the project.
- **.gitignore**: Specifies files and directories that are to be ignored by Git.

### Contribution:
Feel free to fork this repository, make changes, and submit pull requests. Any feedback or suggestions are welcome!
"""
