## 📚 PDF to Audiobook Converter

Convert any PDF file into a lifelike audiobook using [AWS Polly](https://aws.amazon.com/polly/). This Python script extracts text from a PDF, splits it into manageable chunks, and generates high-quality MP3 files using neural voices.

---

### 🎯 Features

- ✅ Extracts text from multi-page PDFs
- 🗣️ Converts text to speech using AWS Polly
- 🔊 Saves audio in MP3 format, chunked for long documents
- 🌍 Supports multiple voices and languages (e.g., English, Spanish)
- 📁 Outputs audio files to a clean directory

---

### 🛠 Requirements

- Python 3.8+
- AWS account with Polly access
- AWS CLI configured with credentials

Install dependencies:

```bash
pip install boto3 pdfplumber
```

---

### 🚀 Usage

1. **Configure AWS CLI** (if not already done):

```bash
aws configure
```

2. **Run the script**:

```bash
python pdf_to_audiobook.py
```

Update the script with your PDF filename:

```python
pdf_file = "your_file.pdf"
pdf_to_audiobook(pdf_file)
```

Audio files will be saved in the `audiobook/` folder.

---

### 🧠 Voice Options

Change the voice by passing a different `VoiceId`:

```python
pdf_to_audiobook(pdf_file, voice="Matthew")  # Male voice
pdf_to_audiobook(pdf_file, voice="Lupe")     # Spanish voice
```

See [Polly voices list](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html) for more options.

---

### 📦 Output

- `audiobook/part_1.mp3`
- `audiobook/part_2.mp3`
- ...

Each part corresponds to a chunk of text from the PDF.

---

### 🧪 Future Enhancements

- GUI for file selection and playback
- Merge MP3 chunks into a single file
- Chapter detection and naming
- Language auto-detection and localization

---

### 📄 License

MIT License — free to use, modify, and share.
