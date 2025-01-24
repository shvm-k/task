# Fullstack ML PDF Extraction Task

This repository contains a Fullstack project focused on extracting structured text data (such as names, emails, and phone numbers) from PDF documents. It includes both backend and frontend implementations to process PDFs and display the extracted data.

---

## **Features**
- **Backend**: Implements a FastAPI-based server to parse PDF files and extract structured information using PyMuPDF.
- **Frontend**: A React-based UI for uploading PDF files and displaying extracted data.
- **PDF Parsing**: The `extract_pdf.py` script parses PDFs and extracts relevant fields like name, email, and phone number.
- **Modular Design**: Separation of backend and frontend for scalability and ease of maintenance.

---

## **File Structure**
```plaintext
fullstack-ml-project/
├── frontend-app/
│   ├── src/
│   │   ├── App.js                # Main React component
│   │   ├── FileUploader.js       # Component for uploading PDFs and showing results
│   │   └── ...                   # Other React components and assets
│   ├── public/
│   ├── package.json              # React dependencies
│   └── ...
├── backend/
│   ├── app.py                    # FastAPI server
│   └── extract_pdf.py            # PDF extraction logic using PyMuPDF
└── README.md                     # Project documentation

```
---
## Technologies Used
### Backend:
Python
FastAPI
PyMuPDF (PDF Parsing)
### Frontend:
React.js
Axios (API communication)

---

## Setup and Usage

### Backend
Navigate to the backend folder:
```plaintext
cd backend
```

Install Python dependencies:
```plaintext
pip install fastapi uvicorn pymupdf
```

Run the API server:
```plaintext
uvicorn app:app --reload
```
The api will be available at http://127.0.0.1:8000



### Frontend
Navigate to the frontend folder:
```plaintext
cd frontend-app
```

Install React dependencies:
```plaintext
npm install
```

Run the development server:
```plaintext
npm start
```
The app will run on http://localhost:3000.
